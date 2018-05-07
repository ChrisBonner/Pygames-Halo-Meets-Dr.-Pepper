import sys, os


def Scores():
    try:
        ScoreArray = []
        ReadScores = open ("HighScores.zt","r")
        #read line into array
        for line in ReadScores.readlines():
        # loop over the elemets, split by whitespace
            for i in line.split():
        # append to the list
                ScoreArray.append(i)
        #close file
        ReadScores.close()
        
        return ScoreArray
    except:
        sys.exit("could not load High Score file to Read :-(")
    
def Names():
    try:
        NameArray = []
        ReadName = open ("Names.zt","r")
        #read line into array
        for line in ReadName.readlines():
        # loop over the elemets, split by whitespace
            for i in line.split():
        # append to the list
                NameArray.append(i)
        #close file
        ReadName.close()
        
        return NameArray
    except:
        sys.exit("could not load Name Score file to Read :-(")
def WriteScores(HighScoreNew):
    str(HighScoreNew)
    try:
        WriteScores = open ("HighScores.zt","w")
        for Score in HighScoreNew:
            WriteScores.write(Score + "\n")
        WriteScores.close() 
    except:
        sys.exit("could not load High Score file to Write :-(")
    
def WriteNames(NameScore):
    str(NameScore)
    try:
        WriteName = open ("Names.zt","w")
        for Name in NameScore:
            WriteName.write(Name + "\n")
        WriteName.close()
    except:
        sys.exit("could not load Name Score file to Write :-(")

if __name__ == "__main__":
    ReadFile()