import serial
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

ser = serial.Serial('COM6', 9600, timeout=1) # COM port can be set to whatever port is being used by microcontroller
devices = AudioUtilities.GetSpeakers() # Using the Pycaw library to control PC volume
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
currPos = 0
currVol = volume.GetMasterVolumeLevelScalar()
startPos = 0
volChange = .05 # Volume will be changed in increments of .05


while True:

    currVol = volume.GetMasterVolumeLevelScalar() # Get the system volume when script starts

    line = ser.readline() # read rotary encoder value from the serial monitor

    if line:
        string = line.decode() # convert byte value to a string
        currPos = int(string) # cast string to an integer

    if currPos == startPos:
        continue # if no change in rotary encoder, do nothing

    if currPos > startPos and currVol != 1: # if rotary encoder turned to the right, and volume isn't max
        if abs(1-currVol < volChange): volume.SetMasterVolumeLevelScalar(1, None) # if value can't be incremented by .05, set it straight to max
        else: volume.SetMasterVolumeLevelScalar(currVol + volChange, None) # otherwise, increment volume by number of turns

    elif currPos < startPos and currVol != 0: # same as above, but volume is decreased
        if currVol-volChange < 0: volume.SetMasterVolumeLevelScalar(0, None)
        else: volume.SetMasterVolumeLevelScalar(currVol - volChange  , None)

    startPos = currPos # set current position of rotary encoder so that change can be measured. 
