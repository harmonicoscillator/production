from CRABClient.UserUtilities import config
config = config()

#### General ####
#config.General.requestName = "newRCTConfig"
#config.General.workArea = "newRCTConfig"
#config.General.transferLogs = True

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "makeOrscLinkPatterns_largeStats.py"
config.JobType.outputFiles = ["rx_summary.txt"]

#### Data ####
config.Data.inputDataset = "/HIMinBiasUPC/icali-HIMinBiasUPC_Skim_HLT_HIMinBiasHfOrBSC_v2-35880fcf9fb9fd84b27cd1405e09ffd1-SD_MinBiasHI/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "EventAwareLumiBased"
config.Data.unitsPerJob = 1000
config.Data.totalUnits = -1

config.Data.outLFNDirBase = "/store/group/phys_heavyions/richard/L1Emulator/icali-HIMinBiasUPC_Skim_HLT_HIMinBiasHfOrBSC_v2_rx_summary"
config.Data.publishDataName = "PbPb_minbias_rx_summary_v1"

#### Site ####
config.Site.storageSite = "T2_CH_CERN"
#config.Site.whitelist = ["T2_US_MIT","T2_US_CERN","T2_US_Vanderbilt"]
#config.Site.blacklist = ["T0","T1"]

#### User ####
# ???
