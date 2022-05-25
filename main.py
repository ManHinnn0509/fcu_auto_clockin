import os
import io
import time
from datetime import datetime
from PIL import Image
from pytesseract import *

import requests as req
from bs4 import BeautifulSoup as BS
from dotenv import load_dotenv

from const import *

def main():
    # Default: Clock-in every 15 mins
    SLEEP_MINS = 15
    SLEEP_SECS = SLEEP_MINS * 60

    load_dotenv()

    NID = os.getenv("NID")
    PASSWORD = os.getenv("PASSWORD")

    # Windows
    if (os.name == "nt"):
        WINDOWS_TESSERACT_BINARY_PATH = os.getenv("WINDOWS_TESSERACT_BINARY_PATH")
        if (WINDOWS_TESSERACT_BINARY_PATH == None):
            print("Tesseract binary not found.")
            print("Please see: https://stackoverflow.com/questions/50655738/how-do-i-resolve-a-tesseractnotfounderror")
            return
        
        pytesseract.tesseract_cmd = WINDOWS_TESSERACT_BINARY_PATH
    
    # Done of initializing the program

    nextClockIn = int(time.time())

    while (True):

        timeNow = int(time.time())
        if (timeNow >= nextClockIn):
            nextClockIn = timeNow + SLEEP_SECS

            result, msg, code = clockIn(NID, PASSWORD)
            print(f"[{getDateTimeNow()}] {NID}: {msg} (Code: {code})")

        # Sleep for 1 min (Check every 1 min)
        try:
            time.sleep(60)
        except:
            break

    print("--- End of Program ---")

def clockIn(nid: str, password: str):
    loginData = {
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        'LoginLdap$LoginButton':'登入'
    }

    s = req.session()

    firstResponse = s.get(LOGIN_URL)
    html = BS(firstResponse.text, "html.parser")

    for i in html.find_all("input", {"type": "hidden", "value": True}):
        name = str(i["name"])
        value = str(i["value"])
        loginData[name] = value
    
    loginData['LoginLdap$UserName'] = nid
    loginData['LoginLdap$Password'] = password

    loginResponse = s.post(LOGIN_URL, headers=HEADERS, data=loginData)

    failMsg = "您的登入嘗試失敗。請再試一次"
    if (failMsg in loginResponse.text):
        return False, "Unable to login with given NID & Password.", None
    
    # ---

    gotoCheckIn = {}
    html = BS(loginResponse.text, "html.parser")

    for i in html.find_all("input", {"type": "hidden", "value": True}):
        name = str(i["name"])
        value = str(i["value"])
        gotoCheckIn[name] = value
    
    gotoCheckIn["ButtonClassClockin"] = "學生課堂打卡"

    # ---

    checkInData = {}

    mainPage = s.post(MAIN_PAGE_URL, headers=HEADERS, data=gotoCheckIn)
    html = BS(mainPage.text, "html.parser")

    r = s.get(VALIDATE_CODE_URL)
    imgBytes = io.BytesIO(r.content)
    img = Image.open(imgBytes)

    imgText = str(image_to_string(img, config="--psm 6 tessedit_char_whitelist=0123456789"))
    code = imgText.replace("\n", "")
    checkInData["validateCode"] = code
    
    button = html.find("input", {"type": "submit", "name": "Button0"})
    if (button == None):
        return False, "You don't have any classes now.", code

    checkInData["Button0"] = button["value"]
    for i in html.find_all("input", {"type": "hidden", "value": True}):
        name = str(i["name"])
        value = str(i["value"])
        checkInData[name] = value

    # ---

    result = s.post(CLOCK_IN_URL, headers=HEADERS, data=checkInData)
    html = BS(result.text, "html.parser")

    try:
        disabled = html.find("input", {"type": "submit", "name": "Button0"})
        if (disabled["disabled"] != "disabled"):
            return False, "Unable to clock in.", code
        
        return True, "Clock in SUCCESS!", code
    
    except Exception as e:
        print(repr(e))
        return False, "Unable to clock in.", code

def getDateTimeNow():
    """
        Format example: "2021-05-28 23:45:15"
    """
    now = str(datetime.now())
    now = now.split(".")[0]
    return now

if (__name__ == "__main__"):
    main()