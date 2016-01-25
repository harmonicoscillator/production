from CRABClient.UserUtilities import config
config = config()

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_MIX_75X.py"
#### Data ####
config.Data.inputDataset = "/Pythia8_Photon30_Hydjet_MB/gsfs-Pythia8_Photon30_Hydjet_RECO-374be93f4012329d5cdc100aeee72e76/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outLFNDirBase = "/store/user/richard/2015-PbPb-MC-photon/"
config.Data.outputDatasetTag = "AllQCDPhoton30-v0"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]
#config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
