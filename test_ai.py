import numpy as np
# https://www.cyberforum.ru/python-beginners/thread2472877.html


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


training_inputs = np.array([[0.1, 0.2, 0.3],
                            [0.5, 0.6, 0.7],
                            [0.0, 0.1, 0.2],
                            [0.6, 0.7, 0.8]])

training_outputs = np.array([[0.4, 0.8, 0.3, 0.9]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3, 1)) - 1
print("Случайные веса: ")
print(synaptic_weights)

# Метод обратного распространени
for i in range(20000):
    input_layer = training_inputs

    outputs = sigmoid(np.dot(input_layer, synaptic_weights))
    if i == 1:
        print(outputs)
    err = training_outputs - outputs

    adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))
    synaptic_weights += adjustments

print("Веса после обучения: ")
print(synaptic_weights)

print("Результат после обучения: ")
for out in outputs:
    print(round(float(out) * 10))
