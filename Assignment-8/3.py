# class PokemonBasic:

#   def __init__(self, name = 'Default', hp = 0, weakness = 'None', type = 'Unknown'):
#     self.name = name
#     self.hit_point = hp
#     self.weakness = weakness
#     self.type = type  
#   def get_type(self):
#     return 'Main type: ' + self.type  
#   def get_move(self):
#     return 'Basic move: ' + 'Quick Attack'  
#   def __str__(self):
#     return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness 


# class PokemonExtra(PokemonBasic):
  
 
#   def __init__(self, name='Default', hp=0, *weakness, type="none"):
#     super().__init__(name, hp, weakness, type)
      
#     self.weakness_list = []
#     self.type_list = []      
#     self.weakness_list.append(self.weakness)
#     self.type_list.append(self.type)
#     self.weakness = list(weakness)
    
    
#   def get_type(self):
#     # return super().get_type()
#     pass
  
  
#   def get_move(self):
#     # return super().get_move()
#     pass
  
#   def __str__(self):
#     # return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness
#     return "OK"
#     pass
  
  
# print('\n------------Basic Info:--------------')
# pk = PokemonBasic()
# print(pk)
# print(pk.get_type())
# print(pk.get_move())

# print('\n------------Pokemon 1 Info:-------------')
# charmander = PokemonExtra('Charmander', 39, 'Water', 'Fire')
# print(charmander)
# print(charmander.get_type())
# print(charmander.get_move())

# print('\n------------Pokemon 2 Info:-------------')
# charizard = PokemonExtra('Charizard', 78, 'Water', 'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
# print(charizard)
# print(charizard.get_type())
# print(charizard.get_move())

class PokemonBasic:

    def __init__(self, name='Default', hp=0, weakness='None', type='Unknown'):
        self.name = name
        self.hit_point = hp
        self.weakness = weakness
        self.type = type

    def get_type(self):
        return 'Main type: ' + self.type

    def get_move(self):
        return 'Basic move: ' + 'Quick Attack'

    def __str__(self):
        return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness


class PokemonExtra(PokemonBasic):

    def __init__(self, name='Default', hp=0, weakness='None', type='Unknown', secondary_type=None, extra_moves=None):
        super().__init__(name, hp, weakness, type)
        self.secondary_type = secondary_type
        self.extra_moves = extra_moves

    def get_type(self):
        if self.secondary_type:
            return super().get_type() + ', Secondary type: ' + self.secondary_type
        return super().get_type()

    def get_move(self):
        basic_move = super().get_move()
        if self.extra_moves:
            return basic_move + '\nOther move: ' + ', '.join(self.extra_moves)
        return basic_move


print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())

print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water', 'Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())

print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water', 'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())
