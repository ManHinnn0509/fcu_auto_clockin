# fcu_auto_clockin
逢甲大學 - 自動打卡系統

This is an edited & Python 3 version script of [this](https://github.com/tamama9527/autopunch-full/blob/master/autopunch.py)

## How to install

### Windows

1) Install Python3 from [here](https://www.python.org/downloads/)

2) Run `pip install -r requirements.txt` in cmd (In this directory)

3) Create a `.env` file in this directory with following template:

```
NID=YOUR_NID_HERE
PASSWORD=YOUR_PASSWORD_HERE

WINDOWS_TESSERACT_BINANY_PATH=
```

4) Download the binary installer from [here](https://github.com/UB-Mannheim/tesseract/wiki)

5) Get the absolute path of `tesseract.exe` and fill it into `WINDOWS_TESSERACT_BINANY_PATH` like this:

```
# Example
WINDOWS_TESSERACT_BINANY_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
```

6) Should be good to go, run `python main.py`

### Linux

1) Install Python3 from [here](https://www.python.org/downloads/)

2) Run `pip install -r requirements.txt` in terminal (In this directory)

3) Create a `.env` file in this directory with following template:

```
NID=YOUR_NID_HERE
PASSWORD=YOUR_PASSWORD_HERE
```

4) If you haven't installed Tesseract yet, type `sudo apt install tesseract-ocr` in terminal

5) Should be good to go, run `python3 main.py`

## DISCLAIMER

This script is for **educational purposes only**
