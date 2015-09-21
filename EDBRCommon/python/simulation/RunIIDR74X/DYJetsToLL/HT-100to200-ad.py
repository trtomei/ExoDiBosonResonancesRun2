import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/948FA505-F72A-E511-AB94-0025905A48EC.root',
       '/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/A0791F40-392A-E511-A3B1-E41D2D08E050.root',
       '/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/A65F73B2-182A-E511-8708-20CF3027A61A.root',
       '/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/A8C14D97-182A-E511-B122-002590743042.root',
       '/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/AC8FF0ED-512F-E511-A458-20CF3027A561.root',
       '/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/B03D36C8-102B-E511-BC87-B083FED42A6E.root',
       '/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/B0D229CD-DA2D-E511-AC0F-002590D60036.root',
       '/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/B4BB1A8E-582F-E511-807A-002590D9D96E.root',
       '/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/BCDB9DEA-132B-E511-81B0-D4AE526A0B8F.root',
       '/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/BE63668E-3B2B-E511-A489-001517FAD934.root',
       '/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/C06EF291-592F-E511-96A0-008CFA166234.root',
       '/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/C0DD7EAD-DA2D-E511-948C-001E0BC18A56.root',
       '/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/C207598E-1E2B-E511-9367-0002C90F8088.root',
       '/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/C4C7EA8F-0A2B-E511-A716-0025905AA9CC.root',
       '/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/C60427C9-F62A-E511-A365-002618943882.root' ] );