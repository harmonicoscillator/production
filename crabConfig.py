from CRABClient.UserUtilities import config
config = config()

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_DATA_75X.py"

#config.JobType.maxMemoryMB = 2500
#### Data ####
config.Data.inputDataset = "/HIPhoton40AndZ/richard-HIPhoton40AndZ_HIRun2015-v1_RECO_v2-d37fabdeb84d528fc97f536fbab90928/USER"
config.Data.inputDBS = "phys03"
#config.Data.lumiMask = "block_json.json"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outLFNDirBase = "/store/user/richard/2015-Data-fullRECOContent-HIPhoton40AndZ/"
config.Data.outputDatasetTag = "HIPhoton40AndZ_HIRun2015-v1_RECO_v2-forest"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
