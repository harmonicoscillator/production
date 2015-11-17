from CRABClient.UserUtilities import config
config = config()

#### General ####
#config.General.requestName = "newRCTConfig"
#config.General.workArea = "newRCTConfig"
#config.General.transferLogs = True

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step3_RAW2DIGI_L1Reco_RECO.py"
config.JobType.maxMemoryMB = 2500

#### Data ####
config.Data.inputDataset = "/ZEE_5TeV_GEN_SIM_PU/twang-ZEE_5TeV_GEN_SIM_PU_step2-f3950ab07bbd1716ce99d1da3e903b99/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = True
config.Data.outLFNDirBase = "/store/user/richard/GlobalEcalRECO/ZEE_5TeV-GlobalEcalReco/"
config.Data.publishDataName = "ZEE_5TeV-GlobalEcalReco"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
