from CRABClient.UserUtilities import config
config = config()

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestANDEmulator_PbPb_MIX_75X.py"

#### Data ####
config.Data.inputDataset = "/Hydjet_Quenched_MinBias_5020GeV/richard-HydjetMB5020_750_75X_mcRun2_HeavyIon_v1_RealisticHICollisions2011_STARTHI50_mc_RECOSIM_v3-8655645b7e5ee8730a5ca66d4a44933b/USER"
config.Data.useParent = True
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1

config.Data.outLFNDirBase = "/store/user/richard/L1Emulator/"
config.Data.publishDataName = "HydjetMB5020_750_75X_mcRun2_HeavyIon_v1_RealisticHICollisions2011_STARTHI50_mc_L1_HLT_HIFOREST_v3"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT","T2_US_CERN","T2_US_Vanderbilt"]
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
