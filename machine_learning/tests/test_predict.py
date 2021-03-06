# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:55:50 2020
This script is designed to predict unseen data using pre-trained model(s).
If have multiple models, eslearn uses the mean prediction as final prediction.
@author: Li Chao, Dong Mengshi
"""

from eslearn.machine_learning.predict import Predict

# Where is the outputs
model_file = r"F:\线上讲座\demo_data\szVShc_fc\outputs.pickle"

# Where is the data_loading file
# The data_loading file could be generated by eslearn GUI
data_file = r'D:\My_Codes\virtualenv_eslearn\Lib\site-packages\eslearn\machine_learning\tests/dataLoadingTest.json'

# 
pred = Predict(data_file, model_file)
accuracy, sensitivity, specificity = pred.run()