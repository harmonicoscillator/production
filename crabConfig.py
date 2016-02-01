from CRABClient.UserUtilities import config
config = config()

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_MC_75X.py"
#### Data ####
config.Data.inputDataset = "/Pythia8_Photon30_pp502_TuneCUETP8M1/gsfs-Pythia8_Photon30_pp_RECO_v2-24bc0f2c47ba7a24fbd3e8494fe06297/USER"
#config.Data.lumiMask = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/5TeV/Cert_262081-262273_5TeV_PromptReco_Collisions15_25ns_JSON_v2.txt"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outLFNDirBase = "/store/user/richard/2015-PP-MC/"
config.Data.outputDatasetTag = "Pythia8_Photon30_pp502_TuneCUETP8M1-v0"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]
#config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
