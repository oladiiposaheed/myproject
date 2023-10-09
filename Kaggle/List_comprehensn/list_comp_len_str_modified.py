planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(short_planets)

for i in short_planets:
    if i.startswith('M'):
        print('The Planet is',i)
    else:
        print(i, 'does not start with letter M')