import FWCore.ParameterSet.Config as cms

process = cms.Process('L1TEMULATION')

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Repacked_cff')
process.load('Configuration.Geometry.GeometryIdeal_cff')

# Select the Message Logger output you would like to see:
process.load('FWCore.MessageService.MessageLogger_cfi')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring("file:/mnt/hadoop/cms/store/user/icali/HIHighPt/HIHIHighPt_RAW_Skim_HLT_HIFullTrack14/4d786c9deacb28bba8fe5ed87e99b9e4/SD_HIFullTrack14_975_1_SZU.root")
    #fileNames = cms.untracked.vstring("file:/export/d00/scratch/belt/HIMinBiasUPC_RAW_v1/HIMinBiasUPC_RAW_v1_B0C97762-8E12-E111-A8E9-00237DDC5AF6.root")
    )

# output file
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('L1Tree.root')
)

process.options = cms.untracked.PSet()

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS1', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_P_V27A::All', '')

process.rctLayer2Format = cms.EDProducer(
    "l1t::L1TCaloRCTToUpgradeConverter",
    regionTag = cms.InputTag("simRctDigis"),
    emTag = cms.InputTag("simRctDigis"))


process.Layer2HW = cms.EDProducer(
    "l1t::Stage1Layer2Producer",
    CaloRegions = cms.InputTag("rctLayer2Format"),
    CaloEmCands = cms.InputTag("rctLayer2Format"),
    FirmwareVersion = cms.uint32(1),  ## 1=HI algo, 2= pp algo
    regionETCutForHT = cms.uint32(7),
    regionETCutForMET = cms.uint32(0),
    minGctEtaForSums = cms.int32(4),
    maxGctEtaForSums = cms.int32(17),
    jetSeedThreshold = cms.double(0.) ## seed threshold in GeV
    )

process.Layer2Phys = cms.EDProducer("l1t::PhysicalEtAdder",
                                    InputCollection = cms.InputTag("Layer2HW")
)

process.Layer2gctFormat = cms.EDProducer("l1t::L1TCaloUpgradeToGCTConverter",
    InputCollection = cms.InputTag("Layer2Phys")
    )

process.load('L1Trigger.Configuration.SimL1Emulator_cff')
process.simRctDigis.ecalDigis = cms.VInputTag(cms.InputTag('ecalDigis:EcalTriggerPrimitives'))
process.simRctDigis.hcalDigis = cms.VInputTag(cms.InputTag('hcalDigis'))
process.simGtDigis.GctInputTag = 'Layer2gctFormat'

process.digiStep = cms.Sequence(
    process.ecalDigis
    *process.hcalDigis
)

#overwrites simGctDigis in SimL1Emulator
process.simGctDigis = cms.Sequence(
    process.rctLayer2Format
    *process.Layer2HW
    *process.Layer2Phys
    *process.Layer2gctFormat
)

# L1 ntuple producers
process.load("L1TriggerDPG.L1Ntuples.l1NtupleProducer_Stage1Layer2_cfi")
process.load("L1TriggerDPG.L1Ntuples.l1ExtraTreeProducer_cfi")

process.l1extraParticles = cms.EDProducer("L1ExtraParticlesProd",
    muonSource = cms.InputTag("simGtDigis"),
    etTotalSource = cms.InputTag("Layer2gctFormat"),
    nonIsolatedEmSource = cms.InputTag("Layer2gctFormat","nonIsoEm"),
    etMissSource = cms.InputTag("Layer2gctFormat"),
    htMissSource = cms.InputTag("Layer2gctFormat"),
    produceMuonParticles = cms.bool(True),
    forwardJetSource = cms.InputTag("Layer2gctFormat","forJets"),
    centralJetSource = cms.InputTag("Layer2gctFormat","cenJets"),
    produceCaloParticles = cms.bool(True),
    tauJetSource = cms.InputTag("Layer2gctFormat","tauJets"),
    isolatedEmSource = cms.InputTag("Layer2gctFormat","isoEm"),
    etHadSource = cms.InputTag("Layer2gctFormat"),
    hfRingEtSumsSource = cms.InputTag("Layer2gctFormat"),
    hfRingBitCountsSource = cms.InputTag("Layer2gctFormat"),
    centralBxOnly = cms.bool(True),
    ignoreHtMiss = cms.bool(False)
)


process.p1 = cms.Path(
    process.digiStep
    *process.SimL1Emulator
    *process.l1NtupleProducer
    *process.l1extraParticles
    *process.l1ExtraTreeProducer
)

process.schedule = cms.Schedule(
    process.p1
    )

#process.SimpleMemoryCheck=cms.Service("SimpleMemoryCheck",
#                                      oncePerEventMode=cms.untracked.bool(False))

#process.Timing=cms.Service("Timing",
#                           useJobReport = cms.untracked.bool(True)
#                           )
