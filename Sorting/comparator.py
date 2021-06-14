from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        pass
    def comparator(a, b):
        array = list()
        array.append([a, b])
        print(array)
    
n = int(input())
data = []
for i in range(n):
    name = input('Introduce el nombre: ').split()
    score = input('Introduce la puntuación: ').split()
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)