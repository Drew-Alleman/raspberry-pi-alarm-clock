import time
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO
from Adafruit_CharLCD import Adafruit_CharLCD

# instantiate lcd and specify pins
lcd = Adafruit_CharLCD(rs=26, en=19,
                       d4=13, d5=6, d6=5, d7=11,
                       cols=16, lines=2) #LCD pins change to desire
lcd.clear() # clear LCD screen
old_time = "" # Old time value
GPIO.setmode(GPIO.BCM) # Set Board mode 
GPIO_BUZZER = 18 # Buzzer Pin
GPIO.setup(GPIO_BUZZER, GPIO.OUT) # Set buzzer pin to output

now = datetime.now()
hour = input("Enter hour: ") # Asks user for Hour
min = input("Enter Minute: ") # asks user for minute
time_day = input("AM or PM: ")
alarm = now.replace(hour=int(hour), minute=int(min), second=0, microsecond=0) # Puts input into time value to compare later
alarm_print = alarm.strftime("%H:%M:%S "+time_day) # Pretty Print

while True: # Loop forever
	now = datetime.now() # Get Current time
	current_time = now.strftime("%H:%M:%S %p") # Print that time and alarm time \n = New Line
	if old_time != current_time: # If time has changed by one second. If this bit was removed it would print the time every few nano-seconds
		lcd.clear() # clear screen
		lcd.message(current_time+"\n"+alarm_print) # Print time to LCD screen
		if now >= alarm & time_day in current_time: # if enough time has passed and the time > than the alarm	and its less than 30 minutes ahead		
			lcd.clear() # clear screen
			lcd.message("WAKE UP") # Display message wake up
			GPIO.output(GPIO_BUZZER, True) # Turn on the buzzer
			time.sleep(1) # Sleep for __ seconds and leave the buzzer on
			GPIO.output(GPIO_BUZZER,False) # Turn Buzzer back off
			lcd.clear() # Clear screen again
			exit(0)	 # Exit
		old_time = current_time
 
