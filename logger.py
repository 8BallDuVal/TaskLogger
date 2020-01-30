from win32gui import GetWindowText, GetForegroundWindow
from datetime import datetime
import time
import io

try:
    with io.open('logging_events.csv', "w", encoding="utf-8") as f:
        f.write('Timestamp, Time Elapsed (seconds), Event')
        f.write('\n')
        newEvent = True
        while(1):
            if newEvent == True:
                start = time.time()
                newEvent = False
            time_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            window = GetWindowText(GetForegroundWindow())
            time.sleep(0.5) 
            if GetWindowText(GetForegroundWindow()) != window:
                end = time.time()
                elapsed = end - start
                print('Timestamp: ',time_date, ' | Time elapsed (sec): ', elapsed, ' | Event: ', GetWindowText(GetForegroundWindow()))
                f.write(time_date)
                f.write(', ')
                f.write(str(elapsed))
                f.write(', ')
                f.write(GetWindowText(GetForegroundWindow()))
                f.write('\n')
                newEvent = True  
            f.flush()
except:
    f.close()