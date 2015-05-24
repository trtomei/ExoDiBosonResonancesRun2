import FWCore.ParameterSet.Config as cms


isolationCutString = cms.string("")
isolationCutString = "(pfIsolationR04().sumChargedHadronPt+max(0.,pfIsolationR04().sumNeutralHadronEt+pfIsolationR04().sumPhotonEt-0.5*pfIsolationR04().sumPUPt))/pt< 0.12"

goodMuons = cms.EDFilter("PATMuonSelector",
                             src = cms.InputTag("slimmedMuons"),
                             cut = cms.string("pt > 40 && abs(eta) < 2.4 " 
                                              "&& isGlobalMuon && isPFMuon "
                                              "&& numberOfMatchedStations() > 1 "
                                              "&& dB() < 0.2 "
                                              "&& globalTrack().normalizedChi2<10 "
                                              "&& globalTrack().hitPattern().numberOfValidMuonHits>0 "
                                              "&& globalTrack().hitPattern().numberOfValidPixelHits>0 "
                                              "&& globalTrack().hitPattern().trackerLayersWithMeasurement>5 "
                                           #   "&& " + isolationCutString
                                             )
                             )

muSequence = cms.Sequence(goodMuons)
