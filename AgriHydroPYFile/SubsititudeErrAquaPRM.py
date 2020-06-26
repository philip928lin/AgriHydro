# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 12:07:11 2019

@author: Philip
"""

import os 
import subprocess
def SubstituteErrPRM(ScenarioPath):
    ErrPath = ScenarioPath +"/AquaCropPlugin_v6\ErrList"
    ErrList = os.listdir(ErrPath)
    DoneList = ScenarioPath +"/AquaCropPlugin_v6\DoneList"
    AquaList = ScenarioPath +"/AquaCropPlugin_v6\LIST"
    AquaCropPluginEXE = ScenarioPath + "/AquaCropPlugin_v6/ACsaV60.exe"
    def ReplaceErrPRM(fnew,f,DoneList,AquaList):
        f1 = open(DoneList+"/"+fnew,"r")
        Content = f1.read()
        f2 = open(AquaList+"/"+f,"w")
        f2.write(Content)
        f1.close()
        f2.close()
    
    for f in ErrList:
        Err = []
        Succ = False
        DiffYear = True
        fsplit = f.split("_")
        for i in range(10):
            count1 = int(fsplit[6])
            if count1 != 1:
                fsplit[6] = str(count1-1)
            else:
                count1 = 10
                fsplit[6] = str(count1)
            fnew = "_".join(fsplit)
            if fnew in ErrList:
                count1 += 1
            else:
                ReplaceErrPRM(fnew,f,DoneList,AquaList)
                Succ = True
                DiffYear = False
                break
        if DiffYear:
            fsplit = f.split("_")
            for i in range(20):
                count2 = int(fsplit[7][1])
                if count2 != 1:
                    fsplit[7] = "y"+str(count2-1)
                else:
                    count1 = 20
                    fsplit[7] = "y"+str(count2)
                fnew = "_".join(fsplit)
                if fnew in ErrList:
                    count2 += 1
                else:
                    ReplaceErrPRM(fnew,f,DoneList,AquaList)
                    Succ = True
                    break
        if Succ:
            print("Succ! "+f+"\n\t->"+fnew)
        else:
            Err.append(f)
            print("Cannot substitute "+f)
    subprocess.run(AquaCropPluginEXE)
    


#AdaptPath = r"F:\AgriHydroNew\Adaptation"
#ScenList = os.listdir(AdaptPath)
#ScenList = [i for i in ScenList if "CCSM4_RCP26" in i]
#for scen in ScenList:
#    ScenarioPath = AdaptPath+"/"+scen
#    Err = {}
#    err = SubstituteErrPRM(ScenarioPath)
#    Err[scen] = err