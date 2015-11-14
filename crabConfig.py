from CRABClient.UserUtilities import config
config = config()

#### General ####
#config.General.requestName = "newRCTConfig"
#config.General.workArea = "newRCTConfig"
#config.General.transferLogs = True

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step2_RAW2DIGI_L1Reco_RECO.py"

#### Data ####
config.Data.inputDataset = "/HIHighPt/dgulhan-HIHighPt_HIRun2011_HLT_HISinglePhoton20_HISinglePhoton30-94b0666b91c951da4a167e1b3165750b/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = True
config.Data.outLFNDirBase = "/store/user/richard/HIHightPt/HIRun2011_HLT_HISinglePhoton20_HISinglePhoton30-GlobalEcalReco/"
config.Data.publishDataName = "HIRun2011_HLT_HISinglePhoton20_HISinglePhoton30-GlobalEcalReco"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
