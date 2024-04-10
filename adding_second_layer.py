import numpy as np
inputs=np.array([[1,2,3,4],
                 [3,4.5,-2.8,4.5],
                 [3.9,1,9,-3.1]])

layer1_bias=np.array([2,3,0.69])
layer2_bias=np.array([1.7,2.3,-3])


layer1_weights=np.array([[0.23,-0.21,-0.93,1.2],
                         [0.2,-0.89,0.57,-0.43],
                         [-0.23,-0.46,0.96,-0.11]])

layer2_weights=np.array([[0.32,-0.12,-0.39],
                         [0.72,-1,0.92],
                         [-0.26,-0.11,0.89]])


layer1_output=np.dot(inputs,layer1_weights.T)+layer1_bias
layer2_output=np.dot(layer1_output,layer2_weights.T)+layer2_bias

print(layer2_output)


