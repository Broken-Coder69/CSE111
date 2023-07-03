# Design a class called Pokemon using a parameterized constructor so that after
# executing the following line of code the desired result shown in the output box will be
# printed.
# The first object along with print has been done for you, you also need to create other
# objects and print accordingly to get the output correctly.
# Subtasks:
# 1. Design the Pokemon class using a parameterized constructor.
# The 5 values that are being passed through the constructor are respectively:
# 1. pokemon 1 name,
# 2. pokemon 2 name,
# 3. pokemon 1 power,
# 4. pokemon 2 power and
# 5. damage rate
# 2. Create an object named team_bulb and pass the values 'bulbasaur',
# 'squirtle', 80, 70, 9 respectively.
# 3. Use print statements accordingly to print the desired result of team_bulb.


class Pokemon:
    def __init__(self, pokemon1_name, pokemon2_name, pokemon1_power, pokemon2_power, damage_rate):
        self.pokemon1_name = pokemon1_name
        self.pokemon2_name = pokemon2_name
        self.pokemon1_power = pokemon1_power
        self.pokemon2_power = pokemon2_power
        self.damage_rate = damage_rate






team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 1=======')
print('Pokemon 1:',team_pika.pokemon1_name,
team_pika.pokemon1_power)
print('Pokemon 2:',team_pika.pokemon2_name,
team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power +
team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)
# Write your code for subtask 2 and 3 here

team_bulb = Pokemon('bulbasaur', 'squirtle', 80, 70, 9)
print('=======Team 2=======')
print('Pokemon 1:',team_bulb.pokemon1_name,
team_bulb.pokemon1_power)
print('Pokemon 2:',team_bulb.pokemon2_name,
team_bulb.pokemon2_power)
bulb_combined_power = (team_bulb.pokemon1_power +
team_bulb.pokemon2_power) * team_bulb.damage_rate
print('Combined Power:', bulb_combined_power)



# =======Team 1=======
# Pokemon 1: pikachu 90
# Pokemon 2: charmander 60
# Combined Power: 1500
# =======Team 2=======
# Pokemon 1: bulbasaur 80
# Pokemon 2: squirtle 70
# Combined Power: 1350
