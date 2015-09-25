import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015D/SingleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/C8056B20-5A60-E511-A277-02163E012757.root',
       '/store/data/Run2015D/SingleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/C8AD9681-4360-E511-A978-02163E01435A.root',
       '/store/data/Run2015D/SingleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/D2D06D1B-5A60-E511-88DC-02163E01284C.root',
       '/store/data/Run2015D/SingleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/F23710DF-4460-E511-A746-02163E0142FD.root',
       '/store/data/Run2015D/SingleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/FCB85319-5A60-E511-9007-02163E014417.root',
       '/store/data/Run2015D/SingleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/FE7F9005-4560-E511-8D61-02163E0142F1.root',
       '/store/data/Run2015D/SingleMuon/MINIAOD/PromptReco-v3/000/256/734/00000/84C8C331-4960-E511-AFD1-02163E014144.root',
       '/store/data/Run2015D/SingleMuon/MINIAOD/PromptReco-v3/000/256/734/00000/C08D5C42-4960-E511-BD77-02163E0145C4.root',
       '/store/data/Run2015D/SingleMuon/MINIAOD/PromptReco-v3/000/256/734/00000/E4FB9549-4960-E511-A4A1-02163E014741.root',
       '/store/data/Run2015D/SingleMuon/MINIAOD/PromptReco-v3/000/256/801/00000/48894C8A-2960-E511-8D45-02163E01348F.root',
       '/store/data/Run2015D/SingleMuon/MINIAOD/PromptReco-v3/000/256/801/00000/AAF9C683-2960-E511-BF68-02163E014297.root',
       '/store/data/Run2015D/SingleMuon/MINIAOD/PromptReco-v3/000/256/801/00000/CC461D87-2960-E511-820F-02163E0141EA.root',
       '/store/data/Run2015D/SingleMuon/MINIAOD/PromptReco-v3/000/256/842/00000/E2BD56BB-4760-E511-B0C8-02163E014750.root' ] );
