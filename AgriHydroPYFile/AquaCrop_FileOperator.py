# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 23:35:39 2018

@author: Philip
"""
import numpy as np
import pandas as pd
import julian
from dateutil.relativedelta import relativedelta
#import matplotlib.pyplot as plt
import os
#os.chdir(r"C:\Users\Philip\Documents\GitHub\AquaCrop\TestDataFile")
# Function
# ET0
def AquaCrop_ETo(filename, ET_mm, Type = 1, Record1stD = 1, Record1stM = 1, Record1stY = 1901, Description = None):
    f = open(filename, 'w')
    # 1st line
    if Description is None:
        f.write("First line is a description which is displayed when selecting the file" + '\n')
    else:
        f.write(Description + '\n')
    # 2nd line
    f.write('{:>6}'.format(str(Type))+"  : Daily records (1=daily, 2=10-daily and 3=monthly data)" + '\n')
    # 3rd line - 5th line
    f.write('{:>6}'.format(str(Record1stD))+"  : First day of record (1, 11 or 21 for 10-day or 1 for months)" + '\n')
    f.write('{:>6}'.format(str(Record1stM))+"  : First month of record" + '\n')
    f.write('{:>6}'.format(str(Record1stY))+"  : First year of record (1901 if not linked to a specific year)" + '\n')
    # 6rd line - 8th line
    f.write('\n'+"  Average ETo (mm/day)" + '\n')
    f.write("=======================" + '\n')
    for et in ET_mm:
        f.write(str(round(et,1)) + '\n')
    f.close()
    print("Done "+filename + " !")
# Precip
def AquaCrop_PLU(filename, P_mm, Type = 1, Record1stD = 1, Record1stM = 1, Record1stY = 1901, Description = None):
    f = open(filename, 'w')
    # 1st line
    if Description is None:
        f.write("First line is a description which is displayed when selecting the file" + '\n')
    else:
        f.write(Description + '\n')
    # 2nd line
    f.write('{:>6}'.format(str(Type))+"  : Daily records (1=daily, 2=10-daily and 3=monthly data)" + '\n')
    # 3rd line - 5th line
    f.write('{:>6}'.format(str(Record1stD))+"  : First day of record (1, 11 or 21 for 10-day or 1 for months)" + '\n')
    f.write('{:>6}'.format(str(Record1stM))+"  : First month of record" + '\n')
    f.write('{:>6}'.format(str(Record1stY))+"  : First year of record (1901 if not linked to a specific year)" + '\n')
    # 6rd line - 8th line
    f.write('\n'+"  Total Rain (mm)" + '\n')
    f.write("=======================" + '\n')
    for p in P_mm:
        f.write('{:>10}'.format(str(round(p,1))) + '\n')
    f.close()  
    print("Done "+filename + " !")
# Temp MinT MaxT 
# Precip
def AquaCrop_TMP(filename, Tmin, Tmax, Type = 1, Record1stD = 1, Record1stM = 1, Record1stY = 1901, Description = None):
    f = open(filename, 'w')
    # 1st line
    if Description is None:
        f.write("First line is a description which is displayed when selecting the file" + '\n')
    else:
        f.write(Description + '\n')
    # 2nd line
    f.write('{:>6}'.format(str(Type))+"  : Daily records (1=daily, 2=10-daily and 3=monthly data)" + '\n')
    # 3rd line - 5th line
    f.write('{:>6}'.format(str(Record1stD))+"  : First day of record (1, 11 or 21 for 10-day or 1 for months)" + '\n')
    f.write('{:>6}'.format(str(Record1stM))+"  : First month of record" + '\n')
    f.write('{:>6}'.format(str(Record1stY))+"  : First year of record (1901 if not linked to a specific year)" + '\n')
    # 6rd line - 8th line
    f.write('\n'+"  Tmin (C)   TMax (C)" + '\n')
    f.write("========================" + '\n')
    for t in range(len(Tmin)):
        f.write('{:>10}{:>10}'.format(str(round(Tmin[t],1)),str(round(Tmax[t],1))) + '\n')
    f.close()  
    print("Done "+filename + " !")

def AquaCrop_CLI(filename, TMPFilename, EToFilename, PLUFilename, CO2Filename = "MaunaLoa.CO2",AquaVersion = 4.0, Description = None):
    f = open(filename, 'w')
    # 1st line
    if Description is None:
        f.write("First line is a description which is displayed when selecting the file" + '\n')
    else:
        f.write(Description + '\n')
    # 2nd line
    f.write('{:>4}'.format(str(round(float(AquaVersion),1)))+"   : AquaCrop Version (June 2012)" + '\n')
    f.write(TMPFilename + '\n')
    f.write(EToFilename + '\n')
    f.write(PLUFilename + '\n')
    f.write(CO2Filename + '\n')
    f.close()
    print("Done "+filename + " !")

def HamonETo_mm(wthdata, lat = None, dz_m = 0):
    wthdata = wthdata.copy()
    def cal_daylight_hours(lat):
        if "Date" not in list(wthdata): 
            J = [julian.to_jd(item, fmt='jd') for item in wthdata.index ]
        else:
            J = [julian.to_jd(item, fmt='jd') for item in wthdata["Date"] ]
        si = [0.409*np.sin(0.0172*j-1.39) for j in J]
        phi = lat*np.pi/180
        w = [np.arccos(-np.tan(s)*np.tan(phi)) for s in si]
        wthdata["Daylight_Hr"] = [24/np.pi*wi for wi in w]
        print("Doned daylight hours at lat="+str(lat)+" !")
    cal_daylight_hours(lat)
    tlaps = 0.6 # Assume TX01 decrease 0.6 degree when dz_m = 1000 m
    temp = wthdata["TX01"] - tlaps*dz_m
    daylight_hour = wthdata["Daylight_Hr"] 
    H = np.array(daylight_hour)
    T = np.array(temp)
    es = 0.6108*np.exp(17.27*T/(T+237.3))
    wthdata["ETo"] = list(29.8*H*es/(T+273.2)) # mm
    print("Done ETo(mm)!")
    return wthdata
#HamonETo_mm(WthData,lat = 23)
# Modify all weather file in once with DataFrame  
def AquaCrop_Weather(filename, df_PP01_TX02_TX04_ET0, RainFile = None,Type = 1, Record1stD = 1, Record1stM = 1, Record1stY = 1901, Description = None, CO2Filename = "MaunaLoa.CO2", AquaVersion = 6.1, lat = 23.5, dz_m = 0):
    if "ETo" not in list(df_PP01_TX02_TX04_ET0):
        df_PP01_TX02_TX04_ET0 = HamonETo_mm(df_PP01_TX02_TX04_ET0, lat, dz_m)
    if RainFile is None: PP01 = list(df_PP01_TX02_TX04_ET0.loc[:,"PP01"])
    TX02 = list(df_PP01_TX02_TX04_ET0.loc[:,"TX02"])  # TX02 最高氣溫(℃)
    TX04 = list(df_PP01_TX02_TX04_ET0.loc[:,"TX04"])  # TX04 最低氣溫(℃)
    ETo = list(df_PP01_TX02_TX04_ET0.loc[:,"ETo"])
    AquaCrop_ETo(filename + ".ETo", ETo, Type, Record1stD, Record1stM, Record1stY, Description)
    if RainFile is None: AquaCrop_PLU(filename + ".PLU", PP01, Type, Record1stD, Record1stM, Record1stY, Description)
    AquaCrop_TMP(filename + ".TMP", TX04, TX02, Type, Record1stD, Record1stM, Record1stY, Description)
    if RainFile is None:
        AquaCrop_CLI(filename + ".CLI", filename + ".TMP", filename + ".ETo", filename + ".PLU", CO2Filename, AquaVersion, Description)
    else:
        AquaCrop_CLI(filename + ".CLI", filename + ".TMP", filename + ".ETo", RainFile, CO2Filename, AquaVersion, Description)
    
def AquaCrop_IRR(filename, df, CropType = "Rice", Planing = True, AquaVersion = 6.1):
    f = open(filename, 'w')
    if "ECw (dS/m)" not in list(df):
        df["ECw (dS/m)"] = [0.0]*df.shape[0]
    # 1st line
    f.write("\n")
    if CropType == "Rice" and Planing:
        Day = list(df.loc[:,"From day"])
        Dmin = list(df.loc[:,"Minimum depth (mm)"])
        Dapp = list(df.loc[:,"Application depth (mm)"])
        ECw = list(df.loc[:,"ECw (dS/m)"])
        # 2nd line
        f.write('{:>6}'.format(str(round(float(AquaVersion),1)))+"   : AquaCrop Version (May 2018)" + '\n')
        # 3rd line - 7th line
        f.write('{:>4}'.format(str(2))+"     : Surface irrigation: Basin" + '\n')
        f.write('{:>4}'.format(str(100))+"     : Percentage of soil surface wetted by irrigation" + '\n')
        f.write('{:>4}'.format(str(2))+"     : Generate irrigation schedule" + '\n')
        f.write('{:>4}'.format(str(4))+"     : Time criterion = minimum level of surface water layer between soil bunds" + '\n')
        f.write('{:>4}'.format(str(2))+"     : Fixed application depth" + '\n')
        # 8th line - 10th line
        f.write('\n'+"  From day    Minimum depth (mm) Application depth (mm)    ECw (dS/m)" + '\n')
        f.write("=========================================================================" + '\n')
        for t in range(len(Day)):
            f.write('{:>8}{:>15}{:>20}{:>22}'.format(str(int(Day[t])),str(int(Dmin[t])),str(int(Dapp[t])),str(round(float(ECw[t]),1)) + '\n'))
    if CropType == "Rice" and Planing is False:
        Day = list(df.loc[:,"Day"])
        Dapp = list(df.loc[:,"Depth (mm)"])
        ECw = list(df.loc[:,"ECw (dS/m)"])
        f.write('{:>6}'.format(str(round(float(AquaVersion),1)))+"   : AquaCrop Version (May 2018)" + '\n')
        f.write('{:>4}'.format(str(2))+"     : Surface irrigation: Basin" + '\n')
        f.write('{:>4}'.format(str(100))+"     : Percentage of soil surface wetted by irrigation" + '\n')
        f.write('{:>4}'.format(str(1))+"     : irrigation schedule" + '\n')
        # 8th line - 10th line
        f.write('\n'+"   Day    Depth (mm)   ECw (dS/m)" + '\n')
        f.write("=========================================================================" + '\n')
        for t in range(len(Day)):
            f.write('{:>6}{:>10}{:>13}'.format(str(int(Day[t])),str(int(Dapp[t])),str(round(float(ECw[t]),1)) + '\n'))
    f.close()   
    print("Done "+filename + " !")
    
def findpath(file, fromdir = os.getcwd()):
    for root, dirs, files in os.walk(fromdir):
        for name in files:
            if name == file:
                print("file dir: ", os.path.abspath(root)+"\\"+name)
                #os.chdir(os.path.abspath(root))
                return(os.path.abspath(root))
    print("Cannot find the file under the directory. "+file)

# PRM    
def AquaCrop_Project(filename,Dict,datapath,RainFile = None, Description = None,AquaVersion = 6.1,SuccessYearNum = None):
    def Date2Num(date):
        monthD = [0,31,59.25,90.25,120.25,151.25,181.25,212.25,243.25,273.25,304.25,334.25]
        Num = int((date.year-1901)*365.25+monthD[date.month - 1]+date.day)
        return str(Num)
    if Dict.get("Weather") is None:
        CLIfilename = Dict.get("CLI")
        TMPfilename = Dict.get("TMP")
        ETofilename = Dict.get("ETo")
        PLUfilename = Dict.get("PLU")
    else:
        CLIfilename = Dict.get("Weather")+".CLI"
        TMPfilename = Dict.get("Weather")+".TMP"
        ETofilename = Dict.get("Weather")+".ETo"
        if RainFile is None:
            PLUfilename = Dict.get("Weather")+".PLU"
        else:
            PLUfilename = RainFile
    CO2filename = Dict.get("CO2")
    CROfilename = Dict.get("CRO")
    IRRfilename = Dict.get("IRR")
    MANfilename = Dict.get("MAN")
    SOLfilename = Dict.get("SOL")
    SW0filename = Dict.get("SW0")   
    FS = Dict.get("FirstSimDate")
    LS = Dict.get("LastSimDate")
    FC = Dict.get("FirstCropDate")
    LC = Dict.get("LastCropDate")
    if SuccessYearNum is None:
        SuccessYearNum = 1
    f = open(filename, 'w')
    # 1st line
    try:
        if Description is None:
            f.write("First line is a description which is displayed when selecting the file" + '\n')
        else:
            f.write(Description + '\n')
        f.write('{:>10}      : '.format(str(AquaVersion))+"AquaCrop Version (May 2018)" + '\n')
        f.write('{:>10}      : '.format(Date2Num(FS))+"First day of simulation period - " + FS.strftime('%Y-%m-%d') + '\n')
        f.write('{:>10}      : '.format(Date2Num(LS))+"Last day of simulation period - " + LS.strftime('%Y-%m-%d') + '\n')
        f.write('{:>10}      : '.format(Date2Num(FC))+"First day of cropping period - " + FC.strftime('%Y-%m-%d') + '\n')
        f.write('{:>10}      : '.format(Date2Num(LC))+"Last day of cropping period - " + LC.strftime('%Y-%m-%d') + '\n')
        f.write('{:>10}      : '.format(str(4))+"Evaporation decline factor for stage II" + '\n')
        f.write('{:>10}      : '.format(str(1.10))+"Ke(x) Soil evaporation coefficient for fully wet and non-shaded soil surface" + '\n')
        f.write('{:>10}      : '.format(str(5))+"Threshold for green CC below which HI can no longer increase (% cover)" + '\n')
        f.write('{:>10}      : '.format(str(70))+"Starting depth of root zone expansion curve (% of Zmin)" + '\n')
        f.write('{:>10}      : '.format(str(5.00))+"Maximum allowable root zone expansion (fixed at 5 cm/day)" + '\n')
        f.write('{:>10}      : '.format(str(-6))+"Shape factor for effect water stress on root zone expansion" + '\n')
        f.write('{:>10}      : '.format(str(20))+"Required soil water content in top soil for germination (% TAW)" + '\n')
        f.write('{:>10}      : '.format(str(1.0))+"Adjustment factor for FAO-adjustment soil water depletion (p) by ETo" + '\n')
        f.write('{:>10}      : '.format(str(3))+"Number of days after which deficient aeration is fully effective" + '\n')
        f.write('{:>10}      : '.format(str(1.00))+"Exponent of senescence factor adjusting drop in photosynthetic activity of dying crop" + '\n')
        f.write('{:>10}      : '.format(str(12))+"Decrease of p(sen) once early canopy senescence is triggered (% of p(sen))" + '\n')
        f.write('{:>10}      : '.format(str(10))+"Thickness top soil (cm) in which soil water depletion has to be determined" + '\n')
        f.write('{:>10}      : '.format(str(30))+"Depth [cm] of soil profile affected by water extraction by soil evaporation" + '\n')
        f.write('{:>10}      : '.format(str(0.30))+"Considered depth (m) of soil profile for calculation of mean soil water content for CN adjustment" + '\n')
        f.write('{:>10}      : '.format(str(1))+"CN is adjusted to Antecedent Moisture Class" + '\n')
        f.write('{:>10}      : '.format(str(20))+"salt diffusion factor (capacity for salt diffusion in micro pores) [%]" + '\n')
        f.write('{:>10}      : '.format(str(100))+"salt solubility [g/liter]" + '\n')
        f.write('{:>10}      : '.format(str(16))+"shape factor for effect of soil water content gradient on capillary rise" + '\n')
        f.write('{:>10}      : '.format(str(12))+"Default minimum temperature (蚓) if no temperature file is specified" + '\n')
        f.write('{:>10}      : '.format(str(28))+"Default maximum temperature (蚓) if no temperature file is specified" + '\n')
        f.write('{:>10}      : '.format(str(3))+"Default method for the calculation of growing degree days" + '\n')
        for i in range(SuccessYearNum):
            if i > 0:
                FS = FS + relativedelta(years=+1); LS = LS + relativedelta(years=+1)
                FC = FC + relativedelta(years=+1); LC = LC + relativedelta(years=+1)
                f.write('{:>10}      : '.format(Date2Num(FS))+"First day of simulation period - " + FS.strftime('%Y-%m-%d') + '\n')
                f.write('{:>10}      : '.format(Date2Num(LS))+"Last day of simulation period - " + LS.strftime('%Y-%m-%d') + '\n')
                f.write('{:>10}      : '.format(Date2Num(FC))+"First day of cropping period - " + FC.strftime('%Y-%m-%d') + '\n')
                f.write('{:>10}      : '.format(Date2Num(LC))+"Last day of cropping period - " + LC.strftime('%Y-%m-%d') + '\n')
            f.write("-- 1. Climate (CLI) file"+"\n")
            f.write("   "+CLIfilename + '\n')
            f.write("   "+findpath(CLIfilename,datapath)+"\\" + '\n')
            f.write("   1.1 Temperature (Tnx or TMP) file" + '\n')
            f.write("   "+TMPfilename + '\n')
            f.write("   "+findpath(TMPfilename,datapath)+"\\" + '\n')
            f.write("   1.2 Reference ET (ETo) file" + '\n')
            f.write("   "+ETofilename + '\n')
            f.write("   "+findpath(ETofilename,datapath)+"\\" + '\n')
            f.write("   1.3 Rain (PLU) file" + '\n')
            f.write("   "+PLUfilename + '\n')
            f.write("   "+findpath(PLUfilename,datapath)+"\\" + '\n')
            f.write("   1.4 Atmospheric CO2 concentration (CO2) file" + '\n')
            f.write("   "+CO2filename + '\n')
            f.write("   "+findpath(CO2filename,datapath)+"\\" + '\n')
            f.write("-- 2. Crop (CRO) file" + '\n')
            f.write("   "+CROfilename + '\n')
            f.write("   "+findpath(CROfilename,datapath)+"\\" + '\n')
            f.write("-- 3. Irrigation management (IRR) file" + '\n')
            f.write("   "+IRRfilename + '\n')
            f.write("   "+findpath(IRRfilename,datapath)+"\\" + '\n')
            f.write("-- 4. Field management (MAN) file" + '\n')
            f.write("   "+MANfilename + '\n')
            f.write("   "+findpath(MANfilename,datapath)+"\\" + '\n')
            f.write("-- 5. Soil profile (SOL) file" + '\n')
            f.write("   "+SOLfilename + '\n')
            f.write("   "+findpath(SOLfilename,datapath)+"\\" + '\n')
            f.write("-- 6. Groundwater table (GWT) file" + '\n')
            f.write("   (None)" + '\n')
            f.write("   (None)" + '\n')
            f.write("-- 7. Initial conditions (SW0) file" + '\n')
            f.write("   "+SW0filename + '\n')
            f.write("   "+findpath(SW0filename,datapath)+"\\" + '\n')
            f.write("-- 8. Off-season conditions (OFF) file" + '\n')
            f.write("   (None)" + '\n')
            f.write("   (None)" + '\n')
        f.close()   
    except:
        f.close()
    print("Done "+filename + " !")    
##############################  Read File  ####################################
# Wabal.OUT
def AquaCrop_Wabal(filename, Covert2DatetimeIndex = True, plot = False, plotvar = ["Surf","Rain","Irri","RO"]):
    header = ['Day', 'Month', 'Year', 'DAP', 'Stage', 'WCTot', 'Rain', 'Irri', 'Surf', 'Infilt', 'RO', 'Drain', 'CR', 'Zgwt', 'Ex', 'E', 'E/Ex', 'Trx', 'Tr', 'Tr/Trx', 'ETx', 'ET', 'ET/ETx']
    d = pd.read_csv(filename,sep = " ",skipinitialspace = True,skiprows = 6,skipfooter = 27,names = header)
    Date = [pd.datetime(d.loc[i,"Year"], d.loc[i,"Month"], d.loc[i,"Day"]) for i in range(d.shape[0])]
    d["Date"] = Date
    print("Summery(mm):")
    print(d.loc[:,plotvar].sum())
    if Covert2DatetimeIndex:
        d = d.set_index("Date")
        d.index = pd.to_datetime(Date)
    if plot:
        d.loc[:,plotvar].plot(xticks = np.arange(d.shape[0])+1, kind = "bar", subplots = True, use_index = False)
    return d

def AquaCrop_PRMday(filename, Covert2DatetimeIndex = True, plot = False, plotvar = ["Surf","Rain","Irri","RO"]):
    header = ['Day', 'Month', 'Year', 'DAP', 'Stage', 'WC(0.88)', 'Rain', 'Irri', 'Surf', 'Infilt', 'RO', 'Drain', 'CR', 'Zgwt', 'Ex', 'E', 'E/Ex', 'Trx', 'Tr', 'Tr/Trx', 'ETx', 'ET', 'ET/ETx', 'GD', 'Z', 'tExp', 'StSto', 'StSen', 'StSalt', 'StWeed', 'CC', 'CCw', 'StTr', 'Kc(Tr)', 'Trx', 'Tr', 'TrW', 'Tr/Trx', 'WP', 'Biomass', 'HI', 'YieldPart', 'Brelative', 'WPet', 'WC(0.88)', 'Wr(0.88)', 'Z', 'Wr', 'Wr(SAT)', 'Wr(FC)', 'Wr(exp)', 'Wr(sto)', 'Wr(sen)', 'Wr(PWP)', 'SaltIn', 'SaltOut', 'SaltUp', 'Salt(0.88)', 'SaltZ', 'Z', 'ECe', 'ECsw', 'StSalt', 'Zgwt', 'ECgw', 'WC01', 'WC 2', 'WC 3', 'WC 4', 'WC 5', 'WC 6', 'WC 7', 'WC 8', 'WC 9', 'WC10', 'ECe01', 'ECe 2', 'ECe 3', 'ECe 4', 'ECe 5', 'ECe 6', 'ECe 7', 'ECe 8', 'ECe 9', 'ECe10', 'Rain', 'ETo', 'Tmin', 'Tavg', 'Tmax', 'CO2']

    d = pd.read_csv(filename,sep = " ",skipinitialspace = True,skiprows = 5,names = header)
    Date = [pd.datetime(d.loc[i,"Year"], d.loc[i,"Month"], d.loc[i,"Day"]) for i in range(d.shape[0])]
    d = d.loc[:,["DAP","Surf","Rain","Irri","RO",'Ex', 'E', 'E/Ex', 'Trx', 'Tr', 'Tr/Trx', 'ETx', 'ET', 'ET/ETx',"CC", 'Rain', 'ETo', 'Tmin', 'Tavg', 'Tmax', 'CO2',"Biomass","YieldPart"]]
    d["Date"] = Date
    print("Summery(mm):")
    print(d.loc[:,plotvar].sum())
    if Covert2DatetimeIndex:
        d = d.set_index("Date")
    if plot:
        d.loc[:,plotvar].plot(xticks = np.arange(d.shape[0])+1, kind = "bar", subplots = True, use_index = False)
    return d

def AquaCrop_PRMseason(filename, Sumvar = ["YearN","Yield","Irri","Cycle"]):
    header = ["RunNr", "Day1", "Month1", "Year1", "Rain", "ETo", "GD", "CO2", "Irri", "Infilt", "Runoff", "Drain", "Upflow", "E", "E/Ex", "Tr", "TrW", "Tr/Trx", "SaltIn", "SaltOut", "SaltUp", "SaltProf", "Cycle", "SaltStr", "FertStr", "WeedStr", "TempStr", "ExpStr", "StoStr", "BioMass", "Brelative"," HI", "Yield", "WPet", "DayN", "MonthN", "YearN"]
    d = pd.read_csv(filename,sep = " ",index_col = False, skipinitialspace = True,skiprows = 4,names = header)
    """
    data = {"YearN": d["YearN"],
            "Yield":d["Yield"],
            "Irri":d["Irri"],
            "Cycle":d["Cycle"]}
    df = pd.DataFrame(data,columns = data.keys())
    """
    df = d[Sumvar]
    print("Summery(mm):")
    print(d.loc[:,Sumvar])
    return df

def D2tenday(df, DateinIndex = False):
    df = df.copy()
    if DateinIndex is False:
        if "Date" not in list(df): print("No \"Date\" column.")
        df = df.set_index("Date") 
    L = len(df.resample("M").mean())
    y=df.index[0].year
    m=df.index[0].month
    rng = pd.date_range(pd.datetime(y,m,5),pd.datetime(df.index[-1].year,df.index[-1].month,25),freq = "D")
    rng1 = rng[rng.day == 5];rng2 = rng[rng.day == 15];rng3 = rng[rng.day == 25]
    Tenday = []; Date = []
    for i in range(L):
        df1 = df[df.index.year == y+int((m-1)/12)]
        df2 = df1[df1.index.month == (m-1)%12+1]
        df10_1 = np.nanmean(df2[df2.index.day <= 10],axis=0)
        df10_2 = df2[df2.index.day > 10];df10_2 = np.nanmean(df10_2[df10_2.index.day <= 20],axis=0)
        df10_3 = np.nanmean(df2[df2.index.day > 20],axis=0)
        Tenday.append(df10_1);Tenday.append(df10_2);Tenday.append(df10_3)
        Date.append(rng1[i]);Date.append(rng2[i]);Date.append(rng3[i])
        m += 1
    d_ini = df.index[0].day; d_last = df.index[-1].day
    h = int(d_ini/10); t = int(d_last/10) - 2; 
    if t>=0: t=len(Date)
    Tenday = Tenday[h:t]; Date = Date[h:t]
    Tenday = np.array(Tenday)
    df_tenday = pd.DataFrame(Tenday,columns = list(df))
    df_tenday.index = Date   
    return df_tenday

def TendayIndex(df10, DateinIndex = True):
    df10 = df10.copy()
    if DateinIndex is False:
        if "Date" not in list(df10): print("No \"Date\" column.")
        df10 = df10.set_index("Date")
    I1 = np.array(df10.index.month)-1; I1 = I1*3
    I2 = np.array([int(i) for i in df10.index.day/10])+1
    Index = I1+I2
    df10["Ten-days"] = Index
    return df10

#%%


#filename = r"C:\Users\Philip\Documents\GitHub\AquaCrop\AquaCropPlugin_v6\OUTP/1Rice_2012_C0C590PRMday.OUT"

#d = AquaCrop_PRMday(filename, plot = True)
#df = d.loc[:,["DAP","Irri"]][d["DAP"]>=0][d["Irri"]>=0]
#df.columns = ["Day","Depth (mm)"]
#AgriDemand = D2tenday(df, DateinIndex = True)*36735/1000*10000 #M^3/d tenday mean
#df["Depth (mm)"] = df["Depth (mm)"]*0.5
#outpath = r"C:\Users\Philip\Desktop/Irrreal.IRR"
#AquaCrop_IRR(outpath, df, CropType = "Rice", Planing = False, AquaVersion = 6.1)







