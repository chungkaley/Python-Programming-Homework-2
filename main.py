def show_growth(cityName, startPopulation, growthRate, years):
  population = startPopulation
  print(f"\nPopulation growth for {cityName}:")
  print(f"\n2023: {population}")
  for year in range (2024, 2024 + years):
    population *= (1 + growthRate/100)
    if population > 1000000:
      print(f"Population reached 1,000,000 in year {year}")
      break
      
    print(f"{year}: {int(population)}")
  else:
    print(f"The population will not reach 1,000,000 by year {year}")
  
  


def main():
  cityName = input("Enter the city name: ")
  startPopulation = int(input("Enter the current population: "))
  growthRate =0
  while not 1 <= growthRate <= 100:
    growthRate = float(input("Enter the projected growth rate: "))
  years = int(input("Enter the number of years to simulate growth: "))
  show_growth(cityName, startPopulation, growthRate, years)

main()
  
