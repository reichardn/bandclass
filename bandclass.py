class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
        print ""

class Band(object):
    def __init__(self, band_members):
        self.band_members = band_members
        
    def hire(self, musician):
        self.band_members.append(musician)
    
    def fire(self, fired):
        self.band_members.remove(fired)
    
    def perform(self):
        for band_member in self.band_members:
            if type(band_member) == Drummer:
                band_member.count_off()
        for band_member in self.band_members:
            band_member.solo(5)

class Drummer(Musician): 
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Drummer, self).__init__(["Bang", "Crash", "Bash"])
        
    def count_off(self):
        print("1, 2, 3, 4")

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print "Be with you in a moment"
        print "Twoning, sproing, splang"

drummer = Drummer()

guitarist = Guitarist()

bassist = Bassist()

band = Band([drummer, guitarist, bassist])

band.perform()

band.fire(bassist)

band.perform()

band.hire(bassist)
band.perform()


