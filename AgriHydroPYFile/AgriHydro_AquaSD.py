# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:58:18 2018
Main program
@author: Philip
"""
import os 
os.chdir(r"F:\AgriHydroNew\AgriHydroPYFile")
from AquaCrop_FileOperator import AquaCrop_Weather, AquaCrop_Project, AquaCrop_PRMday, D2tenday, TendayIndex
import pandas as pd
import subprocess
#os.chdir(r"C:\Users\Philip\Documents\GitHub\AgriHydro")

def WthNameSplit(WthName,FileExtension = True):
    if FileExtension: WthName = WthName.split(".")[0]
    GCM = WthName.split(sep="_")[0]
    RCP = WthName.split(sep="_")[1]
    FuturePeriod = int(WthName.split(sep="_")[2]) # 2021 2041 2061 2081
    Stno = WthName.split(sep="_")[3]
    return GCM,RCP,FuturePeriod,Stno

def StationInfo(StationID, path = None):
    if path is None:
        path = r"C:\Users\Philip\Documents\GitHub\AgriHydro\AgriHydroCommonWthData/Station_Info.xlsx"
    try:
        d = pd.read_excel(path)
        d = d[d["StationID"]==StationID]
        d = d.reset_index()[list(d)]
        print(d)
        return d
    except IOError:
        #WarnSound()
        print("Cannot open the file at: ",path)
        
def AgriHydro_WthDict(WthFileList, CSVDataPath, LeapYear = True, WthDataYears=20):
    # WthFile Format: Stn0_GCM_rcp_period_run.csv
    WthDict = {}
    for WthFile in WthFileList:
        WthData = pd.read_csv(CSVDataPath+"/"+WthFile,parse_dates = ["Date"],index_col=["Date"])
        GCM,RCP,FuturePeriod,Stno = WthNameSplit(WthFile) # WthFile: "C0C590_GCM_rcp_2021.csv"
        rng = pd.date_range(pd.datetime(FuturePeriod,1,1),pd.datetime(FuturePeriod+WthDataYears-1,12,31))
        if LeapYear is not True: 
            df = pd.DataFrame({"Date":rng}); df = df.set_index("Date")
            df = df[~((df.index.month == 2) & (df.index.day == 29))]
            rng = pd.DatetimeIndex(df.index)
        WthData.index = rng
        WthDict[WthFile[:-4]] = WthData
    return WthDict

def AgriHydro_WthForAqua(NoRainfall, WthDict, AquaCropInputDataPath, StationInfoPath, LeapYear = True, AddTail = False):
    # Demand water
    # Stations & 3 periods
    # AquaInput Weather 
    DaysIn20yr = 7305
    if LeapYear is not True: 
        DaysIn20yr = 7300
    for WthDataName in WthDict.keys():
        GCM,RCP,FuturePeriod, Stno = WthNameSplit(WthDataName, FileExtension = False)
        if NoRainfall:
            Rainfile = "Zero"+str(FuturePeriod)+".PLU" # Calculate Crop Water Demand not consider effective rainfall
            rain = "NoRain" # Calculate Crop Water Demand not consider effective rainfall
        else:
            Rainfile = None
            rain = "Rain"
        WthData = WthDict.get(WthDataName).copy()
        Runs = int( (WthData.index.year[-1] - WthData.index.year[0] + 1)/20 ) # 20 years as a run
        StnoInfo = StationInfo(Stno,path = StationInfoPath)
        if RCP == "Baseline": RCP = "MaunaLoa"
        for run in range(Runs):
            Wthfile = WthData.copy().iloc[DaysIn20yr*run:DaysIn20yr*(run+1),:]
            if AddTail:
                Wthfile = pd.concat([Wthfile,Wthfile])
                print("add tail")
            if Wthfile.isnull().values.any(): print("Error number in WthData!")
            # Wthfilename Format: Stn0_GCM_rcp_period_run
            Wthfilename = rain+"_"+WthDataName + "_" + str(run+1)
            AquaCrop_Weather(AquaCropInputDataPath+"/"+Wthfilename, Wthfile, RainFile = Rainfile, Type = 1, Record1stD = 1, Record1stM = 1, Record1stY = FuturePeriod, Description = Wthfilename, CO2Filename = RCP+".CO2", AquaVersion = 6.1, lat = StnoInfo.loc[0,"lat"], dz_m = 0)
    print("Wth for Aquacrop done!.")
    return None
       
# AquaInput PRM for successive 20yr Crop Water Demand
# Soil => Stno => Crop => Runs => Years(20) => Planting Time(3)
def AgriHydro_PRMForAqua(NoRainfall, AquaPRMPath, AquaCropInputDataPath, WthDict,CropFile,CropsRatio,StnoField,ManFile,IrrFile,SW0File,SoilType = ["CYClayLoam.SOL"],GrowPeriod = ["G1","G2"]):  
    # 還沒考慮 soil type，不要考慮了QQ 太多
    for soil in SoilType:
        for WthDataName in WthDict.keys():
            WthData = WthDict.get(WthDataName).copy()
            GCM,RCP,FuturePeriod,Stno = WthNameSplit(WthDataName, FileExtension = False)
            Runs = int( (WthData.index.year[-1] - WthData.index.year[0] + 1)/20 ) # 20 years as a run
            Field = StnoField[Stno]
            if NoRainfall:
                Rainfile = "Zero"+str(FuturePeriod)+".PLU" # Calculate Crop Water Demand not consider effective rainfall
                rain = "NoRain"
            else:
                Rainfile = None
                rain = "Rain"
            for run in range(Runs):
                Wthfilename = WthDataName + "_" + str(run+1)
                for y in range(20):                    
                    for g in GrowPeriod:
                        for crop in CropsRatio[Field][g].keys():
                            # 要再新增選項
                            if g == "G1" :
                                if "Rice" in crop:
                                    PlantingTime = ["-3-1","-3-11","-3-21"]
                                    LastSimTime  = ["-7-5","-7-15","-7-25"]
                            elif g == "G2" :
                                if "Rice" in crop:
                                    PlantingTime = ["-7-25","-8-5","-8-15"]
                                    LastSimTime  = ["-11-21","-12-01","-12-10"]
                            for t in range(len(PlantingTime)):
                                ProDict = {"FirstSimDate":pd.to_datetime(str(FuturePeriod+y)+PlantingTime[t]),
                                           "LastSimDate":pd.to_datetime(str(FuturePeriod+y)+LastSimTime[t]),
                                           "FirstCropDate":pd.to_datetime(str(FuturePeriod+y)+PlantingTime[t]),
                                           "LastCropDate":pd.to_datetime(str(FuturePeriod+y)+LastSimTime[t]),
                                           "Weather":rain +"_"+Wthfilename,
                                           "CO2":RCP+".CO2",
                                           "CRO":CropFile.get(crop),
                                           "IRR":IrrFile.get(crop),
                                           "MAN":ManFile.get(crop),
                                           "SOL":soil,
                                           "SW0":SW0File.get(crop)}
                                if RCP == "Baseline": ProDict["CO2"] = "MaunaLoa.CO2"
                                
                                PRMfilename = rain+"_"+WthDataName + "_" + str(run+1) + "_" + "y" + str(y+1) + "_" + crop + "_" + g + "_" + "P" + str(t+1) + ".PRM"
                                AquaCrop_Project(AquaPRMPath+"/"+PRMfilename,ProDict,datapath = AquaCropInputDataPath,RainFile = Rainfile, Description = PRMfilename,AquaVersion = 6.1,SuccessYearNum = 1)
    print("Finish PRM files.")
    return None

#AgriHydro_PRMForAqua(WthDict,CropFile,CropRatio,SoilType = ["CYClayLoam.SOL"],GrowPeriod = 1)

# Run AquaSim
def AgriHydro_RunAqua(AquaCropPluginEXE,ScenarioPath,AquaPRMPath): 
    l = os.listdir(AquaPRMPath)
    AquaWaitListPath = ScenarioPath + "/AquaCropPlugin_v6/WaitList"
    AquaDoneListPath = ScenarioPath + "/AquaCropPlugin_v6/DoneList"
    AquaErrPath = ScenarioPath + "/AquaCropPlugin_v6/ErrList"
    if not os.path.exists(AquaWaitListPath): os.makedirs(AquaWaitListPath)
    if not os.path.exists(AquaDoneListPath): os.makedirs(AquaDoneListPath)
    if not os.path.exists(AquaErrPath): os.makedirs(AquaErrPath)
    # 先以100為主去跑，不行再換一個一個過濾錯誤檔
    for file in l:
        os.rename(AquaPRMPath+"/"+file, AquaWaitListPath+"/"+file)
    print("Move files to WaitList folder!")
    print("Runing AquaCrop......")
    for i in range(int(len(l)/100)+1):
        if i == int(len(l)/100):
            l2 = l[100*i:]
        else:
            l2 = l[100*i:100*(i+1)]
                
        for file in l2:
            os.rename(AquaWaitListPath+"/"+file, AquaPRMPath+"/"+file)
        try:
            subprocess.run(AquaCropPluginEXE, timeout=360)
            for file in l2:
                os.rename(AquaPRMPath+"/"+file, AquaDoneListPath+"/"+file)
        except subprocess.TimeoutExpired:
            print("Try to find err file.")
            err100 = os.listdir(AquaPRMPath)
            for file in err100:
                os.rename(AquaPRMPath+"/"+file, AquaWaitListPath+"/"+file)
            for file in err100:
                os.rename(AquaWaitListPath+"/"+file, AquaPRMPath+"/"+file)
                try:        
                    subprocess.run(AquaCropPluginEXE, timeout=5)
                    os.rename(AquaPRMPath+"/"+file, AquaDoneListPath+"/"+file)
                except subprocess.TimeoutExpired:
                    print(file)
                    os.rename(AquaPRMPath+"/"+file, AquaErrPath+"/"+file)          
    print("AquaCrop Sim Done!.")
    return None


#def AgriHydro_RunAqua(AquaCropPluginEXE,ScenarioPath,AquaPRMPath): 
#    l = os.listdir(AquaPRMPath)
#    AquaWaitListPath = ScenarioPath + "/AquaCropPlugin_v6/WaitList"
#    AquaDoneListPath = ScenarioPath + "/AquaCropPlugin_v6/DoneList"
#    if not os.path.exists(AquaWaitListPath): os.makedirs(AquaWaitListPath)
#    if not os.path.exists(AquaDoneListPath): os.makedirs(AquaDoneListPath)
#    for file in l:
#        os.rename(AquaPRMPath+"/"+file, AquaWaitListPath+"/"+file)
#    print("Move files to WaitList folder!")
#    print("Runing AquaCrop......")
#    for i in range(int(len(l)/100)+1):
#        if i == int(len(l)/100):
#            l2 = l[100*i:]
#        else:
#            l2 = l[100*i:100*(i+1)]
#        for file in l2:
#            os.rename(AquaWaitListPath+"/"+file, AquaPRMPath+"/"+file)
#        subprocess.call(AquaCropPluginEXE)
#        for file in l2:
#            os.rename(AquaPRMPath+"/"+file, AquaDoneListPath+"/"+file)
#    print("AquaCrop Sim Done!.")
#    return None
#%% Calculate Irrigation plan for Shimen Reservoir per GCM RCP Period Run Year
def Aqua_ReadInputData(filename):
    if filename.split(".")[-1] == "csv":
        df = pd.read_csv(filename,engine = "python")
        df.columns = [ item.strip() for item in list(df)]
    if filename.split(".")[-1] == "xlsx":
        df = pd.read_excel(filename)
    return df
def Aqua_CreateSDAgriDemandFile(Blank_df_TendayIndex, Replace_df, ReplaceCol, FileTendayCol = "Ten-days"):
    AgriBlank = Blank_df_TendayIndex.copy()
    AgriBlank.loc[list(Replace_df[FileTendayCol]),ReplaceCol] = list(Replace_df[ReplaceCol])
    return AgriBlank


def Aqua_FormAgriWaterPlan(GCMs,RCPs,Periods,TotalRuns,AquaPRMOUTPath, CropField, CropsRatio, FieldArea, Stnos, PlantingDateRatio, PreGrowingWaterDemand, AgriWaterSourceRatio, SDWaterPlanBlankFile, SDAgriWaterDemandPath, WaterLossRate):
    Err = []
    PRMdayFileList = [d for d in os.listdir(AquaPRMOUTPath) if "PRMday" in d]
    PRMFutureFileList = [d for d in PRMdayFileList if GCMs and RCPs and str(Periods) in d]
    PRMFutureFileList = [d for d in PRMFutureFileList if "NoRain" == d.split("_")[0]]
    for run in range(TotalRuns):
        PRMRunFileList = [d for d in PRMFutureFileList if str(run+1) == d.split("_")[5]]
        for y in range(20):
            IrrSystemDict = {} # Irr water demand of each irrigation channel known as ["T","S"] in this case
            for region in ["T","S"]:
                StnosArea = [CropField.get(k) for k in CropField.keys() if region in k]
                StnosArea = list(set(Stnos) & set(StnosArea))
                if region == "S": AgriDemandName = "Water Right ShiMen AgriChannel AgriWater"
                if region == "T": AgriDemandName = "Water Right TaoYuan AgriChannel AgriWater"        
                PRMyFileList = [d for d in PRMRunFileList if "y"+str(y+1) == d.split("_")[6]]
                if StnosArea == []: continue
                df10_Reservoir = pd.DataFrame()
                for s in StnosArea:
                    PRMStnoFileList = [d for d in PRMyFileList if s == d.split("_")[4]]
                    Field = list(CropField.keys())[list(CropField.values()).index(s)]
                    Area = FieldArea.get(Field)*10000 #(m2)
                    Efficiency = 1 - WaterLossRate.get(Field)
                    if Field is None: 
                        print("Cannot find the field code for Stno: "+s+".");break
                    if Area is None: 
                        print("Cannot find the Area of field code: "+Field+".");break
                    if Efficiency is None: 
                        print("Cannot find the WaterLossRate of field code: "+Field+".");break  
                    for G in ["G1","G2"]:
                        PRMGFileList = [d for d in PRMStnoFileList if G == d.split("_")[8]]
                        df10_Crop = pd.DataFrame()             
                        for crop in CropsRatio[Field][G].keys():
                            CropAreaRatio = CropsRatio[Field][G].get(crop)
                            PRMCropFileList = [d for d in PRMGFileList if crop == d.split("_")[7]]
                            
                            if len(PRMCropFileList) != 3: 
                                print("The number of files is out of expectation(3).");
                                print(PRMCropFileList);
                                print(str(run+1)+"_"+"y"+str(y+1)+region+"_"+s+"_"+G+"_"+crop)
                                break
                            df10_planting = pd.DataFrame()
                            for file in PRMCropFileList:
                                PlantingRatio = PlantingDateRatio[file.split("_")[-1][0:2]]
                                df = AquaCrop_PRMday(AquaPRMOUTPath+"/"+file, Covert2DatetimeIndex = True, plot = False, plotvar = ["Surf","Rain","Irri","RO"])
                                if df["DAP"][0] == -9:
                                    Err.append(file); continue
                                df = df[df["DAP"]>0]
                                df = df.loc[:,["DAP","Irri"]]
                                df10 = D2tenday(df,True)
                                if df10.index.day[0] == 5:
                                    date = pd.datetime(df10.index.year[0],df10.index.month[0]-1,25)
                                else:
                                    date = pd.datetime(df10.index.year[0],df10.index.month[0],df10.index.day[0]-10)
                                IniDict = {"Date": [date], "DAP":[PreGrowingWaterDemand/10], "Irri":[PreGrowingWaterDemand/10]}
                                df_Ini = pd.DataFrame(IniDict,columns = IniDict.keys())
                                df_Ini = df_Ini.set_index("Date")
                                df10 = pd.concat([df_Ini,df10])["Irri"]*PlantingRatio # Different planting date 
                                df10_planting = pd.concat([df10_planting,df10],axis = 1)                               
                            df10_planting = df10_planting.fillna(0)
                            df10_planting = df10_planting.sum(axis = 1)
                            df10_planting = df10_planting/1000*Area/Efficiency*CropAreaRatio # (m3)
                            df10_planting.name = s+"_"+crop+"_"+" (m3)"
                            df10_Crop = pd.concat([df10_Crop,df10_planting],axis = 1)
                        df10_Crop = df10_Crop.sum(axis = 1)
                        df10_Crop.name = s
                        df10_Reservoir = pd.concat([df10_Reservoir,df10_Crop],axis = 1)
                df10_Reservoir = df10_Reservoir.sum(axis = 1)
                df10_Reservoir.name = AgriDemandName
                df10_Reservoir = df10_Reservoir.to_frame(AgriDemandName)
                df10_Reservoir = df10_Reservoir*AgriWaterSourceRatio["Reservoir"]
                df10_Reservoir = TendayIndex(df10_Reservoir)
                df10_Reservoir = df10_Reservoir[df10_Reservoir[AgriDemandName] > 0]
                IrrSystemDict[AgriDemandName] = df10_Reservoir
                #AgriDemandFileName = region+"_"+GCMs+"_"+RCPs+"_"+str(Periods)+"_"+str(run+1)+"_"+"y"+str(y+1)+".csv"
                # Water Right TaoYuan AgriChannel AgriWater_GCM_RCP26_2021_1_y20.csv
            AgriBlank = Aqua_ReadInputData(SDWaterPlanBlankFile)
            AgriBlank = AgriBlank.set_index("Ten-days")
            for Irr in IrrSystemDict.keys():
                AgriBlank = Aqua_CreateSDAgriDemandFile(AgriBlank, IrrSystemDict[Irr], Irr, FileTendayCol = "Ten-days")
            AgriUpdated = AgriBlank 
            AgriDemandFileName = GCMs+"_"+RCPs+"_"+str(Periods)+"_"+str(run+1)+"_"+"y"+str(y+1)+".csv"
            AgriUpdated.to_csv(SDAgriWaterDemandPath+"/"+AgriDemandFileName)
        print("Finish Run "+str(run+1)+": "+GCMs+"_"+RCPs+"_"+str(Periods)+"_"+str(run+1))
    print("Finish: "+GCMs+"_"+RCPs+"_"+str(Periods)) 
    return None    
        #print("Start to combine into single 20yr AgriDemand file...")
        #AgriDemandFileList = [d for d in os.listdir(SDAgriWaterDemandPath) if GCMs+"_"+RCPs+"_"+str(Periods)+"_"+str(run+1) in d]



                        