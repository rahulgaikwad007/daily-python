from datetime import datetime
from playsound import playsound
import winsound

#take time input in the HH:MM  12 hour format
alarm_date= input("Set the alarm date: ").strip()
alarm_time=''.join(input("Set the alarm time in HH:MM in 12 hour format: ").split())
ringtone= input("Set the ringtone for alarm: m for music/ b for beep  ")

if ringtone=='b':
    dur=int(input("Ringtone will play for(in seconds): "))*1000 #miliseond to sec conversion
    freq= int(input("Noise freq: "))
alarm_hour=alarm_time[0:2]
alarm_minute= alarm_time[3:5]
alarm_period= alarm_time[6:8].upper()

print("Setting alarm.....")

while True:
    current_time= datetime.now()
    current_hour=current_time.strftime("%H")
    current_minute= current_time.strftime("%M")
    current_period= current_time.strftime("%p")
    current_date= current_time.strftime("%d %m %y")

    if current_date==alarm_date and current_period==alarm_period and current_hour==alarm_hour and current_minute==alarm_minute:
        print("*"*10)
        print('||' +'wake up!'+'||')
        print('*'*10)

        if ringtone=='m':
            playsound('E:\Engineer\Projects\python-applications\alarm-clock\music.wav')

        else:
            winsound.Beep(freq, dur)
        
        break
