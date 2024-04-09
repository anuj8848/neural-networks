import numpy as np

class neurons:
    def __init__(self):
        self._inpt=None
        self.bias=None
        self._weight=None
        self._output=None
        
    @property
    def inpt(self):
        return self._inpt

    @inpt.setter
    def inpt(self,value):
        self._inpt=np.array(value)
        
    @property
    def weight(self):
        return self._weight
        
    @weight.setter
    def weight(self,value):
        self._weight=np.array(value)
    
    @property
    def output(self):
        return np.dot(self._inpt,self._weight)+self.bias

n1=neurons()
n1.bias=2
n1.inpt=[1,2,3]
n1.weight=[0.2,0.3,0.8]

print(n1.output)

