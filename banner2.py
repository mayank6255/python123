#!/usr/bin/python


import os

import time


WIDTH = 79

#the message we wish to print
message = "hacker!".upper()

printedMessage = [ "","","","","","","" ]


characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " " ],

               "E" : [ "*****",
                       "*    ",
                       "*    ",
                       "*****",
                       "*    ",
                       "*    ",
                       "*****" ],
               
               "H" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "*   *" ], 

               "A" : [ " *** ",
                       "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "*   *" ],

               "C" : [ "*****",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*****" ],

               "K" : [ "*   *",
                       "* *  ",
                       "**   ",
                       "**   ",
                       "* *  ",
                       "*   *",
                       "*    "],
               "R" : [ "*****",
                       "*   *",
                       "*   *",
                       "*****",
                       "**   ",
                       "* *  ",
                       "*  * "],
                       
               "!" : [ "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "     ",
                       "  *  " ]
               
               }



for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")


offset = WIDTH
while True:
    os.system("clear")
 
    for row in range(7):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
  
    offset -=1

    if offset <= ((len(message)+2)*6) * -1:
        offset = WIDTH

    time.sleep(0.05)
