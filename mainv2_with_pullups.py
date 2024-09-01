import board
import busio
import time
from adafruit_mcp230xx.mcp23017 import MCP23017
import digitalio

# Initialize I2C bus and MCP23017
i2c = busio.I2C(board.GP3, board.GP2)
mcp = MCP23017(i2c, address=0x24)

# Define row and column pins individually
row1 = mcp.get_pin(0)  # GPB0
row2 = mcp.get_pin(1)  # GPB1
row3 = mcp.get_pin(2)  # GPB2
row4 = mcp.get_pin(3)  # GPB3
row5 = mcp.get_pin(4)  # GPB4
row6 = mcp.get_pin(5)  # GPB5
row7 = mcp.get_pin(6)  # GPB6
row8 = mcp.get_pin(7)  # GPB7
row9 = mcp.get_pin(8)  # GPA0
row10 = mcp.get_pin(9) # GPA1

col1 = mcp.get_pin(10) # GPA2
col2 = mcp.get_pin(11) # GPA3
col3 = mcp.get_pin(12) # GPA4
col4 = mcp.get_pin(13) # GPA5
col5 = mcp.get_pin(14) # GPA6
col6 = mcp.get_pin(15) # GPA7

# Set all row pins as outputs and set them high (not active)
row1.switch_to_output(value=True)
row2.switch_to_output(value=True)
row3.switch_to_output(value=True)
row4.switch_to_output(value=True)
row5.switch_to_output(value=True)
row6.switch_to_output(value=True)
row7.switch_to_output(value=True)
row8.switch_to_output(value=True)
row9.switch_to_output(value=True)
row10.switch_to_output(value=True)

# Set all column pins as inputs with pull-up resistors
col1.switch_to_input(pull=digitalio.Pull.UP)
col2.switch_to_input(pull=digitalio.Pull.UP)
col3.switch_to_input(pull=digitalio.Pull.UP)
col4.switch_to_input(pull=digitalio.Pull.UP)
col5.switch_to_input(pull=digitalio.Pull.UP)
col6.switch_to_input(pull=digitalio.Pull.UP)

def check_keys():
    # Check Row 1
    row1.value = True
    time.sleep(0.1)
    print(f"Row 1: Col1={col1.value}, Col2={col2.value}, Col3={col3.value}, Col4={col4.value}, Col5={col5.value}, Col6={col6.value}")
    row1.value = False
    time.sleep(0.1)

    # Check Row 2
    row2.value = True
    time.sleep(0.1)
    print(f"Row 2: Col1={col1.value}, Col2={col2.value}, Col3={col3.value}, Col4={col4.value}, Col5={col5.value}, Col6={col6.value}")
    row2.value = False
    time.sleep(0.1)

    # Check Row 3
    row3.value = True
    time.sleep(0.1)
    print(f"Row 3: Col1={col1.value}, Col2={col2.value}, Col3={col3.value}, Col4={col4.value}, Col5={col5.value}, Col6={col6.value}")
    row3.value = False
    time.sleep(0.1)

    # Check Row 4
    row4.value = True
    time.sleep(0.1)
    print(f"Row 4: Col1={col1.value}, Col2={col2.value}, Col3={col3.value}, Col4={col4.value}, Col5={col5.value}, Col6={col6.value}")
    row4.value = False
    time.sleep(0.1)

    # Check Row 5
    row5.value = True
    time.sleep(0.1)
    print(f"Row 5: Col1={col1.value}, Col2={col2.value}, Col3={col3.value}, Col4={col4.value}, Col5={col5.value}, Col6={col6.value}")
    row5.value = False
    time.sleep(0.1)

    # Check Row 6
    row6.value = True
    time.sleep(0.1)
    print(f"Row 6: Col1={col1.value}, Col2={col2.value}, Col3={col3.value}, Col4={col4.value}, Col5={col5.value}, Col6={col6.value}")
    row6.value = False
    time.sleep(0.1)

    # Check Row 7
    row7.value = True
    time.sleep(0.1)
    print(f"Row 7: Col1={col1.value}, Col2={col2.value}, Col3={col3.value}, Col4={col4.value}, Col5={col5.value}, Col6={col6.value}")
    row7.value = False
    time.sleep(0.1)

    # Check Row 8
    row8.value = True
    time.sleep(0.1)
    print(f"Row 8: Col1={col1.value}, Col2={col2.value}, Col3={col3.value}, Col4={col4.value}, Col5={col5.value}, Col6={col6.value}")
    row8.value = False
    time.sleep(0.1)

    # Check Row 9
    row9.value = True
    time.sleep(0.1)
    print(f"Row 9: Col1={col1.value}, Col2={col2.value}, Col3={col3.value}, Col4={col4.value}, Col5={col5.value}, Col6={col6.value}")
    row9.value = False
    time.sleep(0.1)

    # Check Row 10
    row10.value = True
    time.sleep(0.1)
    print(f"Row 10: Col1={col1.value}, Col2={col2.value}, Col3={col3.value}, Col4={col4.value}, Col5={col5.value}, Col6={col6.value}")
    row10.value = False
    time.sleep(0.1)

while True:
    check_keys()
    print("")
    time.sleep(0.1)  # Add a slight delay to avoid spam

