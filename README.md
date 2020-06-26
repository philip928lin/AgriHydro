# AgriHydro
Agriculture and Hydrological assessment model.
AgriHydro consists of 4 components and each of them will be introduced below, which each of them can be used independently.
To run AgriHydro, please follow the steps below.
1. Make sure following folders are prepared
  (1) AgriHydroPYFile		          => python files
	(2) AgriHydroCommonWthData	    => weather data folder
	(3) AgriHydroCommonSDInflowData	=> stream flow data folder
	(4) AgriHydroBlank		          => results and other files
2. Prepare weather data using MultiWG and name the file as "<GCM>_<RCP>_<start year(EX 2021)>_<station ID>.csv". Put those weather files in AgriHydroCommonWthData folder.
3. Prepare stream flow using GWLF and name the file as "<GCM>_<RCP>_<start year(EX 2021)>_<#Run (EX 1)>_<year in the Run (EX y11)>.csv". Put those stream flow files in AgriHydroCommonSDInflowData folder.
4. Exercute AgriHydro_RUN.py
  
## Multi-site Stochastic Weather Generator

The instruction, sample data, and the program can be downloaded at https://drive.google.com/drive/folders/1YCsQCfLnDI2d7cy8DR51DyG--BJSmEf0?usp=sharing

Currently, we only provide exe file for users. The source code could be provided in the future or by request. Further infomation please contact the author. 

## GWLF model
For this components, user can either run GWLF.py directly from Python or download the EXE version from the link provided in GWLF/GWLF_EXE.txt. Inside the folder we also provide sample input files "Shihmen2008_2017_SampleWthData.csv" & "ShihmenGWLFPar.csv", which represent weather input data and parameter input data respectively. Following the format of sample input files, user can run the GWLF model for their own study area.
### Demo 
#### 1. Enter your working directory

![](https://i.imgur.com/4SJTr09.png)

#### 2. Enter corresponding files and values

![](https://i.imgur.com/4gMF99J.png)

#### 3. If the Discharge is provided in "Shihmen2008_2017_SampleWthData.csv" than the validation results will be displayed. 

![](https://i.imgur.com/rNoad8Z.png)

#### 4. Output files

![](https://i.imgur.com/OEAY1o7.png)

## Taoyuan SD model
Here we provide the converted Taoyuan SD model, which can be exercuted by PySD package.
To load the model, the following code can be used.
"""
SDmodel = pysd.load(filename)
"""
More control options can be found at https://pysd-cookbook.readthedocs.io/en/latest/

## AquaCrop
