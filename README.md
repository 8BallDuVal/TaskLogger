# TaskLogger
Logs information about the windows/tasks that are currently in focus and outputs a CSV file containing the information.

CSV file contains the following fields:
- Timestamp: the timestamp at which the window/event was opened.
- Time Elapsed (seconds): the time elapsed between the new window/event being opened and the last window/event being opened
- Event: scrapes the title of the window you have open.

There are two files in this repository:
- logger.py: source code for this project. Feel free to copy it, improve on it, etc.
- logger.exe: same as source code, just compiled into an exe using pyinstaller. 

Let me know if you have any questions/concerns by emailing dduval6@outlook.com .




