# AI-Academic-projects
neural networks, genetic algorithm
# Data scraping and car price prediction  
1. [ Description. ](#neural)
2. [ How it works ](#genetic)


<a name="neural"></a>  
## 1. Neural networks  

This is implementation of neural networks solving XOR problem.

<a name="genetic"></a>  
## 2. Genetic algorithm

This is implementatnion of genetic algorithm solving optymalization problem.
![image](https://github.com/TomDzie/AI-Academic-projects/assets/117634603/f94b97fc-2c82-44e9-91e3-bebb04b25c7c)

Steps:  
1. Values must be encoded binary, starting population is chosen randomly.
2. For each individual I calculate the value of the price * demand fitness function
3. For selection I use roulette wheel method. (better the individual, higher the chance to be chosen)
4. Then I chose n/2 pairs randomly and do a crossing with probability alpha.
5. crossing is made using random cross point
6. For each individual with probability beta, I do a mutation of random chromosom
7. I assume that the stopping conditions are: maximum number of iterations, no improvement by x iterations, none
differences in the population.


