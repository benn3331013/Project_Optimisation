import numpy as np
import matplotlib.pyplot as plt
import re

def gen_clustering(n_clusters : int, pp_cluster : list):
    # Map is [0,10]x[0,10]

    individuals = [np.random.normal(loc=np.random.uniform(0,10), scale=np.random.uniform(0, 2), size=(pp_cluster[i], 2)) for i in range(n_clusters)]

    file = open('test.dat', 'w')

    file.write("param d := 2;\n\n")

    file.write("param n_indivuals := {};\n\n".format(sum(pp_cluster)))

    file.write("param a := 1 2\n")

    count = 1
    for i in range(n_clusters):
        for j in range(pp_cluster[i]):
            file.write("\t{} {} {}\n".format(count, individuals[i][j, 0], individuals[i][j, 1]))
            count += 1

    file.write(";\n\n")

    file.write("demands := \n")

    for i in range(sum(pp_cluster)):
        file.write("\t{} 1\n".format(i+1))

    file.write(";\n\n")

    file.write("param p := {};\n\n".format(n_clusters))

    file.write("param Q := \n")

    for i in range(n_clusters):
        file.write("\t{} {}\n".format(i+1, pp_cluster[i]))

    file.write(";\n")

    file.close()

    for i in range(n_clusters):

        print(individuals[i][:,0], individuals[i][:,0])

        plt.scatter(individuals[i][:,0], individuals[i][:,1], label="Cluster {}".format(i))

    #plt.show()

    plt.savefig("test.png")

def visualize_clustering(f_input, f_out1, f_out2):

    input = open(f_input, 'r')

    out1 = open(f_out1, 'r')

    out2 = open(f_out2, 'r')

    input_txt = input.read()

    s = re.search(r'param a := 1 2((.|\n)*?);', input_txt)

    individuals_txt = s.group(0).split('\n')[1:-1]

    individuals = np.zeros((len(individuals_txt), 2))

    count = 0
    for txt in individuals_txt:
        txt = txt.replace('\t', '').split(' ')

        individuals[count, :] = txt[1:]

        count += 1

    print(individuals)

    centroids_txt = out1.read().replace('  ', '').split('\n')[1:-3]


    centroids = np.zeros((int(len(centroids_txt)/2), 2))
    count = 0
    for txt in centroids_txt:
        txt = txt.split(' ')

        centroids[int(count/2), count%2] = txt[-1]

        count += 1

    print(centroids)

    clusters_txt = out2.read().replace('  ', '').split('\n')[1:-3]
    #clusters = np.zeros()

    one_clusters = [txt for txt in clusters_txt if txt[-1] == '1']

    clusters = np.array([int(txt.split(' ')[1]) for txt in one_clusters])

    print(clusters)

    plt.scatter(individuals[:,0], individuals[:,1], c = clusters)

    plt.scatter(clusters[:,0], clusters[:,1], '+', label='centroids')

    plt.legend()

    plt.show()

    input.close()

    out1.close()

    out2.close()


if __name__ == "__main__":
    #gen_clustering(3, [7, 7, 7])

    visualize_clustering("test.dat", "piss.txt", "shit.txt")