# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: Configuration/genproductions/HI/photon_analysis/Pyquen_Unquenched_AllQCDPhoton30_PhotonFilter20GeV_eta3_TuneZ2_PbPb_5020GeV_cfi --conditions auto:run2_mc_hi -s GEN,SIM --datatier GEN-SIM -n 1 --eventcontent RAWSIM --scenario HeavyIons --beamspot MatchHI --pileup HiMixGEN --pileup_input das:/Hydjet_Quenched_MinBias_5020GeV/HiFall14-START71_V1-v2/GEN-SIM --fileout step1_GEN_SIM_PU.root --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.HiMixGEN_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.HiGenCommon.VtxSmearedMatchHI_cff')
process.load('Configuration.StandardSequences.GeneratorMix_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/genproductions/HI/photon_analysis/Pyquen_Unquenched_AllQCDPhoton30_PhotonFilter20GeV_eta3_TuneZ2_PbPb_5020GeV_cfi nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('step1_GEN_SIM_PU.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from test.fileLists.hydjetMBFileList_Medium_cff import myFileList
process.mix.input.fileNames = myFileList

process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc_hi', '')

process.generator = cms.EDFilter("PyquenGeneratorFilter",
    PythiaParameters = cms.PSet(
        allQCDPhotonChannel = cms.vstring('MSUB(11)=1',
            'MSUB(12)=1',
            'MSUB(13)=1',
            'MSUB(28)=1',
            'MSUB(53)=1',
            'MSUB(68)=1',
            'MSUB(14)=1',
            'MSUB(18)=1',
            'MSUB(29)=1',
            'MSUB(114)=1',
            'MSUB(115)=1'),
        customProcesses = cms.vstring('MSEL=0   ! User processes'),
        kinematics = cms.vstring('CKIN(3)=30',
            'CKIN(4)=9999'),
        parameterSets = cms.vstring('pythiaUESettings',
            'customProcesses',
            'allQCDPhotonChannel',
            'kinematics'),
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution',
            'MSTJ(22)=2     ! Decay those unstable particles',
            'PARJ(71)=10 .  ! for which ctau  10 mm',
            'MSTP(33)=0     ! no K factors in hard cross sections',
            'MSTP(2)=1      ! which order running alphaS',
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)',
            'MSTP(52)=2     ! work with LHAPDF',
            'PARP(82)=1.832 ! pt cutoff for multiparton interactions',
            'PARP(89)=1800. ! sqrts for which PARP82 is set',
            'PARP(90)=0.275 ! Multiple interactions: rescaling power',
            'MSTP(95)=6     ! CR (color reconnection parameters)',
            'PARP(77)=1.016 ! CR',
            'PARP(78)=0.538 ! CR',
            'PARP(80)=0.1   ! Prob. colored parton from BBR',
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter',
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter',
            'PARP(62)=1.025 ! ISR cutoff',
            'MSTP(91)=1     ! Gaussian primordial kT',
            'PARP(93)=10.0  ! primordial kT-max',
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default',
            'MSTP(82)=4     ! Defines the multi-parton model')
    ),
    aBeamTarget = cms.double(208.0),
    angularSpectrumSelector = cms.int32(0),
    bFixed = cms.double(0.0),
    bMax = cms.double(0.0),
    bMin = cms.double(0.0),
    backgroundLabel = cms.InputTag("generator"),
    cFlag = cms.int32(0),
    comEnergy = cms.double(5020.0),
    doCollisionalEnLoss = cms.bool(False),
    doIsospin = cms.bool(True),
    doQuench = cms.bool(False),
    doRadiativeEnLoss = cms.bool(True),
    embeddingMode = cms.bool(False),
    etaMax = cms.double(3),
    filterType = cms.untracked.string('EcalGenEvtSelectorFrag'),
    hadronFreezoutTemperature = cms.double(0.14),
    maxTries = cms.untracked.int32(5000),
    numQuarkFlavor = cms.int32(0),
    particlePt = cms.vdouble(20),
    particleStatus = cms.vint32(1),
    particles = cms.vint32(22),
    partonPt = cms.vdouble(0, 0, 0, 0, 0,
        0, 0, 0),
    partonStatus = cms.vint32(2, 2, 2, 2, 2,
        2, 2, 1),
    partons = cms.vint32(1, 2, 3, 4, 5,
        6, 21, 22),
    qgpInitialTemperature = cms.double(1.0),
    qgpNumQuarkFlavor = cms.int32(0),
    qgpProperTimeFormation = cms.double(0.1)
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)

## Added manually
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq
