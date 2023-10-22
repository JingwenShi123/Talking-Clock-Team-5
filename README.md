# Talking-Clock-Team-5

## Project description
This is an interactive speaking/talking clock that we developed in Python 3.9 for an assignment for the course "Introduction to Voice Technology" & "Programming" as part of the Voice Technology MSc at RUG - Campus Fryslan.

## Requirements before installing
Make sure you have `Python 3` installed.  
If not, please download the latest 3.12.0 version from here:  
https://www.python.org/downloads/

## Installation Instructions

<b>\### STEPS TO RUN AND INSTALL HAVE BEEN TESTED USING WINDOWS AND MACOS. THERE MAY BE ISSUES OCCURRING FOR LINUX, SO BE ADVISED! ###</b>

1. Click on the green `Code` button at the top of the repository > `Download ZIP`.
2. Extract the ZIP to the location where you want to install it on your computer.

(You can also just clone the repository locally if you are familiar with Git. In that case,
the steps above can be skipped)

3. Open the terminal (or command prompt, depending on the OS you use) and navigate
to where you extracted the zip via the terminal.
4. Run `pip install -r requirements.txt` to install the dependencies required.

## Team Organization and Workflow
### Team organization 
Jingwen Shi  
Lifan Qu   
Yining Lei  
Yilan Wei  
Siqi Zheng  
Shenghuan Ding  

### Project Workflow

#### Basic Clock Functionality
**Display Current Time**  
The clock will show the current hour, minute, and second.  
**Date Setting**  
Display the local year, month, day, and day of the week.  
**Language Setting**  
preferred text language and announcement language for the target user.  
**Time Zone Setting**  
Allow users to choose or set their desired time zone to ensure the clock displays the correct local time.  
**Alarm Function**  
Allow users to set one or more alarms to receive reminders at specific times. 
**Background Setting**  
Visually remind customers of the local time by providing both daytime and nighttime backgrounds.  

#### Audio Recording

#### Voice Integration

#### User Interface and Customization

## Technical documentation and reflection

## User Manual
Run `python main.py` in the terminal. Make sure to be in the same directory where
the repository is installed in the terminal. It will open an interactive GUI with which
you can interact with.

**Language Switch**  
Written Language: Click the "EN-中" button in the top left corner to switch the text language.  
Time-telling Language: Choose either of the time-telling buttom as your prefrred language.  
We will display hours, minutes, and seconds, but when announcing verbally, we won't mention the seconds.

**Timezone Slection**  
This Clock operates on a twelve-hour system  
"AM" - "ante meridiem" 
"PM" -"post meridiem"  
1. Tokyo: Japan Standard Time (JST) Latitude:35.682839°N, Longitude:139.759455°E.  
2. Shanghai: China Standard Time (CST) Latitude:31.230416°N, Longitude:121.473701°E.  
3. New York: Eastern Standard Time (EST) Latitude:40.712776°N, Longitude:74.005974°W.  
4. Amsterdam): Central European Time (CET) Latitude:52.366697°N, Longitude:4.894540°E.  
5. LondonGreenwich Mean Time (GMT) Latitude:51.507351°N, Longitude:0.127758°W.  

**Date: yy-mm-dd**  
Date changes with time zones and attached with Monday - Sunday

**Alarm**  
The clock icon can be clicked to set an alarm. Clicking the button will bring up an interactive window with two sliders to set the reminder time, and the alarm will play music when it's time.

**Daytime & Nighttime**  
The images daytime and nighttime are setted as background. The two models switch automatically to indicate the time.


##  Licensing and FAIR Data Principles
The audio files used were generated using TTS APIs.

No consent forms were required for the collection of this data since there were no individuals recorded by us to generate this speech. The data used for the speaking clock therefore complies with GDPR regulations.
