#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
class HD44780:

    def __init__(self, pin_rs=7, pin_e=8, pins_db=[25, 24, 23, 18]):

	self.tl = ""
	self.bl = ""
        self.pin_rs=pin_rs
        self.pin_e=pin_e
        self.pins_db=pins_db

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_e, GPIO.OUT)
        GPIO.setup(self.pin_rs, GPIO.OUT)
        for pin in self.pins_db:
            GPIO.setup(pin, GPIO.OUT)

        self.clear()

    def clear(self):
        """ Blank / Reset LCD """

        self.cmd(0x33) # $33 8-bit mode
        self.cmd(0x32) # $32 8-bit mode
        self.cmd(0x28) # $28 8-bit mode
        self.cmd(0x0C) # $0C 8-bit mode
        self.cmd(0x06) # $06 8-bit mode
        self.cmd(0x01) # $01 8-bit mode

    def cmd(self, bits, char_mode=False):
        """ Send command to LCD """

        sleep(0.002)
        bits=bin(bits)[2:].zfill(8)

        GPIO.output(self.pin_rs, char_mode)

        for pin in self.pins_db:
            GPIO.output(pin, False)

        for i in range(4):
            if bits[i] == "1":
                GPIO.output(self.pins_db[::-1][i], True)

        GPIO.output(self.pin_e, True)
        GPIO.output(self.pin_e, False)

        for pin in self.pins_db:
            GPIO.output(pin, False)

        for i in range(4,8):
            if bits[i] == "1":
                GPIO.output(self.pins_db[::-1][i-4], True)


        GPIO.output(self.pin_e, True)
        GPIO.output(self.pin_e, False)

    def message(self, text):
        """ Send string to LCD. Newline wraps to second line"""

        for char in text:
            if char == '\n':
                self.cmd(0xC0) # next line
            else:
                self.cmd(ord(char),True)

    def messageBottom(self, text):
        """ Send string to LCD. Newline wraps to second line"""
	self.cmd(0xC0)
        for char in text:
            if char == '\n':
                self.cmd(0xC0) # next line
            else:
                self.cmd(ord(char),True)


    def setTopLine(self, text):
	self.tl = text

    def setBottomLine(self,text):
	self.bl = text
	
    def printLCD(self):
	self.clear()
	self.message(self.tl + "\n" + self.bl)

    def printTopLine(self):
	self.message(" " + self.tl)

    #needs to print spaces where the last output could have been
    def printBottomLine(self):
	self.message("\n" + ' '*(len(self.bl)+1))
	self.message("\n" + self.bl)


if __name__ == '__main__':

    lcd = HD44780()
    
    while True:
	lcd.message(input())
