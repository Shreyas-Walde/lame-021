from playsound import playsound
import time

CLEAR = "\033[2J"    # clears terminal          
CLEAR_AND_RETURN = "\033[H" # return cusor to home position
# ^ changes character on same line of terminal 

def alarm(seconds):  # how long running
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60  
        seconds_left = time_left % 60 

        print(f"{CLEAR_AND_RETURN}Alarm in:{minutes_left:02d}:{seconds_left:02d}")
                     # make it 2 digits with zero

    playsound("alarm.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)