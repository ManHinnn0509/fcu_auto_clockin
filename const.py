HEADERS = {
    'Host': 'signin.fcu.edu.tw',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://signin.fcu.edu.tw/clockin/login.aspx',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
}

WIFI_HEADERS = {
    'Host': '140.134.18.26',
    'Connection': 'keep-alive',
    'Content-Length': '47',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Origin': 'http://140.134.18.26',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT':'1',
    'Referer': 'http://140.134.18.26/upload/custom/fcu-web/fcu-cp6.htm?cmd=login',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2,ja;q=0.2'
}

LOGIN_URL = "https://signin.fcu.edu.tw/clockin/login.aspx"
MAIN_PAGE_URL = "https://signin.fcu.edu.tw/clockin/Student.aspx"
CLOCK_IN_URL = "https://signin.fcu.edu.tw/clockin/ClassClockin.aspx"
VALIDATE_CODE_URL = "https://signin.fcu.edu.tw/clockin/validateCode.aspx"
