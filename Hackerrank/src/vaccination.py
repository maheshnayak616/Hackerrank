__author__ = 'mahesh.nayak'

class City :
    def __init__(self, population):
        self.clinics = 1
        self.population = population
        self.kits = self.population / self.clinics

    @property
    def clinics(self): return self.__clinics

    @property
    def population(self): return self.__population

    @property
    def kits(self):
        return self.__kits



l = raw_input()
a = l.strip().split(" ")
N, B = int(a[0]), int(a[1])
count = 0
cities = []
# cities.sort(key=lambda x: x.count, reverse=True)
while count < N:
    city = City(int(raw_input()))
    cities.append(city)
    count = count + 1
cities.sort(key=lambda x: x.kits, reverse=False)
for i in range(B - N):
    cities[N-1].clinics += 1
    cities[N-1].kits = cities[N-1].population / cities[N-1].clinics
    if cities[N -1].population % cities[N - 1].clinics:
        cities[N-1].kits = cities[N-1].kits + 1
    cities.sort(key=lambda x: x.kits, reverse=False)
max = 0
for c in cities:
    if max < c.kits:
        max = c.kits
print max
