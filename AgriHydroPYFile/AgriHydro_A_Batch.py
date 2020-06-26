# -*- coding: utf-8 -*-




def BatchRun(ScenarioPath, GCM, RCP, Period, RiceRatio, SoyRatio ):
    import os 
    os.chdir(r"F:\AgriHydroNew\AgriHydroPYFile")
    from AquaCrop_FileOperator import AquaCrop_IRR, AquaCrop_PRMday, AquaCrop_PRMseason
    from AgriHydro_AquaSD import AgriHydro_WthDict, AgriHydro_WthForAqua, AgriHydro_PRMForAqua, AgriHydro_RunAqua, Aqua_FormAgriWaterPlan, AquaCrop_Project
    from SDmodel_1yrSim import SD_ReadVensim, SD_Sim1yr, SD_DailyRatio
    from SubsititudeErrAquaPRM import SubstituteErrPRM
    import pandas as pd
    import numpy as np
    os.chdir(ScenarioPath)
    # Path
    ## Forming AquaCrop Files ##
    # CSVDataPath can be set to the common folder for all workspace
    #CSVDataPath = ScenarioPath + "/DATA"
    CommonPath = r"F:\AgriHydroNew"
    
    CSVDataPath = CommonPath+"/AgriHydroCommonWthData"
    StationInfoPath = CSVDataPath+"/Station_Info.xlsx"
    AquaCropInputDataPath = ScenarioPath + "/AquaCropPlugin_v6/DATA"
    AquaPRMPath = ScenarioPath + "/AquaCropPlugin_v6/LIST"
    AquaPRMOUTPath = ScenarioPath + "/AquaCropPlugin_v6/OUTP"
    SDWaterPlanBlankPath = ScenarioPath + "/DATA_SD/Blank"
    SDAgriWaterDemandPath = ScenarioPath + "/DATA_SD/AgriDemand"
    AquaCropPluginEXE = ScenarioPath + "/AquaCropPlugin_v6/ACsaV60.exe"
    SDWaterPlanBlankFile = SDWaterPlanBlankPath + "/Data_allocation_2012_Agri.xlsx"
    # SDModel
    VensimPath = ScenarioPath + "/DATA_SD"
    SDPublicDemandPath = ScenarioPath + "/DATA_SD/PublicDemand"
    SDAgriDemandPath = ScenarioPath + "/DATA_SD/AgriDemand"
    # SDInflowPath can be set to the common folder for all workspace
    #SDInflowPath = ScenarioPath + "/DATA_SD\SDInflow"
    SDInflowPath = CommonPath+r"/AgriHydroCommonSDInflowData"
    SDOutPath = ScenarioPath + "/OUT_SD"
    AggreOutPath = ScenarioPath + "/OUT_Aggre"
    
    # Background Scenario Setting
    GCMs = GCM
    RCPs = RCP
    Periods = Period
    
    # Simulation Setting
    WthDataYears = 200
    LeapYear = False
    TotalRuns = 10
    PreGrowingWaterDemand = 180  # (mm)
    # Adaptation Setting
    CropField = {"T1":"C0C540","T2":"C0C590","T3":"C1C510-1",
                 "S1":"C0C630","S2":"C0C650","S3":"C1C510-2"} 
    StnoField = {"C0C540":"T1","C0C590":"T2","C1C510-1":"T3",
                 "C0C630":"S1","C0C650":"S2","C1C510-2":"S3"} 
    # 資料來源：桃園農田水利會2005年灌溉計畫書, Total = 34682
    # 更新成107年
    FieldArea = {"T1":5942,"T2":7971,"T3":7159,
                 "S1":2385,"S2":6013,"S3":3808}     #(ha)
    WaterLossRate = {"T1":0.17,"T2":0.17,"T3":0.17,
                     "S1":0.16,"S2":0.16,"S3":0.16}
    #CropsRatio = {"G1":{"Rice1":1},"G2":{"Rice1":1}} #,"Soybean":0.5
    aRice = RiceRatio
    aSoy = SoyRatio
    ## A
    CropsRatio = {"T1":{"G1":{"Rice1":aRice,"Soybean":aSoy},"G2":{"Rice1":1}}, #"Rice1":0.5,"Soybean":0.5
                 "T2":{"G1":{"Rice1":aRice,"Soybean":aSoy},"G2":{"Rice1":1}},
                 "T3":{"G1":{"Rice1":aRice,"Soybean":aSoy},"G2":{"Rice1":1}},
                 "S1":{"G1":{"Rice1":1},"G2":{"Rice1":1}},
                 "S2":{"G1":{"Rice1":aRice,"Soybean":aSoy},"G2":{"Rice1":1}},
                 "S3":{"G1":{"Rice1":1},"G2":{"Rice1":1}}}
    ## B
#    CropsRatio = {"T1":{"G1":{"Rice1":1},"G2":{"Rice1":aRice,"Soybean":aSoy}}, #"Rice1":0.5,"Soybean":0.5
#                 "T2":{"G1":{"Rice1":1},"G2":{"Rice1":aRice,"Soybean":aSoy}},
#                 "T3":{"G1":{"Rice1":1},"G2":{"Rice1":aRice,"Soybean":aSoy}},
#                 "S1":{"G1":{"Rice1":1},"G2":{"Rice1":1}},
#                 "S2":{"G1":{"Rice1":1},"G2":{"Rice1":aRice,"Soybean":aSoy}},
#                 "S3":{"G1":{"Rice1":1},"G2":{"Rice1":1}}}
    GrowPeriod = ["G1","G2"]
    Stnos = ["C0C540","C0C590","C1C510-1","C0C630","C0C650","C1C510-2"] # Stations that are used in Input data
    PlantingDateRatio = {"P1":1/3,"P2":1/3,"P3":1/3} # Sep into three periods
    AgriWaterSourceRatio = {"Reservoir": 0.549,"EffRainfall":0.172,"Other":0.279}
    # AquaCrop Files
    WthFileList = [GCMs+"_"+RCPs+"_"+str(Periods)+"_"+s+".csv" for s in Stnos]  #["GCM_RCP26_2021_C0C590.csv"]
    CropFile = {"Rice1":"New1RiceGDD_v5.CRO","Rice2":"New1RiceGDD_v5_2.CRO","Soybean":"CYSoybeanGDD_v6.CRO"}  # Root 0.05m - 0.3m
    IrrFile = {"Rice1":"CYRice1_v2.IRR","Rice2":"CYRice1_v2.IRR","Soybean":"SoyGen50.IRR"}
    ManFile = {"Rice1":"CYBund10.MAN","Rice2":"CYBund10.MAN","Soybean":"SoybeanNone.MAN"}
    SW0File = {"Rice1":"CYClayLoam.SW0","Rice2":"CYClayLoam.SW0","Soybean":"CYClayLoamSoyFC.SW0"}
    
    # SDModel
    # Setting
    SocEcoList = ["PublicShort-H","PublicShort-L"]  #,"Public2018"
    SDLevelComponents = ["ShiMen Reservoir","ShiMen WPP Storage Pool", "ZhongZhuang Adjustment Reservoir"]
    SDOutputVar = ['Date', 'ShiMen Reservoir', 'ShiMen Reservoir Depth',"Transfer From BanXinWPP To NorthTaoYuanWaterDemand"]
    SDmodel = SD_ReadVensim(VensimPath+"/"+"TaoYuanSystem_SDLab_NoLossRate.mdl", AutoSelect = True)
    
    # AquaInput = Irrigation
    IrrData = pd.read_csv(CSVDataPath+"/"+"IRRRice1CY_v2.csv")
    #IrrData.plot()
    AquaCrop_IRR(AquaCropInputDataPath+"/"+"CYRice1_v2.IRR", IrrData, CropType = "Rice", Planing = True, AquaVersion = 6.1)
    
    WthDict = AgriHydro_WthDict(WthFileList, CSVDataPath, LeapYear = LeapYear, WthDataYears=WthDataYears)
    
    NoRainfall = True
    AgriHydro_WthForAqua(NoRainfall, WthDict, AquaCropInputDataPath, StationInfoPath = StationInfoPath, LeapYear = LeapYear,AddTail = True)
    AgriHydro_PRMForAqua(NoRainfall, AquaPRMPath, AquaCropInputDataPath, WthDict,CropFile,CropsRatio,StnoField,ManFile,IrrFile,SW0File,SoilType = ["CYClayLoam.SOL"],GrowPeriod = GrowPeriod)
    NoRainfall = False
    AgriHydro_WthForAqua(NoRainfall, WthDict, AquaCropInputDataPath, StationInfoPath = StationInfoPath, LeapYear = LeapYear,AddTail = True)
    AgriHydro_PRMForAqua(NoRainfall, AquaPRMPath, AquaCropInputDataPath, WthDict,CropFile,CropsRatio,StnoField,ManFile,IrrFile,SW0File,SoilType = ["CYClayLoam.SOL"],GrowPeriod = GrowPeriod)
    AgriHydro_RunAqua(AquaCropPluginEXE,ScenarioPath,AquaPRMPath)
    SubstituteErrPRM(ScenarioPath)
    Aqua_FormAgriWaterPlan(GCMs,RCPs,Periods,TotalRuns,AquaPRMOUTPath, CropField, CropsRatio, FieldArea, Stnos, PlantingDateRatio, PreGrowingWaterDemand, AgriWaterSourceRatio, SDWaterPlanBlankFile, SDAgriWaterDemandPath, WaterLossRate)
    
    #%% SDmodel
    
    # Run SD model to extract how many water can be extracted
    for SocEco in SocEcoList:
        SDInitial = {'ShiMen Reservoir':205588000,
                 'ZhongZhuang Adjustment Reservoir':5050000,
                 'ShiMen WPP Storage Pool':500000}
        SI_SocEco = pd.DataFrame()
        for r in range(TotalRuns):
            SI20yr = []
            for y in range(20):
                # Public demand
                ListofFile = [SDPublicDemandPath+"/"+SocEco+".xlsx"]
                # Inflow data
                
                ListofFile.append(SDInflowPath+"/"+GCMs+"_"+RCPs+"_"+str(Periods)+"_"+str(r+1)+"_y"+str(y+1)+".csv") #y+1
                # AgriDemand data
                ListofFile.append(SDAgriDemandPath+"/"+GCMs+"_"+RCPs+"_"+str(Periods)+"_"+str(r+1)+"_y"+str(y+1)+".csv") 
                SDResult_1yr = SD_Sim1yr(SDmodel, SDInitial, SDLevelComponents, SDOutputVar, ListofFile, Tenday2Day = True, FileDir = None, SDDecisionTimePoint = None)
                SDResult_1yr.to_csv(SDOutPath+"/"+"SDResult_"+SocEco+"_"+GCMs+"_"+RCPs+"_"+str(Periods)+"_"+str(r+1)+"_y"+str(y+1)+".csv")
                ActualRatio, SI = SD_DailyRatio(SDResult_1yr)
                ActualRatio.to_csv(SDOutPath+"/"+"AgriRatio_"+SocEco+"_"+GCMs+"_"+RCPs+"_"+str(Periods)+"_"+str(r+1)+"_y"+str(y+1)+".csv")
                SI20yr.append(SI)
            SI20yr = pd.Series(np.mean(np.array(SI20yr),axis = 0))
            SI20yr.name = r+1
            SI_SocEco = pd.concat([SI_SocEco,SI20yr],axis = 1)
        SI_SocEco = SI_SocEco.T
        SI_SocEco.to_csv(AggreOutPath+"/"+"SI_"+SocEco+"_"+GCMs+"_"+RCPs+"_"+str(Periods)+".csv")
    
    #%%
    # generate new Irr
    def UpdateIrrValue(OrgIrri,SDAgriRatio,AddDays,FromReservoirRatio,region,ReservoirIrrRatio):
        OrgIrri = OrgIrri.copy()
        OrgIrri = OrgIrri.reset_index()
        SDAgriRatio = SDAgriRatio.copy()
        if "T" in region: name = "TaoyuanIrrRatio"
        if "S" in region: name = "ShimenIrrRatio"
        NewIrri = []
        for i in range(OrgIrri.shape[0]):
            
            sdRatio = SDAgriRatio.loc[OrgIrri.loc[i,"DAP"]+AddDays-1,name]
            if np.isnan(sdRatio):
                sdRatio = 1
            IrrFromRes = OrgIrri.loc[i,"Irri"]*FromReservoirRatio*sdRatio*ReservoirIrrRatio
            NewIrri.append(OrgIrri.loc[i,"Irri"]*(1-FromReservoirRatio) + IrrFromRes)
            print(SDAgriRatio.loc[OrgIrri.loc[i,"DAP"]+AddDays-1,name])
        OrgIrri["NewIrri"] =  NewIrri
        return OrgIrri
    
    import pandas as pd
    for SocEco in SocEcoList:
        for s in Stnos:
            region = StnoField[s]
            if "T" in region: AgriIrrRegion = "TaoyuanIrrRatio"
            elif "S" in region: AgriIrrRegion = "ShimenIrrRatio"
            for r in range(TotalRuns):
                for y in range(20):
                    for g in GrowPeriod:
                        for crop in CropsRatio[region][g].keys():
                            # 未加Ccrop
                            if g == "G1":
                                GDay = {"P1":60,"P2":70,"P3":80} # ["-3-1","-3-11","-3-21"]
                                PlantingTime = {"P1":"-3-1","P2":"-3-11","P3":"-3-21"}
                                LastSimTime  = {"P1":"-7-5","P2":"-7-15","P3":"-7-25"}
                            elif g == "G2":
                                GDay = {"P1":206,"P2":217,"P3":227} # ["-7-25","-8-5","-8-15"]
                                PlantingTime = {"P1":"-7-25","P2":"-8-5","P3":"-8-15"}
                                LastSimTime  = {"P1":"-11-21","P2":"-12-01","P3":"-12-10"}
                            for p in ["P1","P2","P3"]:
                                IrrReal = pd.DataFrame()
                                filename = GCMs+"_"+RCPs+"_"+str(Periods)+"_"+s+"_"+str(r+1)+"_y"+str(y+1)+"_"+crop+"_"+g+"_"+p
                                PRMfilename = "Rain_"+filename+"PRMday.OUT"
                                ReservoirRatioName = "AgriRatio_"+SocEco+"_"+GCMs+"_"+RCPs+"_"+str(Periods)+"_"+str(r+1)+"_y"+str(y+1)+".csv"
                                RainOut = AquaCrop_PRMday(AquaPRMOUTPath+"/"+PRMfilename, Covert2DatetimeIndex = True, plot = False, plotvar = ["Surf","Rain","Irri","RO"])
                                RainOut = RainOut[RainOut["DAP"]>0]
                                RainOut = RainOut[RainOut["Irri"]>0]
                                SDAgriRatio = pd.read_csv(SDOutPath+"/"+ReservoirRatioName)
                                AgriIni = SDAgriRatio.loc[GDay[p]-1,AgriIrrRegion]
                                OrgIrri = RainOut[["DAP","Irri"]]
                                IrrRain = AquaCrop_PRMseason(AquaPRMOUTPath+"/"+"Rain_"+filename+"PRMseason.OUT", Sumvar = ["YearN","Yield","Irri"]).loc[0,"Irri"]
                                IrrNoRain = AquaCrop_PRMseason(AquaPRMOUTPath+"/"+"NoRain_"+filename+"PRMseason.OUT", Sumvar = ["YearN","Yield","Irri"]).loc[0,"Irri"]
                                ReservoirIrrRatio = min(IrrNoRain*AgriWaterSourceRatio["Reservoir"]/IrrRain,1)
                                if "Rice" in crop: FromReservoirRatio = 1 #記得分母要換，先假設所有水都從水庫來(其他來源變動跟水庫一樣)，一致性要維持跟前面一樣或不一定
                                else: FromReservoirRatio = 0.5
                                OrgIrri = UpdateIrrValue(OrgIrri,SDAgriRatio, GDay[p],FromReservoirRatio,region,ReservoirIrrRatio)
                                IrrReal["Day"] = list(OrgIrri["DAP"])
                                IrrReal["Depth (mm)"] = list(OrgIrri["NewIrri"])
                                #IrrReal["ECw (dS/m)"] Autofill in with 0 
                                IRRName = SocEco+"_"+GCMs+"_"+RCPs+"_"+str(Periods)+"_"+s+"_"+str(r+1)+"_y"+str(y+1)+"_"+crop+"_"+g+"_"+p+".IRR"
                                # Create IRR file for actual run
                                AquaCrop_IRR(AquaCropInputDataPath+"/"+IRRName, IrrReal, CropType = "Rice", Planing = False, AquaVersion = 6.1)
                                
                                #Choose SWO based on AgriIni 
                                if AgriIni >= 0.90: 
                                    if "Rice" in crop: SW0 = "CYClayLoam.SW0"  # Rice 
                                    else: SW0 = "CYClayLoamSoyFC.SW0"   # dry farm
                                elif AgriIni >= 0.70 and AgriIni < 0.90: SW0 = "CYClayLoam09.SW0" #0.75
                                elif AgriIni >= 0.4 and AgriIni < 0.70: SW0 = "CYClayLoam06.SW0"#0.5
                                elif AgriIni < 0.4: SW0 = "CYClayLoam00.SW0" #0
                                # Create Actual PRM
                                WthDataName = GCMs+"_"+RCPs+"_"+str(Periods)+"_"+s+"_"+str(r+1)
                                ProDict = {"FirstSimDate":pd.to_datetime(str(Periods+y)+PlantingTime[p]),
                                           "LastSimDate":pd.to_datetime(str(Periods+y)+LastSimTime[p]),
                                           "FirstCropDate":pd.to_datetime(str(Periods+y)+PlantingTime[p]),
                                           "LastCropDate":pd.to_datetime(str(Periods+y)+LastSimTime[p]),
                                           "Weather":"Rain_"+WthDataName,
                                           "CO2":RCPs+".CO2",
                                           "CRO":CropFile.get(crop),
                                           "IRR":IRRName,
                                           "MAN":ManFile.get(crop),
                                           "SOL":"CYClayLoam.SOL", 
                                           "SW0": SW0}
                                if RCPs == "Baseline": ProDict["CO2"] = "MaunaLoa.CO2"
                                
                                PRMfilename = "Actual"+"_"+SocEco+"_"+WthDataName + "_" + "y" + str(y+1) + "_" + crop + "_" + g + "_" + p + ".PRM"
                                AquaCrop_Project(AquaPRMPath+"/"+PRMfilename,ProDict,datapath = AquaCropInputDataPath,RainFile = None, Description = PRMfilename,AquaVersion = 6.1,SuccessYearNum = 1)
    
    # Run AquaCrop again!
    AgriHydro_RunAqua(AquaCropPluginEXE,ScenarioPath,AquaPRMPath)
    SubstituteErrPRM(ScenarioPath)
    #%%
    def Aqua_SurfStress(ActualDepth,PlanDepth = "IRRRice1CY_v2_minDepth.csv",Ini_AgriRatio = 1):
        PlanDepth = pd.read_csv(CSVDataPath+"/"+PlanDepth)
        TotalLength = min(PlanDepth.shape[0],len(ActualDepth))
        ActualDepth = ActualDepth[0:TotalLength]
        BaseThreshold = 5 # (mm) if dific is < BaseThreshold don't count
        if Ini_AgriRatio >= 0.99: a = 0.86
        elif Ini_AgriRatio >= 0.75 and Ini_AgriRatio < 0.99: a = 0.75
        elif Ini_AgriRatio >= 0.5 and Ini_AgriRatio < 0.75: a = 0.65
        elif Ini_AgriRatio < 0.5: a = 0.6
        
        Count = np.array(ActualDepth) - np.array(PlanDepth["Depth"][0:TotalLength])
        Countn = max(len(Count[Count<-BaseThreshold]),0)
        Count = Count[Count<0]
        Count = Count[Count>=-BaseThreshold]
        #print(Count)
        BaseLegth = len(Count)
        DeficitPar =  a**(1/(TotalLength-BaseLegth))
        YieldPenaltySurf = DeficitPar**Countn
        return YieldPenaltySurf
    
    #df_compare = pd.DataFrame(columns=['SocEco','Stno','Run','yr','Crop','G','Area','Yield','Irri','GDay','Rainfall','AreaYield'])
    ResultALL = pd.DataFrame()
    for s in Stnos:
        region = StnoField[s]
        if "T" in region: AgriIrrRegion = "TaoyuanIrrRatio"
        elif "S" in region: AgriIrrRegion = "ShimenIrrRatio"
        for r in range(TotalRuns):
            for y in range(20):
                for g in GrowPeriod:
                    for crop in CropsRatio[region][g].keys():
                        Result1yr = pd.DataFrame()
                        # for extract AgriRatio Info
                        if g == "G1":
                            GDay = {"P1":60,"P2":70,"P3":80} # ["-3-1","-3-11","-3-21"]
                        elif g == "G2":
                            GDay = {"P1":206,"P2":217,"P3":227} # ["-7-25","-8-5","-8-15"]
                            
                        for p in ["P1","P2","P3"]:
                            for SocEco in ["Rain","NoRain"] + SocEcoList:
                                Day = False; SurfStress = 1; YieldPenaltySurf = 1
                                if SocEco == "Rain":
                                    filename = "Rain_"+GCMs+"_"+RCPs+"_"+str(Periods)+"_"+s+"_"+str(r+1)+"_y"+str(y+1)+"_"+crop+"_"+g+"_"+p+"PRMseason.OUT"
                                elif SocEco == "NoRain":
                                    filename = "NoRain_"+GCMs+"_"+RCPs+"_"+str(Periods)+"_"+s+"_"+str(r+1)+"_y"+str(y+1)+"_"+crop+"_"+g+"_"+p+"PRMseason.OUT"
                                else:
                                    #read AgriInitial 
                                    AgriIni = pd.read_csv(SDOutPath+"/"+"AgriRatio_"+SocEco+"_"+GCMs+"_"+RCPs+"_"+str(Periods)+"_"+str(r+1)+"_y"+str(y+1)+".csv").loc[GDay[p]-1,AgriIrrRegion]
                                    filename = "Actual_"+SocEco+"_"+GCMs+"_"+RCPs+"_"+str(Periods)+"_"+s+"_"+str(r+1)+"_y"+str(y+1)+"_"+crop+"_"+g+"_"+p+"PRMseason.OUT"
                                    filename_day = "Actual_"+SocEco+"_"+GCMs+"_"+RCPs+"_"+str(Periods)+"_"+s+"_"+str(r+1)+"_y"+str(y+1)+"_"+crop+"_"+g+"_"+p+"PRMday.OUT"
                                    Day = True
                                if Day:
                                    Result1yr_day = AquaCrop_PRMday(AquaPRMOUTPath+"/"+filename_day, Covert2DatetimeIndex = True, plot = False, plotvar = ["Surf","Rain","Irri","RO"])
                                    Result1yr_day = Result1yr_day[Result1yr_day["DAP"]>0]
                                    if "Rice" in crop:
                                        YieldPenaltySurf = Aqua_SurfStress(Result1yr_day["Surf"],PlanDepth = "IRRRice1CY_v2_minDepth.csv",Ini_AgriRatio = AgriIni)
                                Result1yr = AquaCrop_PRMseason(AquaPRMOUTPath+"/"+filename, Sumvar = ["YearN","Yield","Irri","Cycle","Rain","Runoff","Brelative"])
                                Result1yr["SocEco"] = SocEco
                                Result1yr["Stno"] = s 
                                Result1yr["Run"] = r+1
                                Result1yr["yr"] = y+1
                                Result1yr["Crop"] = crop
                                Result1yr["CropRatio"] = CropsRatio[region][g][crop]
                                Result1yr["G"] = g
                                Result1yr["P"] = p 
                                Result1yr["PlantRatio"] = PlantingDateRatio[p]
                                Result1yr["FieldArea"] = FieldArea[StnoField[s]]
                                Result1yr["YieldPenaltySurf"] = YieldPenaltySurf
                                ResultALL = pd.concat([ResultALL,Result1yr])
                        
    ResultALL.to_csv(AggreOutPath+"/"+"AgriResultAll"+"_"+GCMs+"_"+RCPs+"_"+str(Periods)+".csv",index = None)          
    
    #%%
    FinalResDf = ResultALL.copy()
    FinalResDf["ActualYield"] = FinalResDf["Yield"]*FinalResDf["CropRatio"]*FinalResDf["PlantRatio"]*FinalResDf["YieldPenaltySurf"]*FinalResDf["FieldArea"]
    
    #FinalResDf["Run"] = FinalResDf["Run"]+1
    #FinalResDf["yr"] = FinalResDf["yr"]+1
    DeficitRatioDf = pd.DataFrame()
    for SocEco in SocEcoList:
        for s in Stnos:
            region = StnoField[s]
            for r in range(TotalRuns):
                for y in range(20):
                    for g in GrowPeriod:
                        for crop in CropsRatio[region][g].keys():                    
                            ResDf = pd.concat([FinalResDf[FinalResDf["SocEco"] == SocEco],  FinalResDf[FinalResDf["SocEco"] ==  "Rain"]])
                            ResDf = ResDf[ResDf["Stno"] == s]
                            ResDf = ResDf[ResDf["Run"] == r+1]
                            ResDf = ResDf[ResDf["yr"] == y+1 ]
                            ResDf = ResDf[ResDf["Crop"] == crop]
                            ResDf = ResDf[ResDf["G"] == g].reset_index()
                            # for recording scenario setting
                            CalDf = ResDf.loc[0,["YearN","SocEco","Run","yr","Crop","Stno","G","FieldArea","CropRatio"]].to_frame().T
                            # Eliminate the unknown from AquaCrop simulation 
                            na = np.array([1,1,1])
                            for i, v in enumerate(ResDf[ResDf["SocEco"] == SocEco]["Cycle"]):
                                if v < 0: na[i] = 0
                            if sum(na) == 0: continue
                            ResDf_Potential = (ResDf[ResDf["SocEco"] == "Rain"]["ActualYield"]*na).sum()
                            ResDf_Actual = (ResDf[ResDf["SocEco"] == SocEco]["ActualYield"]*na).sum()
                            DeficitRatio = (ResDf_Actual-ResDf_Potential)/ ResDf_Potential 
                            CalDf["DeficitRatio"] = DeficitRatio
                            DeficitRatioDf = pd.concat([DeficitRatioDf,CalDf])
    DeficitRatioDf["DeficitRatio"] = DeficitRatioDf["DeficitRatio"]*DeficitRatioDf["CropRatio"]  
    DeficitRatioDf["FieldArea"] = DeficitRatioDf["FieldArea"]*DeficitRatioDf["CropRatio"]          
    DeficitRatioDf2 = DeficitRatioDf.groupby(["YearN","SocEco","Run","yr","Stno","G"]).sum().reset_index()
    DeficitRatioDf2.to_csv(AggreOutPath+"/"+"AgriDeficit"+"_"+GCMs+"_"+RCPs+"_"+str(Periods)+".csv",index = None)
