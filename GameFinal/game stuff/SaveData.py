import sys, os, pygame
import pprint, pickle
pygame.init()
"""
    This program will create a list of dictionaries
    need to add sprite features to make this easier to print out as a menu
    The "raw_input" function down in main() will not work in pygame
    pprint is the pretty print module
    pickle is for serializing data
    order of data is as folllows
    charname,savename,livesleft, level,score,locationxy
"""


class Gamedatasaver(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        
    def gamedatapickle(self, datalist, filename, listlength):
        if os.path.isfile(filename):
            filehandle = open(filename, "r")
            getsavedlist = pickle.load(filehandle)
            filehandle.close()
            
            if len(getsavedlist) >= listlength:
                getsavedlist.pop()
            getsavedlist.insert(0, datalist)
            filehandle = open(filename, "w")
            pickle.dump(getsavedlist, filehandle)
            filehandle.close()
            print "File opened successfully"
        else:
            filehandle = open(filename, "w")
            createsavedlist = []
            createsavedlist.append(datalist)
            pickle.dump(createsavedlist, filehandle)
            filehandle.close()

    def gamedataunpickle(self, filename):
        filehandle = open(filename, "r")
        self.gamedictretrieved = pickle.load(filehandle)
        filehandle.close()

    def printtest(self):
        """just for testing purposes, needs work"""
        counter = 0
        for game in self.gamedictretrieved:
            print counter+1,". ", game["savename"]
            counter+=1

def main():
    gamesavefile = "game_save_textfile_class_02.txt"
    charname = "zaphod"
    level = 5
    livesleft = 3
    score = 15000
    locationxy = (454,233)
    listlength = 10
    gamedict = {}
    gamedict["charname"] = charname
    gamedict["savename"] = raw_input("Save name: ")
    gamedict["level"] = level
    gamedict["livesleft"] = livesleft
    gamedict["score"] = score
    gamedict["locationxy"] = locationxy

    mygame = Gamedatasaver()
    mygame.gamedatapickle(gamedict, gamesavefile, listlength)    
    mygame.gamedataunpickle(gamesavefile)
    mygame.printtest()




if __name__ == "__main__":
    main()

    
