import datetime
import binascii
import sys
def showTime():
    print datetime.datetime.now().strftime("%H:%M:%S")  
def crack():
    number = 0
    f = open("crc.txt","r")
    lines = f.readlines()
    str1 = ''
    for line in lines:
        crc = int(line,16)
        r = xrange(32, 127)
        for a in r:
            for b in r:
                for c in r:
                    txt = chr(a)+chr(b)+chr(c)
                    crcx = binascii.crc32(txt)
                    if (crcx & 0xFFFFFFFF) == crc:
                        # print hex(crc)
                        # sys.stdout.write(chr(int(txt)))
                        str1 = str1 + chr(int(txt))
        number += 1
        print "find crc "+str(number)
    print str1
if __name__ == "__main__":
    showTime()
    crack()
    showTime()