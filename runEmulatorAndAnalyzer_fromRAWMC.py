import FWCore.ParameterSet.Config as cms

process = cms.Process('L1TEMULATION')

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryIdeal_cff')

# Select the Message Logger output you would like to see:
process.load('FWCore.MessageService.MessageLogger_cfi')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
    )

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
                            fileNames = cms.untracked.vstring(
"root://xrootd.unl.edu//store/user/abaty/Hydjet1p8_TuneDrum_Quenched_MinBias_2760GeV/HydjetMB_p8_TuneDrum_Quenched_2760GeV_740pre8_MCHI_DIGI-RAW/71b4174245c8fdab441fe218fa0914ed/step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_1004_2_r6G.root"

                            )
)

process.options = cms.untracked.PSet()

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag as customiseGlobalTag
process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = 'MCHI1_74_V3')
process.GlobalTag.connect   = 'frontier://FrontierProd/CMS_CONDITIONS'

# Use PPFromRaw because it grabs the MC info correctly, then change parameters
# to match the HI emulator.
process.load('L1Trigger.L1TCalorimeter.L1TCaloStage1_PPFromRaw_cff')
process.simCaloStage1Digis.FirmwareVersion = cms.uint32(1)
process.RCTConfigProducers.hOeCut = cms.double(999)
process.caloStage1Params.jetSeedThreshold = cms.double(0.)

process.p1 = cms.Path(
    process.L1TCaloStage1_PPFromRaw
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("L1UpgradeAnalyzer.root")
)

process.L1UpgradeAnalyzer = cms.EDAnalyzer('l1t::L1UpgradeAnalyzer',
                                           InputLayer2Collection = cms.InputTag("simCaloStage1FinalDigis"),
                                           InputLayer2TauCollection = cms.InputTag("simCaloStage1FinalDigis:rlxTaus"),
                                           InputLayer2IsoTauCollection = cms.InputTag("simCaloStage1FinalDigis:isoTaus"),
                                           InputLayer2CaloSpareCollection = cms.InputTag("simCaloStage1FinalDigis:HFRingSums"),
                                           InputLayer1Collection = cms.InputTag("simRctUpgradeFormatDigis"),
                                           legacyRCTDigis = cms.InputTag("simRctDigis")
)

process.p2 = cms.Path(process.L1UpgradeAnalyzer)

process.schedule = cms.Schedule(
    process.p1, process.p2
    )
