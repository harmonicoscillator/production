from CRABClient.UserUtilities import config
config = config()

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_DATA_75X.py"
#### Data ####
config.Data.inputDataset = "/HIHardProbesPhotons/HIRun2015-PromptReco-v1/AOD"
config.Data.lumiMask = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON.txt"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outLFNDirBase = "/store/user/richard/2015-Data-promptRECO-photonSkims/"
config.Data.outputDatasetTag = "PbPb-photonHLTFilter-v0"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]
#config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
