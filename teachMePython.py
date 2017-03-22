
import time
import sys

#w petli zmienia sie rozmiar paddingu
#zwracanie obiektu funkcyjnego, ktorego wywolanie daje kolejny numer.

try:
    _passedRate = int(sys.argv[1])
    _passedSize = int(sys.argv[2])
except IndexError:
    print("Default rate and size. (You can specify them as prog. invoke parameters)")
    _passedRate = 300
    _passedSize = 30

RATE_HZ = _passedRate
MAX_SIZE = _passedSize


SLEEP_TIME = 1/RATE_HZ

def fLoop():
    itCount = 0
    while(1):
        growLeftToRight()
        shrinkLeftToRight()
        growRightToLeft()
        shrinkRightToLeft()
        
        #growRightToLeft()
            
def growLeftToRight():
    for i in range(2, MAX_SIZE):
            time.sleep(SLEEP_TIME)
            print(" "*MAX_SIZE+"\r", end="")
            print(getAnimString(i)+ "\r", end="")

def shrinkRightToLeft():
    for i in reversed(range(2, MAX_SIZE)):
            time.sleep(SLEEP_TIME)         
            print(" "*MAX_SIZE+"\r", end="")  
            print(getAnimString(i)+"\r", end="")

def growRightToLeft():
    for i in range(2, MAX_SIZE):
            time.sleep(SLEEP_TIME)
            print(" "*MAX_SIZE+"\r", end="")
            print(" "*(MAX_SIZE-i)+getAnimString(i)+ "\r", end="")

def shrinkLeftToRight():
    for i in reversed(range(2, MAX_SIZE)):
            time.sleep(SLEEP_TIME)         
            print(" "*MAX_SIZE+"\r", end="")  
            print(" "*(MAX_SIZE-i)+getAnimString(i)+"\r", end="")

def getAnimString(n):
    return "^".center(n, '_')

def main():
    print("What: ")
    fLoop()
main()