def maximumPopulation(logs):
    ans = []

    for birth, death in logs:
        ans.append((birth, 1))
        ans.append((death, -1))
        
    ans.sort()

    population = 0
    max_population = 0
    max_year = 0

    for year, count in ans:
        population += count

        if population > max_population:
            max_population = population
            max_year = year
    
    return max_year

print(maximumPopulation(logs = [[1993,1999],[2000,2010]]))