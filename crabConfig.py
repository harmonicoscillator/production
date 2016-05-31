from CRABClient.UserUtilities import config
config = config()

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step3_RAW2DIGI_L1Reco_RECO.py"

config.JobType.maxMemoryMB = 2500
#### Data ####
config.Data.inputDataset = "/HIPhoton40AndZ/HIRun2015-v1/RAW"
config.Data.lumiMask = "block_json.json"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = True
config.Data.outLFNDirBase = "/store/user/richard/2015-Data-fullRECOContent-HIPhoton40AndZ/"
config.Data.outputDatasetTag = "HIPhoton40AndZ_HIRun2015-v1_RECO_v2"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
