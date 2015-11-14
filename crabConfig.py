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
config.Data.inputDataset = "/RelValZEEMM_13_HI/CMSSW_7_5_3_patch1-75X_mcRun2_HeavyIon_v5-v1/GEN-SIM-DIGI-RAW-HLTDEBUG"
#config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = True
config.Data.outLFNDirBase = "/store/group/phys_heavyions/richard/HIHightPt/RelValZEEMM_13_HI_7_5_3_patch1-GlobalEcalReco/"
config.Data.publishDataName = "RelValZEEMM_13_HI_7_5_3_patch1-GlobalEcalReco"

#### Site ####
config.Site.storageSite = "T2_CH_CERN"
#config.Site.whitelist = ["T2_US_MIT"]
#config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
