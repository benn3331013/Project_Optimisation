import numpy as np
import matplotlib.pyplot as plt

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


if __name__ == "__main__":
    gen_clustering(3, [7, 7, 7])