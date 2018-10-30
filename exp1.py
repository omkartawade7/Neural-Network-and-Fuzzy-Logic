import numpy as np
import random
import sys
bias = (1,)
learning_constant = 0.1

and_gate = [

# [(inputs), expected output]

[(1, 1), 1],
[(1, -1), -1],
[(-1, 1), -1],
[(-1, -1), -1]

]



or_gate = [

[(1, 1), 1],
[(1, -1), 1],
[(-1, 1), 1],
[(-1, -1), -1]

]



weights = []
def activation_function(x):
    if x>0:
        return 1
    elif x<0:
        return -1



def run_perceptron(and_gate):
    bias=(1,) # the bias is always one
    learning_constant = 0.1
    n = 50 # how many times the machine learns

    
    



# initialize with 3 random weights between -1 and 1, one for each input and one for the bias



for i in range(3):
    weights.append(random.uniform(-1, 1))



for i in range(50):
    inputs, expected_output = random.choice(and_gate)
    inputs = inputs + bias # add the bias here
    weighted_sum = np.dot(inputs, weights)
    guess = activation_function(weighted_sum) # find the sign of the weighted sum
    error = expected_output - guess
    weights += learning_constant * error * np.asarray(inputs) # change the weights to include the error times input, won't change if there's no error
    inputs, expected_output = random.choice(and_gate)
    print ("inputs: ",inputs)
    inputs=(1, 1)
    inputs = inputs + bias
    weighted_sum = np.dot(inputs, weights)
    print ("weighted sum: ",weighted_sum)
    print ("correct answer: " ,expected_output)
    print ("perceptron guess: ",activation_function(weighted_sum))
    #print("tests = int(sys.argv[1])
    tests = input("test : ")



for i in range(tests):
    print ("// AND //")
    run_perceptron(and_gate)
    print ("// OR //")
    run_perceptron(or_gate)



#Output : 


#Conclusion : Hence implemented perceptron based linear functions AND and OR function.

