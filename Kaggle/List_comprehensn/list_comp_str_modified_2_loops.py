planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet.upper() + '!'
for planet in planets:
    if len(planet) < 6:
        print(planet)

for i in planet:
    if i.startswith('M'):
        print('The Planet is',i)
    else:
        print(i, 'does not start with letter M')