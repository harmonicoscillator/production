from CRABClient.UserUtilities import config
config = config()

#config.General.requestName = "pp_15"
#config.General.requestName = "pp_30"
#config.General.requestName = "pp_50"
#config.General.requestName = "pp_80"
config.General.requestName = "pp_120"
#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_MC_75X.py"
#### Data ####
#config.Data.inputDataset = "/Pythia8_Photon15_pp502_TuneCUETP8M1/gsfs-Pythia8_Photon15_pp_RECO_20160221-0564587735dfa98972125c928a8975ef/USER"
#config.Data.inputDataset = "/Pythia8_Photon30_pp502_TuneCUETP8M1/gsfs-Pythia8_Photon30_pp_RECO_20160221-0564587735dfa98972125c928a8975ef/USER"
#config.Data.inputDataset = "/Pythia8_Photon50_pp502_TuneCUETP8M1/gsfs-Pythia8_Photon50_pp_RECO_20160221-0564587735dfa98972125c928a8975ef/USER"
#config.Data.inputDataset = "/Pythia8_Photon80_pp502_TuneCUETP8M1/gsfs-Pythia8_Photon80_pp_RECO_20160221-0564587735dfa98972125c928a8975ef/USER"
config.Data.inputDataset = "/Pythia8_Photon120_pp502_TuneCUETP8M1/gsfs-Pythia8_Photon120_pp_RECO_20160221-0564587735dfa98972125c928a8975ef/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 100
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outLFNDirBase = "/store/user/richard/2015-PP-MC-photon/"
#config.Data.outputDatasetTag = "20160222_Pythia8_Photon15_pp-v1"
#config.Data.outputDatasetTag = "20160222_Pythia8_Photon30_pp-v1"
#config.Data.outputDatasetTag = "20160222_Pythia8_Photon50_pp-v1"
#config.Data.outputDatasetTag = "20160222_Pythia8_Photon80_pp-v1"
config.Data.outputDatasetTag = "20160222_Pythia8_Photon120_pp-v1"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]
#config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
