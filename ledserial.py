import time

import board
import busio
import digitalio


from adafruit_mcp230xx.mcp23017 import MCP23017


i2c = busio.I2C(board.SCL, board.SDA)

mcp = MCP23017(i2c, address=0x20)  # MCP23017 w/ A0 set

pin0 = mcp.get_pin(0)
pin1 = mcp.get_pin(1)
pin2 = mcp.get_pin(2)
pin3 = mcp.get_pin(3)
#x = input("enter the value")

pin0.switch_to_output(value=True)
pin1.switch_to_output(value=True)
pin2.switch_to_output(value=True)
pin3.switch_to_output(value=True)
pin0.value = False
pin1.value = False
pin2.value = False
pin3.value = False
#pin0.pull = digitalio.Pull.DOWN
#pin1.pull = digitalio.Pull.DOWN

def forward():


while True:
	x = input("enter the value")
	if x==('F'):
		pin0.value = True
		pin1.value = False
		pin2.value = True
                pin3.value = False

	elif x==('B'):
		pin0.value = False
		pin1.value = True
		pin2.value = False
                pin3.value = True

	elif x==('L'):
		pin0.value = False
		pin1.value = False
		pin2.value = False
                pin3.value = True

	elif x==('R')
		pin0.value = False
                pin1.value = True
		pin2.value = True
                pin3.value = False

