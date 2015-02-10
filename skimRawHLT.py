import FWCore.ParameterSet.Config as cms

process = cms.Process("RAWSkim")

# import of standard configurations
process.load("Configuration.StandardSequences.Services_cff")
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("Configuration.StandardSequences.ReconstructionHeavyIons_cff")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.EventContent.EventContentHeavyIons_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    #wantSummary = cms.untracked.bool(True)
)

#process.Timing = cms.Service("Timing")

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    #'/store/hidata/HIRun2010/HIAllPhysics/RECO/ZS-v2/0033/7E0F627F-5C43-E011-AF82-003048F1CA12.root'
    #'file:/d101/icali/ROOTFiles_SWsrc392pa5/3855C0DE-FCF4-DF11-857D-003048D2C092.root'
    #'/store/hidata/HIRun2010/HIAllPhysics/RAW/v1/000/151/878/FCB5F9D9-16F5-DF11-89B1-001D09F251FE.root'
    '/store/hidata/HIRun2011/HIHighPt/RAW/v1/000/181/531/4E33D225-0A0D-E111-8C91-0025901D5DB8.root'
))


# Other statements
process.GlobalTag.globaltag = "GR_P_V27A::All"
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.load("HLTrigger.HLTfilters.hltHighLevel_cfi")

### PhotonHI SD
process.hltJet55 = process.hltHighLevel.clone(HLTPaths = ['HLT_HISinglePhoton20_v*','HLT_HISinglePhoton30_v*'])
process.filterJet55 = cms.Path(process.hltJet55)



############ Output Modules ##########


### PhotonHI SD
process.outputSdJet55 = cms.OutputModule("PoolOutputModule",
                                            SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring('filterJet55')),
                                            dataset = cms.untracked.PSet(
    dataTier = cms.untracked.string('RAW'),
    filterName = cms.untracked.string('SD_HIJet55')),
                                            outputCommands = process.RAWEventContent.outputCommands,
                                            fileName = cms.untracked.string('HIHighPt-HIRun2011-RAW-photon20.root')
                                            )

myEvContent = cms.PSet(
    outputCommands = cms.untracked.vstring('drop *_*_*_RAWSkim')
    )

process.outputSdJet55.outputCommands.extend(myEvContent.outputCommands)

process.this_is_the_end = cms.EndPath(
    process.outputSdJet55
)
