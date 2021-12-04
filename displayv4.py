#This program is used for displaying numbers and characters on 14 segment LCD
#The number range that the program can display is 0.000-99999 
#It only displays the first 4 character or int number, the rest will be discarded
#for decimal number, examples: 1.234 12.34 123.4 1234. 
#usage: python displayv4.py 123.4 
import sys
import string
import os


display={
"0":["0x3f",0x0], 
"1":["0x6",0x0],
"2":["0xdb",0x0],
"3":["0xcf",0x0],
"4":["0xe6",0x0],
"5":["0xed",0x0],
"6":["0xfd",0x0],
"7":["0x1",0xc],
"8":["0xff",0x0],
"9":["0xe7",0x0],
".":["0x0",0x40],
"+":["0xc0",0x12],
" ":["0x0",0x0],
"-":["0xc0",0x0],
"A":["0xF7",0x0],
"B":["0x8F",0x12],
"C": ["0x39",0x0],
"D": ["0xF",0x12],
"E": ["0xF9",0x0],
"F": ["0xF1",0x0],
"G": ["0xBD",0x0],
"H": ["0xF6",0x0],
"I": ["0x9",0x12],
"J": ["0x1E",0x0],
"K": ["0x70",0x24],
"L": ["0x38",0x0],
"M": ["0x36",0x5],
"N": ["0x36",0x21],
"O": ["0x3F",0x0],
"P": ["0xF3",0x0],
"Q": ["0x3F",0x20],
"R": ["0xF3",0x20],
"S": ["0xED",0x0],
"T": ["0x0",0x12],
"U": ["0x3E",0x0],
"V": ["0x30",0xC],
"W": ["0x36",0x28],
"X": ["0x0", 0x2D],
"Y": ["0x0",0x15],
"Z": ["0x9",0xC],
"a": ["0x58",0x10],
"b": ["0x78",0x20],
"c": ["0xD8",0x0],
"d": ["0x8E",0x8],
"e": ["0x58",0x8],
"f": ["0x71",0x0],
"g": ["0x8E",0x4],
"h": ["0x70",0x10],
"i": ["0x0",0x10],
"j": ["0xE",0x0],
"k": ["0x0",0x36],
"l": ["0x30",0x0],
"m": ["0xD4",0x10],
"n": ["0x50",0x10],
"o": ["0xDC",0x0],
"p": ["0x70",0x1],
"q": ["0x86",0x4],
"r": ["0x50",0x0],
"s": ["0x88",0x20],
"t": ["0x78",0x0],
"u": ["0x1C",0x0],
"v": ["0x4",0x20],
"w": ["0x14",0x28],
"x": ["0xC0",0x28],
"y": ["0xC",0x28],
"z": ["0x48",0x8]
}
def dojob(cmd1,cmd2):
    os.system(cmd1)
    os.system(cmd2)

def printjob(cmd1,cmd2):
    print(cmd1)
    print(cmd2)

def executeCommand(addr1,addr2, unit_value):
        myCmd1 = "i2cset -y 2"
        myCmd2 = "i2cset -y 2"
        outside = " 0x70 %s %s w"%(addr1,unit_value[0])
        inside = " 0x70 %s %s w"%(addr2,str(unit_value[1]))
        myCmd1 += outside
        myCmd2 += inside
        #printjob(myCmd1, myCmd2)
        dojob(myCmd1, myCmd2)
def getValue(character):
        for key, value in display.items():
                if character==key:
                        return value
def getUnit_addr(unit):
    unit_addr={0:["0x0","0x1"],1:["0x2","0x3"],2:["0x4","0x5"],3:["0x6","0x7"]}
    for key,value in unit_addr.items():
        if unit==key:
            return value
def displaySeg(value):
    unit_value=""
    if ((type(value)==int)&(value>9999)&(value<99999)):
            value =float(value)/1000
            #value=round(value,1)
            value=str(value)[0:4]
            valuelen=len(value)
    else:
        value=str(value)
        valuelen=len(value)
        if (valuelen<4):
            value=(4-valuelen)*" "+value
            valuelen=4
        elif(valuelen>4):
            if ("." in value[0:5]):
                valuelen=5
            else:
                valuelen=4
    if (valuelen==4):
        for i in range(valuelen):
            unit_value=getValue(value[i])
            #print(value[i])
            #print(unit_value)
            address1 = getUnit_addr(i)[0]
            address2 = getUnit_addr(i)[1]       
            executeCommand(address1,address2,unit_value)
    else:
             #has "." in the string; string length is 5
             #if next element is ".", turn on the "." of the unit.
        valuelist=value.split(".")
        #.split() generate a list
        for i in range(len(valuelist[0])):
            unit_value=getValue(valuelist[0][i])
            if (i==(len(valuelist[0])-1)):
            #last element in the splited string, means a "." is after it
                unit_value[1]=unit_value[1]|0x40
            #print(valuelist[0][i])
            #print(unit_value)
            address1 = getUnit_addr(i)[0]
            address2 = getUnit_addr(i)[1]       
            executeCommand(address1,address2,unit_value)
        for i in range(4-len(valuelist[0])):
            unit_value=getValue(valuelist[1][i])
            #print(valuelist[1][i])
            i+=len(valuelist[0])
            #print(unit_value)
            address1 = getUnit_addr(i)[0]
            address2 = getUnit_addr(i)[1]       
            executeCommand(address1,address2,unit_value)

def main():
        if (len(sys.argv)<2):
                
                print"run the command in the following format:"
                print"python display.py string"
        else:
                displaySeg(sys.argv[1])
if __name__=='__main__':
        main()

