# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Define pin #4 as output and set it to a PWM mode
GPIO.setup(7, GPIO.OUT)
ServoMotor = GPIO.PWM(7, 50) #50 refers to the frequency in Hz.

# Begin PWM but initialize it to 0
ServoMotor.start(0)
print("Waiting for 2 seconds")
time.sleep(2) # 2 second delay

# Move the servo motor
print("Rotating servo motor")

# Define duty value
duty = 2

# Loop for duty values from 2 to 12 = 0 to 180 degrees
while duty <= 12:
    ServoMotor.ChangeDutyCycle(duty) # Move to current duty cycle
    time.sleep(1) # delay for one second
    duty = duty + 1

# Wait a moment
time.sleep(2)

# Return servo to 90 degrees
print("Turning to 90 degrees for 2 seconds")
ServoMotor.ChangeDutyCycle(7) # 7 = 90 degrees

# Clean things up
ServoMotor.stop() # Stop writing to the servo motor
GPIO.cleanup()
print("2 % better.")

# Making a change
print("Github detect")