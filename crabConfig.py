from CRABClient.UserUtilities import config
config = config()

#### General ####
#config.General.requestName = "newRCTConfig"
#config.General.workArea = "newRCTConfig"
#config.General.transferLogs = True

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runUnpackerReEmulatorAnalyzer.py"

#### Data ####
config.Data.inputDataset = "/ExpressPhysics/Run2015D-Express-v4/FEVT"
#config.Data.inputDBS = "phys03"
config.Data.splitting = "LumiBased"
config.Data.runRange = "260350,260422-260433"
config.Data.unitsPerJob = 20
config.Data.totalUnits = -1

config.Data.outLFNDirBase = "/store/user/richard/L1Emulator/20151031/75X/"
config.Data.publishDataName = "PP_Physics_38T_HIFW_SecondBoard_RUNS_v2"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT","T2_US_CERN","T2_US_Vanderbilt"]
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
