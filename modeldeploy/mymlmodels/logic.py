from rdkit import Chem
from rdkit.Chem import Descriptors
from keras.models import load_model
from sklearn import *
import joblib
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def Prediction(SMILES: str):

    molecule = Chem.MolFromSmiles(SMILES)
    descriptors = []
    noUseColumns = ['NumRadicalElectrons','SMR_VSA8','SlogP_VSA9',
                    'fr_SH','fr_azide','fr_benzodiazepine','fr_diazo',
                    'fr_epoxide','fr_isocyan','fr_isothiocyan','fr_phos_acid',
                    'fr_phos_ester','fr_prisulfonamd','fr_quatN','fr_thiocyan'
                    ]
    for rdkitDescriptorName, rdkitDescriptorFunction in Descriptors.descList:
        if rdkitDescriptorName not in noUseColumns:
            descriptors.append(rdkitDescriptorFunction(molecule))
    
    minmaxscaler = joblib.load('mymlmodels/implementedModels/minmaxscaler.gz')
    descriptors = minmaxscaler.transform([descriptors])
    standardscaler = joblib.load('mymlmodels/implementedModels/standardScaler.gz')
    descriptors = standardscaler.transform(descriptors)

    nnmodel = load_model('mymlmodels/implementedModels/neuralNetwork.h5')
    nnprediction = nnmodel.predict([descriptors]).flatten()[0]
    # print("Neural network prediction: ", nnprediction)

    logisticmodel = joblib.load('mymlmodels/implementedModels/logistic.pkl')
    logisticprediction = logisticmodel.predict(descriptors).flatten()[0]
    # print("Logistic prediction: ", logisticprediction)

    svmmodel = joblib.load('mymlmodels/implementedModels/supportVector.pkl')
    svmprediction = svmmodel.predict(descriptors).flatten()[0]
    # print("SVM prediction: ", svmprediction)

    if nnprediction+logisticprediction+svmprediction > 1.5:
        prediction = True
    else:
        prediction = False

    return prediction

