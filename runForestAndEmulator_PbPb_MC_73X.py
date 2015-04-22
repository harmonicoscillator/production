 #!/usr/bin/env python2
# Run the foresting configuration on PbPb in CMSSW_5_3_X, using the new HF/Voronoi jets
# Author: Alex Barbieri
# Date: 2013-10-15

hiTrackQuality = "highPurity"              # iterative tracks
#hiTrackQuality = "highPuritySetWithPV"    # calo-matched tracks

import FWCore.ParameterSet.Config as cms
process = cms.Process('HIFOREST')
process.options = cms.untracked.PSet(
    # wantSummary = cms.untracked.bool(True)
    #SkipEvent = cms.untracked.vstring('ProductNotFound')
)

#####################################################################################
# HiForest labelling info
#####################################################################################

process.load("HeavyIonsAnalysis.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest V3",)
import subprocess
version = subprocess.Popen(["(cd $CMSSW_BASE/src && git describe --tags)"], stdout=subprocess.PIPE, shell=True).stdout.read()
if version == '':
    version = 'no git info'
process.HiForest.HiForestVersion = cms.untracked.string(version)

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring("root://xrootd.unl.edu//store/user/mnguyen/Hydjet_Quenched_MinBias_5020GeV/HydjetMB_740pre8_MCHI2_74_V3_53XBS_RECO_v5/fa4d7cedb51d6196cc0424fd90debe3f/step3_RAW2DIGI_L1Reco_RECO_101_1_1dG.root"),
                            secondaryFileNames = cms.untracked.vstring("/store/user/mnguyen/Hydjet_Quenched_MinBias_5020GeV/HydjetMB_740pre8_MCHI2_74_V3_53XBS_DIGI-RAW/6da45e4e90741bc03dbd9aec5f36c050/step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_100_1_nRy.root")
)

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10))


#####################################################################################
# Load Global Tag, Geometry, etc.
#####################################################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

# PbPb 53X MC
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc_HIon', '')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag as customiseGlobalTag
process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = 'MCHI2_74_V3')
process.GlobalTag.connect   = 'frontier://FrontierProd/CMS_CONDITIONS'

process.GlobalTag.toGet.extend([
    cms.PSet(record = cms.string("HeavyIonRcd"),
             tag = cms.string("CentralityTable_HFtowers200_HydjetDrum5_v740x01_mc"),
             connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
             label = cms.untracked.string("HFtowersHydjetDrum5")
         ),
])

from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import *
overrideGT_PbPb2760(process)

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")
process.centralityBin.nonDefaultGlauberModel = cms.string("HydjetDrum5")

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("HiForest.root"))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################

process.load('HeavyIonsAnalysis.JetAnalysis.jets.HiGenJetsCleaned_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3CaloJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3PFJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_PbPb_mc_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4CaloJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4PFJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_PbPb_mc_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5CaloJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5CaloJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5PFJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5PFJetSequence_PbPb_mc_cff')

process.akPu3CaloJetAnalyzer.doSubEvent = cms.untracked.bool(False)
process.akPu4CaloJetAnalyzer.doSubEvent = cms.untracked.bool(False)
process.akPu3PFJetAnalyzer.doSubEvent = cms.untracked.bool(False)
process.akPu4PFJetAnalyzer.doSubEvent = cms.untracked.bool(False)
process.akVs3CaloJetAnalyzer.doSubEvent = cms.untracked.bool(False)
process.akVs4CaloJetAnalyzer.doSubEvent = cms.untracked.bool(False)
process.akVs3PFJetAnalyzer.doSubEvent = cms.untracked.bool(False)
process.akVs4PFJetAnalyzer.doSubEvent = cms.untracked.bool(False)

process.jetSequences = cms.Sequence(process.akPu3CaloJetSequence +
                                    process.akVs3CaloJetSequence +
                                    process.akVs3PFJetSequence +
                                    process.akPu3PFJetSequence +

                                    process.akPu4CaloJetSequence +
                                    process.akVs4CaloJetSequence +
                                    process.akVs4PFJetSequence +
                                    process.akPu4PFJetSequence

                                    #process.akPu5CaloJetSequence +
                                    #process.akVs5CaloJetSequence +
                                    #process.akVs5PFJetSequence +
                                    #process.akPu5PFJetSequence

                                    )

process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_mc_cfi')
process.hiEvtAnalyzer.doMC = cms.bool(False) #the gen info dataformat has changed in 73X, we need to update hiEvtAnalyzer code
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
process.hltanalysis.HLTProcessName = cms.string('HIFOREST')
process.hltanalysis.hltresults = cms.InputTag("TriggerResults","","HIFOREST")
process.hltanalysis.l1GtReadoutRecord = cms.InputTag("simGtDigis","","HIFOREST")
process.hltanalysis.l1GctHFBitCounts = cms.InputTag("simCaloStage1LegacyFormatDigis")
process.hltanalysis.l1GctHFRingSums = cms.InputTag("simCaloStage1LegacyFormatDigis")
process.load('HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi')

#####################################################################################
# To be cleaned

process.load('HeavyIonsAnalysis.JetAnalysis.ExtraTrackReco_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_MC_cff')
process.load("HeavyIonsAnalysis.TrackAnalysis.METAnalyzer_cff")
process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_cfi")
process.load('HeavyIonsAnalysis.JetAnalysis.rechitanalyzer_cfi')
process.rechitAna = cms.Sequence(process.rechitanalyzer+process.pfTowers)
process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0

#####################################################################################

#########################
# Track Analyzer
#########################
process.anaTrack.qualityStrings = cms.untracked.vstring('highPurity','highPuritySetWithPV')
process.pixelTrack.qualityStrings = cms.untracked.vstring('highPurity','highPuritySetWithPV')
process.hiTracks.cut = cms.string('quality("highPurity")')

# set track collection to iterative tracking
process.anaTrack.trackSrc = cms.InputTag("hiGeneralTracks")

# clusters missing in recodebug - to be resolved
process.anaTrack.doPFMatching = False
process.pixelTrack.doPFMatching = False

# process.ppTrack.doSimVertex = True
# process.ppTrack.doSimTrack = True
# process.ppTrack.fillSimTrack = True

process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cff")
process.tpRecoAssocGeneralTracks = process.trackingParticleRecoTrackAsssociation.clone()
process.tpRecoAssocGeneralTracks.label_tr = cms.InputTag("hiGeneralTracks")
process.quickTrackAssociatorByHits.ComponentName = cms.string('quickTrackAssociatorByHits')


#####################
# photons
process.load('HeavyIonsAnalysis.JetAnalysis.EGammaAnalyzers_cff')
process.multiPhotonAnalyzer.GenEventScale = cms.InputTag("generator")
process.multiPhotonAnalyzer.HepMCProducer = cms.InputTag("generator")
process.RandomNumberGeneratorService.multiPhotonAnalyzer = process.RandomNumberGeneratorService.generator.clone()
process.load('HeavyIonsAnalysis.PhotonAnalysis.ggHiNtuplizer_cfi')

process.photonMatch.matched = cms.InputTag("genParticles")
process.multiPhotonAnalyzer.GenParticleProducer = cms.InputTag("genParticles")
process.ggHiNtuplizer.genParticleSrc = cms.InputTag("genParticles")
#####################
# muons
######################
process.load("HeavyIonsAnalysis.MuonAnalysis.hltMuTree_cfi")
process.hltMuTree.doGen = cms.untracked.bool(True)
process.load("RecoHI.HiMuonAlgos.HiRecoMuon_cff")
process.muons.JetExtractorPSet.JetCollectionLabel = cms.InputTag("akVs3PFJets")
process.globalMuons.TrackerCollectionLabel = "hiGeneralTracks"
process.muons.TrackExtractorPSet.inputTrackCollection = "hiGeneralTracks"
process.muons.inputCollectionLabels = ["hiGeneralTracks", "globalMuons", "standAloneMuons:UpdatedAtVtx", "tevMuons:firstHit", "tevMuons:picky", "tevMuons:dyt"]

# HYDJET RECO file didn't have ak2GenJets and ak6GenJets as input, so removed them
# and ran our own hiGenJetsCleaned sequence
from HeavyIonsAnalysis.JetAnalysis.jets.HiGenJetsCleaned_cff import *

process.hiSelectGenJets = cms.Sequence(
    ak3HiGenJetsCleaned +
    ak4HiGenJetsCleaned +
    #ak5HiGenJetsCleaned +
    ak7HiGenJetsCleaned
)

process.HiGenParticleAna.genParticleSrc = cms.untracked.InputTag("genParticles")

process.load('HeavyIonsAnalysis.Configuration.hlt_MC_stage1_cff')
#from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1_HI
#process = customisePostLS1_HI(process)
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC
process = customizeHLTforMC(process)
# add release-specific customizations
from HLTrigger.Configuration.customizeHLTforCMSSW import customiseHLTforCMSSW
process = customiseHLTforCMSSW(process,menuType="HIon",fastSim=False)

# load 2015 Run-2 L1 Menu for HIon
from L1Trigger.Configuration.customise_overwriteL1Menu import L1Menu_CollisionsHeavyIons2015_v0 as loadL1Menu
process = loadL1Menu(process)


########## L1 ##############
# Use PPFromRaw because it grabs the MC info correctly, then change parameters
# to match the HI emulator.
#process.load('L1Trigger.L1TCalorimeter.L1TCaloStage1_PPFromRaw_cff')
# override the L1 menu from an Xml file
process.l1GtTriggerMenuXml = cms.ESProducer("L1GtTriggerMenuXmlProducer",
  TriggerMenuLuminosity = cms.string('startup'),
  DefXmlFile = cms.string('L1Menu_CollisionsHeavyIons2011_v0_nobsc_notau_centrality_q2_singletrack.v1.xml'),
  VmeXmlFile = cms.string('')
)
process.L1GtTriggerMenuRcdSource = cms.ESSource("EmptyESSource",
  recordName = cms.string('L1GtTriggerMenuRcd'),
  iovIsRunNotTime = cms.bool(True),
  firstValid = cms.vuint32(1)
)
process.es_prefer_l1GtParameters = cms.ESPrefer('L1GtTriggerMenuXmlProducer','l1GtTriggerMenuXml')

# customize the L1 emulator to run customiseL1EmulatorFromRaw with HLT to switchToSimStage1Digis
process.load( 'Configuration.StandardSequences.RawToDigi_cff' )
process.load( 'Configuration.StandardSequences.SimL1Emulator_cff' )
import L1Trigger.Configuration.L1Trigger_custom
#

# 2015 Run2 emulator
import L1Trigger.L1TCalorimeter.L1TCaloStage1_customForHLT
process = L1Trigger.L1TCalorimeter.L1TCaloStage1_customForHLT.customiseL1EmulatorFromRaw( process )

#
process = L1Trigger.Configuration.L1Trigger_custom.customiseResetPrescalesAndMasks( process )
# customize the HLT to use the emulated results
import HLTrigger.Configuration.customizeHLTforL1Emulator
process = HLTrigger.Configuration.customizeHLTforL1Emulator.switchToL1Emulator( process )
process = HLTrigger.Configuration.customizeHLTforL1Emulator.switchToSimStage1Digis( process )

process.simCaloStage1Digis.FirmwareVersion = cms.uint32(1)
process.caloStage1Params.jetSeedThreshold = cms.double(0.)
process.RCTConfigProducers.eicIsolationThreshold = cms.uint32(7)
process.RCTConfigProducers.hOeCut = cms.double(999)
process.RCTConfigProducers.eMinForHoECut = cms.double(999)
process.RCTConfigProducers.eMaxForHoECut = cms.double(999)
process.RCTConfigProducers.hMinForHoECut = cms.double(999)
process.RCTConfigProducers.eMinForFGCut = cms.double(999)


process.L1UpgradeAnalyzer = cms.EDAnalyzer('l1t::L1UpgradeAnalyzer',
                                           InputLayer2Collection = cms.InputTag("simCaloStage1FinalDigis"),
                                           InputLayer2TauCollection = cms.InputTag("simCaloStage1FinalDigis:rlxTaus"),
                                           InputLayer2IsoTauCollection = cms.InputTag("simCaloStage1FinalDigis:isoTaus"),
                                           InputLayer2CaloSpareCollection = cms.InputTag("simCaloStage1FinalDigis:HFRingSums"),
                                           InputLayer1Collection = cms.InputTag("simRctUpgradeFormatDigis"),
                                           legacyRCTDigis = cms.InputTag("simRctDigis")
)
##################################


process.ana_step = cms.Path(#process.L1TCaloStage1_PPFromRaw *
                            process.L1UpgradeAnalyzer *
                            process.heavyIon*
                            process.hltanalysis *
#temp                            process.hltobject *
                            process.centralityBin *
                            process.hiEvtAnalyzer*
                            process.HiGenParticleAna*
                            #process.hiGenJetsCleaned*
                            #process.quickTrackAssociatorByHits*
                            #process.tpRecoAssocGeneralTracks + #used in HiPFJetAnalyzer
                            process.hiSelectGenJets +
                            process.jetSequences +
                            process.photonStep_withReco +
                            #process.ggHiNtuplizer +
                            process.pfcandAnalyzer +
                            process.rechitAna +
#temp                            process.hltMuTree +
                            process.HiForest +
                            # process.cutsTPForFak +
                            # process.cutsTPForEff +
                            process.anaTrack
                            #process.pixelTrack
                            )

process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')
process.phltJetHI = cms.Path( process.hltJetHI )
process.pcollisionEventSelection = cms.Path(process.collisionEventSelection)
process.pHBHENoiseFilter = cms.Path( process.HBHENoiseFilter )
process.phfCoincFilter = cms.Path(process.hfCoincFilter )
process.phfCoincFilter3 = cms.Path(process.hfCoincFilter3 )
process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter )
process.phltPixelClusterShapeFilter = cms.Path(process.siPixelRecHits*process.hltPixelClusterShapeFilter )
process.phiEcalRecHitSpikeFilter = cms.Path(process.hiEcalRecHitSpikeFilter )

process.skimanalysis.hltresults = cms.InputTag("TriggerResults", "", "HIFOREST")
process.pAna = cms.EndPath(process.skimanalysis)

process.schedule = cms.Schedule()
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.ana_step, process.phltJetHI, process.pcollisionEventSelection, process.pHBHENoiseFilter, process.phfCoincFilter, process.phfCoincFilter3, process.pprimaryVertexFilter, process.phltPixelClusterShapeFilter, process.phiEcalRecHitSpikeFilter, process.pAna])

# Customization
