import machine
import utime

# Setup RTC
rtc = machine.RTC()

# Set current time
rtc.datetime((2025, 1, 2, 0, 9, 0, 0, 0))  # (Year, Month, Day, Weekday, Hour, Minute, Second, Microsecond)

# Setup motor control pins
IN1 = machine.Pin(4, machine.Pin.OUT)  # GPIO4 connected to IN1
IN2 = machine.Pin(5, machine.Pin.OUT)  # GPIO5 connected to IN2

# Function to run the water pump
def start_water_pump():
    IN1.value(1)
    IN2.value(0)
    print("Pump ON: Watering plants")


def stop_water_pump():
    IN1.value(0)
    IN2.value(0)
    print("Pump OFF: Watering complete")


def water_plants():
    while True:
        current_time = rtc.datetime()
        hour, minute = current_time[4], current_time[5]

        # Check for times (10:00 AM and 6:00 PM)
        if (hour == 10 and minute == 0) or (hour == 18 and minute == 0):
            print("Watering plants...")
            start_water_pump()
            utime.sleep(60)  # Keep pump on for 60 seconds
            stop_water_pump()
            utime.sleep(60)  


water_plants()

