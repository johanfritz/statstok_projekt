# Import necessary libraries for the entire exercise.
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import scipy.signal
#import sounddevice as sd
#rom help_funcs_SSP import signalsim, getCov, melSpectrogram, melFil


#-----Part 1-----

#---1.1---
# Load the data (You can use this way the entire course)
path_to_data = "labs_python/data.mat" # Change to YOUR path to data.
data = scipy.io.loadmat(path_to_data,simplify_cells=True)
print("test change here 2024-09-13")
print(data.keys())
# Plot the sequences
plt.figure(figsize=(8, 4))
plt.plot(data["data1"], label='Realization 1')
plt.plot(data["data2"], label='Realization 2')
plt.plot(data["data3"], label='Realization 3')
plt.xlabel('Sample Index')
plt.ylabel('Value')
plt.title('Realizations of White Gaussian Noise')
plt.legend()
plt.show()