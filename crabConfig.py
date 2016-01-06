from CRABClient.UserUtilities import config
config = config()

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_DATA_75X.py"
#config.JobType.maxMemoryMB = 2500
#### Data ####
config.Data.inputDataset = "/HIPhoton40AndZ/HIRun2015-Photon-PromptReco-v1/AOD"
config.Data.lumiMask = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/DCSOnly/json_DCSONLY.txt"
#config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outLFNDirBase = "/store/user/richard/2015-Data-photonSkims/"
config.Data.outputDatasetTag = "PbPb-photonSkim-v1"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]
#config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
