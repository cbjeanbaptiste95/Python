# Perceptrons!

class TwoStepFun(object):
    """A step function with configurable threshold.

    >>> 3+3
    6
    >>> f1 = TwoStepFun()
    >>> f1.threshold
    0.5
    >>> f1(0.4)
    0
    >>> f1(0.6)
    1

    >>> f2 = TwoStepFun(1)
    >>> f2(0.99)
    0
    >>> f2(-1.2)
    0
    >>> f2(1.001)
    1
    """
    def __init__(self, threshold=0.5):
        self.threshold = threshold

    def __call__(self, value):
        if value < self.threshold:
            return 0
        else:
            return 1

class Perceptron(object):
    """Represent a perceptron with 2 inputs, bias.

    >>> p1 = Perceptron(TwoStepFun(1))
    >>> p1.weights = [0.6, 0.6, 0.0]
    >>> bits = [0,1]
    >>> [p1(a,b) for a in bits for b in bits]
    [0, 0, 0, 1]

    >>> p2 = Perceptron(TwoStepFun(0.5))
    >>> p2.weights = [0.6, 0.6, 0.0]
    >>> bits = [0,1]
    >>> [p2(a,b) for a in bits for b in bits]
    [0, 1, 1, 1]
    """
    def __init__(self, transfer):
        from random import random
        self.transfer = transfer
        self.weights = [random()*4-2,
                        random()*4-2,
                        random()*4-2]

    def __call__(self, x0, x1):
        avg = (x0 * self.weights[0] +
               x1 * self.weights[1] +
               1  * self.weights[2])
        return self.transfer(avg)
    """
    #Δw = α(t - y) x
    #α = learning rate
    #t = target
    #y = output
    #x = input
    #y = ((x*w) + (x*))
    """
    def learn(self, x0, x1, target):
      output = Perceptron.__call__(x0,x1)
      deltaW0 = 0
      deltaW1 = 0
      attempts = 0;
      err = (target - output)
      w0 = (x0 + deltaW0)
      w1 = (x1 + deltaW1)
      t1 = TwoStepFun()
      if (output < t1.threshold):
          deltaW0 = (0.2)*(err)*(x0)
          deltaW1 = (0.2)*(err)*(x1)
          self.learn(w0, w1,target)
          print "attempting"
      if ((err == 0) and (output == target)):
          print "success"
          

        

      
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print doctest.testmod()
    p2 = Perceptron(TwoStepFun(0.5))
    p2.weights = [0.6, 0.6, 0.0]
    bits = [0,1]
    p2.learn(0.2,0.4, 1)
    
