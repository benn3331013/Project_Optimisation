import numpy as np
import matplotlib.pyplot as plt
import re

def visualize_clustering(f_input, f_out1, f_out2):

    input = open(f_input, 'r')

    out1 = open(f_out1, 'r')

    out2 = open(f_out2, 'r')

    input_txt = input.read()

    s = re.search(r'param a : 1 2 :=((.|\n)*?);', input_txt)

    individuals_txt = s.group(0).split('\n')[1:-1]

    individuals = np.zeros((len(individuals_txt), 2))

    count = 0
    for txt in individuals_txt:
        txt = txt.replace('\t', '').split(' ')

        individuals[count, :] = txt[1:]

        count += 1

#    print(individuals)

#   Getting the centroids
    with open('X.txt', 'r') as f:
        lines = f.readlines()
        coordinates = [float(line.split()[-1]) for line in lines[1:-2]]
        clusters_x = [coordinates[i] for i in range(0, len(coordinates), 2)]
        clusters_y = [coordinates[i] for i in range(1, len(coordinates), 2)]


#   Getting the individual's colours
    plt_colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '0.30', '0.60', '0.90', '0.75', '0.15', '0.45']
    
    with open('Y.txt', 'r') as f:
        lines = f.readlines()
        data = [line.split() for line in lines[2:-2]]
        colours_index = [ plt_colours[[i for i, x in enumerate(row[1:], 1) if x == "1"][0]-1] for row in data]


    plt.scatter(individuals[:,0], individuals[:,1], s=10., c = colours_index)

    print(clusters_x)
    print(clusters_y)
    plt.scatter(clusters_x, clusters_y, s=200., marker='+', label='centroids', c=plt_colours[:len(clusters_x)])

    plt.legend()

    plt.savefig("fuck_you.png")

    input.close()

    out1.close()

    out2.close()


if __name__ == "__main__":
    visualize_clustering("test.dat", "X.txt", "Y.txt")