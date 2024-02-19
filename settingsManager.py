class SettingsManager(object):
    def __init__(self,main):
        self.__main = main
        self.__resList = ["default",(1000,1000),(1400,1150),(1920,1080),"fullscreen"]
        self.__schemeList = [("brown",((49,10,11),(224,163,135),(185,106,89),(116,58,54)))
                             ,("blue",((1,31,75),(3,57,108),(0,91,150),(179,205,224)))
                            ]
        self.__currentRes = 0
        self.__currentScheme = 0
        
    def getResList(self):
        return self.__resList
    
    def getSchemeList(self):
        return self.__schemeList
    
    def getCurrentRes(self):
        return self.__currentRes
    
    def getCurrentScheme(self):
        return self.__currentScheme
    
    def changeRes(self,newResDirection):
        newres = self.__currentRes+newResDirection
        newCurrentRes = newres%len(self.__resList)
        self.__main.gameEnvironment.setGameWindowSize(self.__resList[newCurrentRes])
        self.__currentRes = newCurrentRes
        
    def changeColorScheme(self,newSchemeDirection):
        '''
        self.__colorBgDark = colors[0]
        self.__colorBgMid = colors[1]
        self.__colorBgBright = colors[2]
        self.__colorFontMid = colors[3]
        '''
        newscheme = self.__currentScheme+newSchemeDirection
        newCurrentScheme = newscheme%len(self.__schemeList)
        self.__main.menuCreator.changeColors(self.__schemeList[newCurrentScheme][1])
        self.__currentScheme = newCurrentScheme
