import numpy as np
inputs=np.array([[1,2,3,4],[3,4.5,-2.8,4.5],[3.9,1,9,-3.1]])
bias=np.array([2,3,0.69])


weights=np.array([[0.23,-0.21,-0.93,1.2],[0.2,-0.89,0.57,-0.43],[-0.23,-0.46,0.96,-0.11]])

output=np.dot(inputs,weights.T)+bias
print(output)

