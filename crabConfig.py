from CRABClient.UserUtilities import config
config = config()

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_MIX_75X.py"
config.JobType.maxMemoryMB = 2500
#### Data ####
config.Data.inputDataset = "/Pyquen_Unquenched_AllQCDPhoton30_PhotonFilter20GeV_eta24_TuneZ2_PbPb_5020GeV_GEN_SIM_PU/dgulhan-Pyquen_Unquenched_AllQCDPhoton30_PhotonFilter20GeV_eta24_TuneZ2_PbPb_5020GeV_RECODEBUG-da20efb8d790a485408707a5f3e14af7/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outLFNDirBase = "/store/user/richard/Pyquen/AllQCDPhoton30_PhotonFilter20GeV_eta24/"
config.Data.publishDataName = "Pyquen_AllQCDPhoton30_PhotonFilter20GeV_eta24-HiForest"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
