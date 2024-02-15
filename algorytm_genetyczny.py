import random
import matplotlib.pyplot as plt


prices = {'11': 30, '01': 20, '10': 15, '00': 10}
demand = {'0000': 6, '0001': 3, '0010': 6, '0011': 3, '0100': 10, '0101': 5, '0110': 6, '0111': 3, '1000': 8, '1001': 4, '1010': 12, '1011': 6, '1100': 10, '1101': 5, '1110': 12, '1111': 6,}  # Popyt podstawowy dla różnych smaków

pop_size = 4
cross_prob = 0.5
mutation_prob = 0.1
iterations = 100

for i in demand:
    print(prices[i[2:]] * demand[i], i)



def draw_init_population(pop_size, declare_population = None):
    if not declare_population:
        population = [''.join([random.choice('01') for _ in range(4)]) for _ in range(pop_size)]
        return population

def fitness(population):
    value = []
    
    sum_shares = []
    total = 0
    for i in population:
        value.append(prices[i[2:]]*demand[i] )
    total = sum(value)
    shares  = [i/total for i in value]
    start = 0
    for i in shares:        
        sum_shares.append(start+i)
        start +=i
    return value, shares, sum_shares

def reproduction(population, sum_shares):
    random_values = [random.uniform(0.000001, 1.0) for i in population]
    indexes = []
    for liczba1 in random_values:
        closest = min([x for x in sum_shares if x >= liczba1], default=None)
        if closest is not None:
            indexes.append(sum_shares.index(closest))

    new_population = [population[i] for i in indexes ]
    return new_population

def mutate(population):
    new_population =[]
    for i in population:
        r = random.uniform(0,1)
        if r <= mutation_prob:
            gene = int(random.choice('0123'))
            ind = list(i)
            ind[gene] = str(int(not int(ind[gene])))
            i = ''.join(ind)
            new_population.append(i)
        else: new_population.append(i)
    return new_population

def cross(population):
    new_population = population
    for index,i in enumerate(population):
        r = random.uniform(0,1)
        if r <= cross_prob:
            pop = list(range(len(population)))
            pop.remove(index)            
            parent2 = random.choice(pop)
            cross_point = random.choice(range(1, len(population)-1))
            child = ''.join([population[index][cross_point:],population[parent2][:cross_point]])
            new_population[index] = child
    return new_population
    

value_list = []

pop = draw_init_population(pop_size)
value, shares, sum_shares = fitness(pop)

# liczba iteracji
# pop = reproduction(pop, sum_shares)
# pop = cross(pop)
# pop = mutate(pop)
# for i in range(iterations):
#     value, shares, sum_shares = fitness(pop)
#     value_list.append(sum(value)/len(value))
#     pop = reproduction(pop, sum_shares)
#     pop = cross(pop)
#     pop = mutate(pop)


#roznice w populacji
# while True:
#     pop = reproduction(pop, sum_shares)
#     pop = cross(pop)
#     pop = mutate(pop)
#     value, shares, sum_shares = fitness(pop)
#     value_list.append(sum(value)/len(value))
#     if min(value) >=  max(value):

#         break


# brak zmian przez x iteracji
it = 0
stop = 0
best = [0, 0]
while True:
    pop = reproduction(pop, sum_shares)
    pop = cross(pop)
    pop = mutate(pop)
    value, shares, sum_shares = fitness(pop)
    value_list.append(sum(value)/len(value))
    if max(value) > best[0]:       
        best = [max(value), pop[value.index(max(value))]]
    if value_list[it-1] >= value_list[it]:
        stop +=1
    else: stop = 0
    if stop >3:
        break
    it +=1    
    



print(best)
print(pop)
print(value)
print(value_list)
plt.plot(range(len(value_list)), value_list,)
plt.show()