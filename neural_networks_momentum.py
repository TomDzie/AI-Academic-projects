l_rate = 0.2
epochs = 10000
momentum_factor = 0.2
start_bias = 0
inputs = [
        [0,0],
        [0,1],
        [1,0],
        [1,1]
    ]

outputs = [
        [0],
        [1],
        [1],
        [0]
    ]

import random
w11 = random.uniform(0, 1)
w21 = random.uniform(0, 1)
bias1 = start_bias

w12 = random.uniform(0, 1)
w22 = random.uniform(0, 1)
bias2 = start_bias

o1 = random.uniform(0, 1)
o2 = random.uniform(0, 1)
output_bias = start_bias

import random
import math
import matplotlib.pyplot as plt

# Add momentum terms
momentum_o1 = start_bias
momentum_o2 = start_bias
momentum_output_bias = start_bias

momentum_w11 = start_bias
momentum_w21 = start_bias
momentum_bias1 = start_bias

momentum_w12 = start_bias
momentum_w22 = start_bias
momentum_bias2 = start_bias  

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

def predict(i1, i2):
    # Hidden layer    
    s1 = w11 * i1 + w21 * i2 + bias1
    s1 = sigmoid(s1)
    s2 = w12 * i1 + w22 * i2 + bias2
    s2 = sigmoid(s2)

    # Output layer
    output = s1 * o1 + s2 * o2 + output_bias
    output = sigmoid(output)
    
    return output

def learn(i1, i2, target):
    global w11, w21, bias1, w12, w22, bias2
    global o1, o2, output_bias
    global momentum_o1, momentum_o2, momentum_output_bias
    global momentum_w11, momentum_w21, momentum_bias1
    global momentum_w12, momentum_w22, momentum_bias2
    
    hidden1_output = w11 * i1 + w21 * i2 + bias1
    hidden1_output = sigmoid(hidden1_output)
    hidden2_output = w12 * i1 + w22 * i2 + bias2
    hidden2_output = sigmoid(hidden2_output)
    
    output_layer = hidden1_output * o1 + hidden2_output * o2 + output_bias
    output_layer = sigmoid(output_layer)
    
    error = target - output_layer
    print(0.5*(error** 2))

    output_layer_weight1_diffirence = (target - output_layer) * l_rate * (output_layer * (1-output_layer)) * hidden1_output
    output_layer_weight2_diffirence = (target - output_layer) * l_rate * (output_layer * (1-output_layer)) * hidden2_output

    # Update momentum terms
    momentum_o1 = momentum_factor * momentum_o1 + output_layer_weight1_diffirence
    momentum_o2 = momentum_factor * momentum_o2 + output_layer_weight2_diffirence
    momentum_output_bias = momentum_factor * momentum_output_bias + (target - output_layer) * l_rate * (output_layer * (1-output_layer))

    o1 += momentum_o1
    o2 += momentum_o2
    output_bias += momentum_output_bias
    
    w11_diff = l_rate * i1 * (target - output_layer) * (output_layer * (1-output_layer)) * o1 * (hidden1_output * (1-hidden1_output))
    w21_diff = l_rate * i2 * (target - output_layer) * (output_layer * (1-output_layer)) * o1 * (hidden1_output * (1-hidden1_output))
    bias1_diff = l_rate * (target - output_layer) * (output_layer * (1-output_layer)) * o1 * (hidden1_output * (1-hidden1_output))

    momentum_w11 = momentum_factor * momentum_w11 + w11_diff
    momentum_w21 = momentum_factor * momentum_w21 + w21_diff
    momentum_bias1 = momentum_factor * momentum_bias1 + bias1_diff

    w11 += momentum_w11
    w21 += momentum_w21
    bias1 += momentum_bias1
    
    w12_diff = l_rate * i1 * (target - output_layer) * (output_layer * (1-output_layer)) * o2 * (hidden2_output * (1-hidden2_output))
    w22_diff = l_rate * i2 * (target - output_layer) * (output_layer * (1-output_layer)) * o2 * (hidden2_output * (1-hidden2_output))
    bias2_diff = l_rate * (target - output_layer) * (output_layer * (1-output_layer)) * o2 * (hidden2_output * (1-hidden2_output))

    momentum_w12 = momentum_factor * momentum_w12 + w12_diff
    momentum_w22 = momentum_factor * momentum_w22 + w22_diff
    momentum_bias2 = momentum_factor * momentum_bias2 + bias2_diff

    w12 += momentum_w12
    w22 += momentum_w22
    bias2 += momentum_bias2

mean_square_error = []
for epoch in range(1,epochs):
    indexes = [0,1,2,3]
    random.shuffle(indexes)
    for j in indexes:
        learn(inputs[j][0],inputs[j][1],outputs[j][0])

    if epoch%100 == 0:
        cost = 0
        for j in range(4):
            o = predict(inputs[j][0],inputs[j][1])
            cost += (outputs[j][0] - o) ** 2
            cost /= 4
        mean_square_error.append(cost)
        
for i in range(4):
    result = predict(inputs[i][0],inputs[i][1])
    print("dla wejścia", inputs[i])
    print("y_pred = ", f"{result:4.4}", "wartość oczekiwana = ", outputs[i][0])

plt.plot(range(1, int(epochs/100)), mean_square_error)
plt.xlabel('epoka *100')
plt.ylabel('błąd średniokwadratowy')
plt.show()   