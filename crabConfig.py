from CRABClient.UserUtilities import config
config = config()

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_DATA_75X_wFilter.py"
#config.JobType.maxMemoryMB = 2500
#### Data ####
config.Data.inputDataset = "/HighPtPhoton30AndZ/Run2015E-PromptReco-v1/AOD"
config.Data.lumiMask = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/5TeV/Cert_262081-262273_5TeV_PromptReco_Collisions15_25ns_JSON_v2.txt"
#config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outLFNDirBase = "/store/user/richard/2015-Data-photonSkims/"
config.Data.outputDatasetTag = "pp-photonSkim-wFilter-v0"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]
#config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
