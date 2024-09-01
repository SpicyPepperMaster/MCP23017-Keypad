import board
import busio
import time
from adafruit_mcp230xx.mcp23017 import MCP23017
import digitalio

# Initialize I2C bus and MCP23017
i2c = busio.I2C(board.GP3, board.GP2)
mcp = MCP23017(i2c, address=0x24)

# Define row and column pins
rows = [mcp.get_pin(i) for i in range(8)]  # GPB0 to GPB7
rows += [mcp.get_pin(8), mcp.get_pin(9)]   # GPA0 to GPA1 (key_row9, key_row10)
cols = [mcp.get_pin(i) for i in range(10, 16)]  # GPA2 to GPA7

# Set all row pins as outputs and set them high
for row in rows:
    row.switch_to_output(value=True)

# Set all column pins as inputs with pull-up resistors
for col in cols:
    col.switch_to_input(pull=digitalio.Pull.UP)

def check_keys():
    for row_num, row in enumerate(rows):
        # Drive the current row low
        row.value = False
        
        # Small delay to allow the signal to propagate
        time.sleep(0.001)
        
        for col_num, col in enumerate(cols):
            if not col.value:  # If the column pin is low, the button is pressed
                print(f"Button pressed at Row {row_num + 1}, Column {col_num}")
        
        # Reset the row pin high
        row.value = True
        
        # Another small delay to avoid false triggers when switching rows
        time.sleep(0.001)

while True:
    check_keys()
    time.sleep(0.1)  # Add a slight delay to avoid insane console spam

