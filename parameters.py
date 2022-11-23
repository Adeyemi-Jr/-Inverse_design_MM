import torch

#s_par_types = ['SZmax_Zmin', 'SZmin_Zmin']
s_par_type ='SZmax_Zmin'





featureDim = 12
featureName = ['acrylic_t', 'blood_t','cover_t','cross_2_h','cross_t','gl_t','period','ph','spacer_t','subs_t','w1','w2']
#featureNames = ['volFrac','thetaX', 'thetaY', 'thetaZ']

labelDim = 101

labelNames = ['32','32.11','32.22','32.33','32.44','32.55','32.66','32.77','32.88','32.99','33.1','33.21','33.32','33.43','33.54','33.65','33.76','33.87','33.98','34.09','34.2','34.31','34.42','34.53','34.64','34.75','34.86','34.97','35.08','35.19','35.3','35.41','35.52','35.63','35.74','35.85','35.96','36.07','36.18','36.29','36.4','36.51','36.62','36.73','36.84','36.95','37.06','37.17','37.28','37.39','37.5','37.61','37.72','37.83','37.94','38.05','38.16','38.27','38.38','38.49','38.6','38.71','38.82','38.93','39.04','39.15','39.26','39.37','39.48','39.59','39.7','39.81','39.92','40.03','40.14','40.25','40.36','40.47','40.58','40.69','40.8','40.91','41.02','41.13','41.24','41.35','41.46','41.57','41.68','41.79','41.9','42.01','42.12','42.23','42.34','42.45','42.56','42.67','42.78','42.89','43'];

labelNames = [ s_par_type +'_'+ x for x in labelNames]

#labelNames = ['acrylic_t', 'blood_t','cover_t','cross_2_h','cross_t','gl_t,period','ph','spacer_t','subs_t','w1','w2']

trainSplit = 0.8
testSplit = 0.1
valSplit =  0.1

batchSize = 64
batchShuffle = True
numWorkers = 0

randomWeights = False

fwdTrain = True
fwdEpochs =  200
fwdHiddenDim = [128, 128, 64, 64, 32, 32]
fwdHiddenLayers = len(fwdHiddenDim)-1
fwdLearningRate = 1e-4
fwdLossFn = torch.nn.MSELoss()

invTrain = True
invEpochs =  200
invHiddenDim = [100, 100, 100, 100, 100, 100]
invHiddenLayers = len(invHiddenDim)-1
invLearningRate = 1e-4
invLossFn = torch.nn.MSELoss()
betaX = 0.5
betaXEpochSchedule = 40
thetaMin = 0.1667 #normalized equivalent of 15 degrees