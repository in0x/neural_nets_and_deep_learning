def calc_bin_neurons(digit):
    values = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
    values[digit] = 0.99

    weights = [        
        [0.0, 2.0, 0.0, 2.0, 0.0, 2.0, 0.0, 2.0, 0.0, 2.0],
        [0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0],   
        [0.0, 0.0, 0.0, 0.0, 2.0, 2.0, 2.0, 2.0, 0.0, 0.0],    
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0]
    ]

    bias = 1
    out_neurons = [-bias, -bias, -bias, -bias]

    for w in range(0, 4):
        for i in range(0, 10):
            val_i = values[i] * weights[w][i]
            out_neurons[w] += val_i

    print("Neuron output for digit %d:" % (digit))
    print("%2.7f , %2.7f , %2.7f , %2.7f" % (out_neurons[0], out_neurons[1], out_neurons[2], out_neurons[3]))

def main():
    print("Hello world!")
    for i in range(0, 10):
        calc_bin_neurons(i)
        print("\n")


if __name__ == "__main__":
    main()