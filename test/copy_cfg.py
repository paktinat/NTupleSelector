import FWCore.ParameterSet.Config as cms


# Give the process a name
process = cms.Process("PickEvent")



### Message Logger #############################################################
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True))


process.load("DiLeptonAnalysis.NTupleSelector.NTupleSelector_cff")
## MultiJet
process.NTupleSelector.min_HT = 350.0
process.NTupleSelector.min_njets = 4
process.NTupleSelector.HLTPaths = ['HLT_QuadJet80_v*'
                                   ,'HLT_SixJet45_v*']


## MultiJet1Parked
#process.NTupleSelector.min_HT = 300.0
#process.NTupleSelector.min_njets = 4
#process.NTupleSelector.HLTPaths = ['HLT_QuadJet50_v1','HLT_QuadJet50_v2','HLT_QuadJet50_v3','HLT_QuadJet50_v5']




# Tell the process which files to use as the sourdce
process.source = cms.Source ("PoolSource",
#          fileNames = cms.untracked.vstring ("file:///dataLOCAL/paktinat/Projects/MT2/MT2_V02-03-02/MT2Analysis/Code/MT2AnalysisCode/MT2Code/V03_09_01_MultiJet_Run2012D_PromptReco_v1_NTupleProducer_53X_data_1939_1_wj9.root")
           fileNames = cms.untracked.vstring ("file:MultiJet1Parked_D1SNTupleProducer_53X_data_9_2_nCm.root")
#fileNames = cms.untracked.vstring ("rfio:///dpm/particles.ipm.ac.ir/home/cms//store/user/paktinat/MultiJet1Parked/V03-09-01_MultiJet1Parked-Run2012D-part1-10Dec2012-v1-SecondHalf/913e379464056a6b529e5016356a02b3/NTupleProducer_53X_data_3347_3_kHY.root")

                             
)

# tell the process to only run over 100 events (-1 would mean run over
#  everything
process.maxEvents = cms.untracked.PSet(
            input = cms.untracked.int32 (-1)

)

# Tell the process what filename to use to save the output
process.Out = cms.OutputModule("PoolOutputModule",
         SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('filter') ),
         fileName = cms.untracked.string ("MyOutputFile.root")
)

process.filter = cms.Path(process.NTupleSelector)

# make sure everything is hooked up
process.end = cms.EndPath(process.Out)
