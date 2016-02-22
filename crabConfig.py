from CRABClient.UserUtilities import config
config = config()

#config.General.requestName = "PbPb_15"
#config.General.requestName = "PbPb_30"
#config.General.requestName = "PbPb_50"
#config.General.requestName = "PbPb_80"
config.General.requestName = "PbPb_120"
#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_MIX_75X.py"
#### Data ####
#config.Data.inputDataset = "/Pythia8_Photon15_Hydjet_MB/gsfs-Pythia8_Photon15_Hydjet_RECO_20160219-a78b3072e46c33a0fe1fffcdcc303b7d/USER"
#config.Data.inputDataset = "/Pythia8_Photon30_Hydjet_MB/gsfs-Pythia8_Photon30_Hydjet_RECO_20160220-a78b3072e46c33a0fe1fffcdcc303b7d/USER"
#config.Data.inputDataset = "/Pythia8_Photon50_Hydjet_MB/gsfs-Pythia8_Photon50_Hydjet_RECO_20160220-a78b3072e46c33a0fe1fffcdcc303b7d/USER"
#config.Data.inputDataset = "/Pythia8_Photon80_Hydjet_MB/gsfs-Pythia8_Photon80_Hydjet_RECO_20160219-a78b3072e46c33a0fe1fffcdcc303b7d/USER"
config.Data.inputDataset = "/Pythia8_Photon120_Hydjet_MB/gsfs-Pythia8_Photon120_Hydjet_RECO_20160219-a78b3072e46c33a0fe1fffcdcc303b7d/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outLFNDirBase = "/store/user/richard/2015-PbPb-MC-photon/"
#config.Data.outputDatasetTag = "20160222_Pythia8_Photon15_Hydjet-v1"
#config.Data.outputDatasetTag = "20160222_Pythia8_Photon30_Hydjet-v1"
#config.Data.outputDatasetTag = "20160222_Pythia8_Photon50_Hydjet-v1"
#config.Data.outputDatasetTag = "20160222_Pythia8_Photon80_Hydjet-v1"
config.Data.outputDatasetTag = "20160222_Pythia8_Photon120_Hydjet-v1"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]
#config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
