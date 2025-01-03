import machine
import utime

# GPIO Pin Configuration
pin1 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)  # Edge-triggered
pin2 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)  # Level-triggered

# Interrupt Flags
interrupt_flag1 = False
interrupt_flag2 = False

# Priority Levels
PRIORITIES = {
    "pin1": 1,  # Higher priority
    "pin2": 2   # Lower priority
}

# Interrupt Handlers
def pin1_handler(pin):
    global interrupt_flag1
    interrupt_flag1 = True
    print("Interrupt on pin1 (Edge-Triggered)")

def pin2_handler(pin):
    global interrupt_flag2
    interrupt_flag2 = True
    print("Interrupt on pin2 (Level-Triggered)")

# Attach Interrupts
pin1.irq(trigger=machine.Pin.IRQ_RISING, handler=pin1_handler)  # Rising edge
pin2.irq(trigger=machine.Pin.IRQ_HIGH_LEVEL, handler=pin2_handler)  # High level

# State Machine
def state_machine():
    global interrupt_flag1, interrupt_flag2

    while True:
        # Idle State
        if not (interrupt_flag1 or interrupt_flag2):
            utime.sleep(0.1)
            continue

        # Detect Interrupt
        if interrupt_flag1:
            # Handle Edge-Triggered Interrupt
            print("Handling pin1 interrupt...")
            interrupt_flag1 = False
            handle_interrupt("pin1")

        if interrupt_flag2:
            # Handle Level-Triggered Interrupt
            print("Handling pin2 interrupt...")
            interrupt_flag2 = False
            handle_interrupt("pin2")

# Nested Interrupt Handling
def handle_interrupt(pin_name):
    if pin_name == "pin1" and interrupt_flag2:
        if PRIORITIES["pin2"] > PRIORITIES["pin1"]:
            print("Nested interrupt: Handling pin2 first...")
            handle_interrupt("pin2")

    print(f"Interrupt handled for {pin_name}")

# Start the State Machine
state_machine()

