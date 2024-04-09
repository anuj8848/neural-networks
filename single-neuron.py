import numpy as np

class neurons:
    count=0
 
    def __init__(self):
        self._inpt=None
        self._bias=None
        self._weight=None
        self._output=None
        
    @property
    def inpt(self):
        return self._inpt
    
    @property
    def bias(self):
        return self._bias 
    
    @bias.setter
    def bias(self,value):
        self._bias=value

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
    
inputs=[1,2,3,4]


n1=neurons()
n1.bias=2
n1.inpt=inputs
n1.weight=[0.23,-0.21,-0.93,1.2]

n2=neurons()
n2.bias=3
n2.inpt=inputs
n2.weight=[0.2,-0.89,0.57,-0.43]


n3=neurons()
n3.bias=0.69
n3.inpt=inputs
n3.weight=[-0.23,-0.46,0.96,-0.11]

n_layer_outpt=np.array([n1.output,n2.output,n3.output])


print(n_layer_outpt)
    