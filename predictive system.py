import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open(
    'S:\\Coding\\Github\\Design Engineering Project\\Parkinsons-Disease-Classification\\predictive system.py', 'rb'))


input_data = (91.904, 115.871, 86.292, 0.0054, 0.00006, 0.00281, 0.00336, 0.00844, 0.02752, 0.249, 0.01424,
              0.01641, 0.02214, 0.04272, 0.01141, 21.414, 0.58339, 0.79252, -4.960234, 0.363566, 2.642476, 0.275931)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
    print('The person has not Parkinsons Disease')
else:
    print('The person has Parkinsons Disease')
