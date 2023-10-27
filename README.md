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
**1. Display Current Time**: The clock will show the current hour, minute, and second.  
**2. Date Setting**: Display the local year, month, day, and day of the week.  
**3. Language Setting**: preferred text language and announcement language for the target user. 
**4. Time Announcement**: Deliver a clear and concise bilingual time announcement capability in both Chinese and English.  
**5. Time Zone Setting**: Allow users to choose or set their desired time zone to ensure the clock displays the correct local time.  
**6. Alarm Function**: Allow users to set one or more alarms to receive reminders at specific times and pause them as well. 
**7. Snooze**: Allow users to "snooze for 5 minutes" by clicking a button that automatically sets an alarm for 5 minutes later.  
**8. Background Automation**: Visually remind customers of the local time by providing both daytime and nighttime backgrounds.  
**9. Countdown Timer**: Develop a countdown timer function in hours / minutes, and offer users the option to select their preferred ringtone.  

#### Voice Integration
**1. Text Preparation**: Begin by structuring the text for both languages. In Chinese, it should be in the format: “现在是” + “上午/下午” + the hour + “点” + the minute. For English, structure it as: “It’s” + the minute + past/for + the hour”.  
**2. File Naming**: Associate each text with a relevant file name for the generated audio.  
**3. Text-to-Speech Conversion**: Utilize Google Text-to-Speech (TTS) to convert the prepared text into audio, ensuring that the correct language and accent settings are in place for each language.  
**4. Audio Recording**: We have recorded 'it's / o'clock / a quarter past / a quarter to / half past / minutes past minutes to / 1-29 (except for 15)' according to time and code logic.  
**5. File Output**: Save the resulting audio as WAV files with meaningful file names, ideally organized in a well-structured directory.  
**6. Modular Implementation**: Integrate this process into a modular component within your program, allowing easy and seamless time announcements in either language.”  

#### User Interface and Customization
**1. Display Clarity**: Ensure that the numbers and text on the clock are easily legible, allowing users to effortlessly read the time.  
**2. Font Customization**: Employ a charming and rounded typeface to enhance the clock's aesthetics.  
**3. Display Layout**: Consider the layout of numbers and buttons for easy comprehension. Separate the display of hours, minutes, and seconds clearly. Arrange the buttons in a manner consistent with existing English web and app products, aligning with user familiarity to facilitate a quick learning curve. Adjust the buttons and various components to appropriate sizes to create a harmonious overall visual composition.  
**4. Brightness and Contrast**: Ensure the clock's brightness and contrast are appropriate for various lighting conditions. The time display and background should exhibit contrast while maintaining an overall harmonious effect to ensure user comfort.  
**5. Voice Control**: Ensure that synthesized voice commands are clear and maintain an average pace in line with the respective language's norms.  
**6. User-Friendliness**: Allow language switching for buttons, organize buttons logically, and provide text or symbol. labels to ensure that clock settings and customization options are easily understood and used, preventing user confusion.  
**7. Personalized Service**: Tailor to the preferences of late risers and those prone to forgetfulness by offering the option to "remind me again in 5 minutes," thus enhancing the user experience.  
**8. Background Settings**: Offer different backgrounds for day and night, not only for intuitive time representation but also to adapt to the ambient lighting conditions.  
**9. Language Settings**: Support multiple languages to ensure global users can understand and use the clock.  
**10. Time Zone Selection**: Make it easy for users to select their desired time zone for displaying accurate local time. Ensure the clock displays the current time in real-time without noticeable delays or asynchrony.  
**11. Date Display**: Show the local date and day of the week, helping users quickly access date information.  
**12. Alarm Functionality**: Provide users with the ability to set alarms, allowing them to independently pause music or ringtone.  
**13. Music**: We altered different musics to find the best one for the alarm, not only serving as a reminder but also provide a delightful wake-up (reminder) service, pleasing to the ear for customers.  
**14. Diverse Selection**: We offer our customers a wide array of choices for countdown alert ringtones, allowing them to customize their settings based on individual needs and preferences.

## Technical documentation and reflection
### Code



### Audio Recording
**1. Speech Rate**: Maintain a roughly consistent pace for each individual word, particularly with numbers, to avoid variations in speed that can result in unclear English voice time announcements.  

**2. WAV Segment Duration**: When extracting audio using Praat software, endeavor to make the audio length of each number approximately equal. This helps prevent situations where the minute announcement hasn't been completed yet, while the hour announcement has already begun.  

**3. Utilizing Appropriate Waiting Durations**: Only when audio durations are approximately equivalent can we determine suitable waiting periods between two audio segments. On this foundation, constant adjustments are made to achieve the most appropriate interval duration. Too short of a pause can lead to unclear time announcements, while overly lengthy pauses can reduce efficiency and make the announcements sound less like artificial intelligence-generated responses.  

## User Manual
Run `python main.py` in the terminal. Make sure to be in the same directory where
the repository is installed in the terminal. It will open an interactive GUI with which
you can interact with.

**Language Switch**  
Written Language: Click the "EN-中" button in the top left corner to switch the text language.  
Time-telling Language: Choose either of the time-telling buttom as your prefrred language.  
For Example: EN-*What time is it*  /  中-*现在几点了*  
We will display hours, minutes, and seconds, but when announcing verbally, we won't mention the seconds.

**Timezone Slection**  
This Clock operates on a twelve-hour system  
"AM" - "ante meridiem" 
"PM" -"post meridiem"  
*- Tokyo: Japan Standard Time (JST) Latitude:35.682839°N, Longitude:139.759455°E.*  
*- Shanghai: China Standard Time (CST) Latitude:31.230416°N, Longitude:121.473701°E.*  
*- New York: Eastern Standard Time (EST) Latitude:40.712776°N, Longitude:74.005974°W.*  
*- Amsterdam): Central European Time (CET) Latitude:52.366697°N, Longitude:4.894540°E.*  
*- LondonGreenwich Mean Time (GMT) Latitude:51.507351°N, Longitude:0.127758°W.*  

**Date: yy-mm-dd**  
Date changes with time zones and attached with Monday - Sunday

**Alarm**  
The clock icon can be clicked to set an alarm. Clicking the button will bring up an interactive window with two sliders to set the reminder time. Once the settings are completed, the alarm time will be displayed on the screen for your reference. The alarm will play music when it's time. Also, clicking the "Stop" buttom would pause the music as you will.

**Snooze**  
If you wish to "snooze for 5 minutes," simply press the "Snooze" button, and the system will automatically set an alarm to gently awaken you again in 5 minutes, providing you with a delightful morning experience.

**Daytime & Nighttime Indication**  
The images daytime and nighttime are setted as background. The two models switch automatically to indicate the time.  

**Countdown Timer**  
Select the countdown icon and, in the pop-up interface, configure the countdown duration by:  
*(1) Choosing the time unit - hours/minutes;*  
*(2) Manually entering the numerical value;*  
*(3) Selecting a preferred alert ringtone (or using the default ringtone).*  

##  Licensing and FAIR Data Principles
The significance of Licensing and adherence to the FAIR data principles in our project is paramount in ensuring the creation of a reliable, inclusive, and ethically responsible tool. Our bilingual time-announcing clock is committed to upholding these principles.

**1. Significance of Licensing and FAIR Data Principle**: Licensing and FAIR data principles hold profound importance. Licensing ensures that our tool is legally and ethically sound, contributing to its trustworthiness and credibility. FAIR principles—Findable, Accessible, Interoperable, and Reusable—ensure that our data and technology are accessible to all, fostering inclusivity and data integrity.

**2. Google Text-to-Speech**: In the context of Chinese voice time announcements, we employ speech synthesis technology, utilizing Google to generate synthetic voices, which allows us to use these voices directly without the need for authorization.

**3. Audio Recording**: In the context of English voice time announcements, we utilize the voice of our team member, J. Shi, with her explicit authorization. Therefore, our process aligns with the FAIR and GDPR principles, ensuring compliance and ethical handling of data and personal information.

**4. Adherence to FAIR Data Principles**:  
   - *Findable: Our clock's dual-language time-announcing functionality enhances its discoverability, catering to a broad, global audience.*  
   - *Accessible: We prioritize ease of use, ensuring our tool is accessible to individuals of varying technological proficiency.*  
   - *Interoperable: Designed to cater to diverse time zones, our project fosters interoperability, delivering precise time data for a global user base.*  
   - *Reusable: The core functionality of our bilingual time-announcing clock is versatile, allowing it to be reused across diverse applications and platforms.* 

**5. GDPR Compliance**: We take pride in confirming that our voice synthesis process adheres to the stringent regulations of the General Data Protection Regulation (GDPR), ensuring users' data privacy and security.  

In summary, our bilingual time-announcing clock represents a trustworthy and inclusive tool, aligning with the ethical standards of data management, licensing, and accessibility.
