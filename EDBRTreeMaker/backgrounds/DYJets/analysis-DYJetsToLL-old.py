import FWCore.ParameterSet.Config as cms

process = cms.Process( "TEST" )
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.cerr.FwkReport.limit = 99999999

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag.globaltag = '74X_mcRun2_asymptotic_v2'

#*********************************** CHOOSE YOUR CHANNEL  *******************************************#
                                                                                                    
CHANNEL         = "VZ_CHANNEL" # VZnu_CHANNEL
VZ_semileptonic = True         # False
VZ_JetMET       = False        # True
                                                                                                   
#*********************************** POOL SOURCE ****************************************************#

import sys
SAMPLE = str(sys.argv[2])
process.load("ExoDiBosonResonances.EDBRCommon.simulation.RunIIDR74X.DYJetsToLL."+SAMPLE)

configXsecs = {  "HT-100to200-aa" : 139.4,
                 "HT-100to200-ab" : 139.4,
                 "HT-100to200-ac" : 139.4,
                 "HT-100to200-ad" : 139.4,
                 "HT-100to200-ae" : 139.4,
                 "HT-100to200-af" : 139.4,
                 "HT-200to400-aa" : 42.75,
                 "HT-200to400-ab" : 42.75,
                 "HT-200to400-ac" : 42.75,
                 "HT-200to400-ad" : 42.75,
                 "HT-200to400-ae" : 42.75,
                 "HT-200to400-af" : 42.75,
                 "HT-400to600-aa" : 5.497,
                 "HT-400to600-ab" : 5.497,
                 "HT-400to600-ac" : 5.497,
                 "HT-400to600-ad" : 5.497,
                 "HT-400to600-ae" : 5.497,
                 "HT-400to600-af" : 5.497,
                 "HT-600toInf-aa" : 2.21,
                 "HT-600toInf-ab" : 2.21,
                 "HT-600toInf-ac" : 2.21,
                 "HT-600toInf-ad" : 2.21,
                 "HT-600toInf-ae" : 2.21,
                 "HT-600toInf-af" : 2.21,
                 "HT-600toInf-ag" : 2.21,
                 "HT-600toInf-ah" : 2.21,
                 "HT-600toInf-ai" : 2.21,
                 "HT-600toInf-aj" : 2.21,
              }

configNevents = {"HT-100to200-aa" : 2625679,
                 "HT-100to200-ab" : 2625679,
                 "HT-100to200-ac" : 2625679,
                 "HT-100to200-ad" : 2625679,
                 "HT-100to200-ae" : 2625679,
                 "HT-100to200-af" : 2625679,
                 "HT-200to400-aa" : 955972,
                 "HT-200to400-ab" : 955972,
                 "HT-200to400-ac" : 955972,
                 "HT-200to400-ad" : 955972,
                 "HT-200to400-ae" : 955972,
                 "HT-200to400-af" : 955972,
                 "HT-400to600-aa" : 1048047,
                 "HT-400to600-ab" : 1048047,
                 "HT-400to600-ac" : 1048047,
                 "HT-400to600-ad" : 1048047,
                 "HT-400to600-ae" : 1048047,
                 "HT-400to600-af" : 1048047,
                 "HT-600toInf-aa" : 987977,
                 "HT-600toInf-ab" : 987977,
                 "HT-600toInf-ac" : 987977,
                 "HT-600toInf-ad" : 987977,
                 "HT-600toInf-ae" : 987977,
                 "HT-600toInf-af" : 987977,
                 "HT-600toInf-ag" : 987977,
                 "HT-600toInf-ah" : 987977,
                 "HT-600toInf-ai" : 987977,
                 "HT-600toInf-aj" : 987977,
                }

usedXsec    = configXsecs[SAMPLE]
usedNevents = configNevents[SAMPLE]

#********************************  MODULES *********************************************************#

process.load("ExoDiBosonResonances.EDBRCommon.leptonicZ_cff")
process.load("ExoDiBosonResonances.EDBRCommon.hadronicZ_cff")

process.bestLeptonicV = cms.EDFilter(    "LargestPtCandSelector",
                                          src             = cms.InputTag( "leptonicVSelector"           ),
                                          maxNumber       = cms.uint32  (  1                            ))

process.bestHadronicV = cms.EDFilter(    "LargestPtCandSelector",
                                          src             = cms.InputTag( "hadronicV"                   ),
                                          maxNumber       = cms.uint32  (  1                            ))

process.graviton = cms.EDProducer(        "CandViewCombiner",
                                          decay           = cms.string  ( "bestLeptonicV bestHadronicV" ),
                                          checkCharge     = cms.bool    (  False                        ),
                                          cut             = cms.string  ( " "                           ),
                                          roles           = cms.vstring ( 'leptonicV', 'hadronicV'      ))

process.gravitonFilter =  cms.EDFilter(   "CandViewCountFilter",
                                          src             = cms.InputTag( "graviton"                    ),
                                          minNumber       = cms.uint32  (  1                            ),
                                          filter          = cms.bool    (  True                         ))

process.treeDumper = cms.EDAnalyzer(      "EDBRTreeMaker",
                                          isGen           = cms.bool      (  False                                              ),
                                          isData          = cms.bool      (  False                                              ),
                                          originalNEvents = cms.int32     (  usedNevents                                        ),
                                          crossSectionPb  = cms.double    (  usedXsec                                           ),
                                          targetLumiInvPb = cms.double    (  1000.                                              ),
                                          EDBRChannel     = cms.string    (  CHANNEL                                            ),
                                          gravitonSrc     = cms.string    ( "graviton"                                          ),
                                          metSrc          = cms.string    ( "slimmedMETs"                                       ),
                                          puWeights       = cms.FileInPath( "ExoDiBosonResonances/StatTools/pileupWeights.root" ),
                                          vertex          = cms.InputTag  ( "goodOfflinePrimaryVertex"                          ))

#***************************************** SEQUENCES **********************************************# 
process.load("ExoDiBosonResonances.EDBRCommon.hltFilter_cff")
process.load("ExoDiBosonResonances.EDBRLeptons.goodLeptonsProducer_cff")
process.load("ExoDiBosonResonances.EDBRCommon.goodJets_cff")

from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
switchOnVIDElectronIdProducer(process, DataFormat.MiniAOD)
my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV60_cff']
for idmod in my_id_modules:
    setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)

process.leptonSequence = cms.Sequence(    process.hltSequence              +
                                          process.egmGsfElectronIDs        + 
                                          process.goodLeptonsProducer      +  
                                          process.leptonicVSequence        + 
                                          process.bestLeptonicV            )

process.jetSequence = cms.Sequence(       process.fatJetsSequence          +
                                          process.hadronicVSequence        +
                                          process.bestHadronicV            )

process.gravitonSequence = cms.Sequence(  process.graviton                 +
                                          process.gravitonFilter           )

process.analysis = cms.Path(              process.leptonSequence           +
                                          process.jetSequence              +
                                          process.gravitonSequence         +
                                          process.treeDumper               )

#************************************ TRIGGER REPORT DATA *******************************************#
# Supported for VZ channel only                                   

process.load("ExoDiBosonResonances.EDBRCommon.trigReportData_cff")
process.endpath = cms.EndPath( process.trigReportData )

#****************************************************************************************************#

#***************************************** FILTER MODE **********************************************#

filterMode = True       
if filterMode == False:
    process.hltFilter.triggerConditions = ('*',)
    process.goodLeptons.filter = False
    process.leptonicVSelector.cut = '70. < mass < 110.'
    process.graviton.cut = ''

#****************************************************************************************************#

if VZ_JetMET == True :
    process.load("ExoDiBosonResonances.EDBRCommon.goodMET_cff")
    process.graviton.decay = cms.string("goodMET hadronicV")
    process.graviton.cut   = cms.string("")
    process.graviton.roles = cms.vstring('goodMET', 'hadronicV')

    process.leptonSequence.remove(  process.leptonicVSequence,
                                    process.leptonicVSelector,
                                    process.leptonicVFilter)

    process.leptonSequence.replace( process.leptonSequence,
                                    process.leptonSequence +
                                    process.metSequence    )

print "++++++++++ CUTS ++++++++++\n"
print "Graviton cut = "+str(process.graviton.cut)
print "Leptonic V cut = "+str(process.leptonicVSelector.cut)
print "Hadronic V cut = "+str(process.hadronicV.cut)
print "\n++++++++++++++++++++++++++"

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("treeEDBR_"+SAMPLE+".root")
                                  )