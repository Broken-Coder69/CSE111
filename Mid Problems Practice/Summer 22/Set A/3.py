class RickMote:
    def __init__(self):
        self.supported_channels = [0, 2, 3, 6, 7, 9]
        self.power_on = False
        self.channel = 0
        self.volume = 3
    
    def power(self):
        self.power_on = not self.power_on
    

    def changeChannel(self, change=2 ):
        if not self.power_on:
            print(f"Power is turned off. Cannot change channel.")
            
            
        else:
            if change in self.supported_channels:
                self.channel = change
            else:
                print("TV channel does not exist.")

    

    def changeVolumeLevel(self, vol=1):
        if not self.power_on:
            print(f"Power is turned off. Cannot change volume.")
            
        else:
            self.volume += int(vol)
    
    
    def showInfo(self):
        power = ""
        if not self.power_on:
            power += "OFF"
            print(f"ID Cable Box Status:")        
            print(f"Cable Box is: {power}")
        else:
            power += "ON"
            print(f"ID Cable Box Status:")        
            print(f"Cable Box is: {power}")
            print(f"Channel:{self.channel}")
            print(f"Volume:{self.volume}")
            


        




oTV = RickMote()
oTV.power()
print("1.############################")
oTV.showInfo()
print("2.############################")
oTV.changeChannel()
oTV.changeVolumeLevel()
oTV.showInfo()
print("3.############################")
oTV.power()
oTV.showInfo()
print("4.############################")
oTV.power()
oTV.changeVolumeLevel(4)
oTV.changeChannel(3)
oTV.showInfo()
print("5.############################")
oTV.changeVolumeLevel(-2)
oTV.showInfo()
print("6.############################")
oTV.power()
oTV.changeChannel(9)
oTV.changeVolumeLevel(-1)
oTV.showInfo()
print("7.############################")
oTV.power()
oTV.changeChannel(11)
oTV.showInfo()