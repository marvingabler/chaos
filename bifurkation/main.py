import numpy as np
import matplotlib.pyplot as plt



def logistic_map(current_poplation, growth_rate):
    next_population = growth_rate*current_poplation*(1-current_poplation)
    return next_population


def plot_population_growth():

    growth_rate = np.linspace(1,4, 20)
    iterations = 400
    population = 0.05

    fig, ax = plt.subplots(int(len(growth_rate)/2), 2)
    row = 0
    column = 0

    for idx, rate in enumerate(growth_rate):

        x = []
        y = []    

        for i in range(iterations):
            
            x.append(i)
            y.append(population)
            population = logistic_map(population, rate)

        ax[row][column].plot(x,y)
        ax[row][column].set_title(rate, pad=-70.0)

        if column +1 == 2:
            row +=1
            column = 0
        else:
            column+=1

    fig.suptitle("Population growth depending on growth rate")
    plt.tight_layout()
    plt.savefig("population_growth.png")
    plt.show()
    


def plot_final_population():

    number_points = 400000
    growth_rate = np.linspace(1,4, number_points)
    iterations = 400
    population = 0.05

    # initial population
    y = np.random.uniform(0,1,size=number_points)

    for _ in range(iterations):
        y = logistic_map(y, growth_rate)

    fig, ax = plt.subplots()
    plt.plot(growth_rate, y, '.-', linewidth=0.01, markersize=0.25)
    ax.set(xlabel='Growth rate (r)', ylabel='Final Population', title='Final population depending on growth rate')
    plt.tight_layout()
    plt.savefig("final_populations.png")
    plt.show()

if __name__ == "__main__":
    plot_population_growth()
    plot_final_population()
