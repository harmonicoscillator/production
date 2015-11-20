from CRABClient.UserUtilities import config
config = config()

#### General ####
#config.General.requestName = "newRCTConfig"
#config.General.workArea = "newRCTConfig"
#config.General.transferLogs = True

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForest_pp_MC_75X_minbias.py"
#config.JobType.maxMemoryMB = 2500
config.JobType.inputFiles = ['HI_PythiaCUETP8M1_5020GeV_753p1_v3.db']
#### Data ####
#config.Data.inputDataset = "/MinBias_TuneCUETP8M1_5p02TeV-pythia8/twang-MinBias_TuneCUETP8M1_5p02TeV_pythia8_pp502Fall15_MCRUN2_71_V1_v1_AOD_CMSSW_7_5_4_20151113-78e0f1f0cb22713d3582ee21ebad8b42/USER"
config.Data.inputDataset = "/Neutrinos5Mfor5TeVpp/gsfs-pp5TeVPileupAOD__2015_11_18-0fbbb68e7aea6e58696cc3c7d18d21c8/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
#config.Data.publication = True
config.Data.outLFNDirBase = "/store/user/richard/2015-PP-MC/gsfs-pp5TeVPileupAOD__2015_11_18-HiForest/"
config.Data.publishDataName = "ppMinbiasHiForest"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
