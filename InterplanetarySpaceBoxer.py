name = input("What is your name? ")

print("Hi,", name,)
weight = int(input("How much do you weigh? "))
planet = input("""And what planet are you visiting?

1. Venus   2. Mars    3. Jupiter
4. Saturn  5. Uranus  6. Neptune

""")

# Write an if statement below:
if planet == "1" or planet == "Venus" or planet == "venus":
    weight = weight * 0.91
    print("Wow", name, ", Venus is like the Australia of planets as it spins clockwise on its axis opposite the other planets in our solar system.")
    print("Your weight on Venus will be", weight)
elif planet == "2" or planet == "Mars" or planet == "mars":
    weight = weight * 0.38
    print("Wow", name, ", Mars, The Red planet. Named after the Roman God of War!")
    print("Your weight on Mars will be", weight)
elif planet == "3" or planet == "Jupiter" or planet == "jupiter":
    weight = weight * 2.34
    print("Wow", name, ", Jupiter!! hang on tight thats the fastest spinning planet in our solar system.")
    print("Your weight on Jupiter will be", weight)
elif planet == "4" or planet == "Saturn" or planet == "saturn":
    weight = weight * 1.06
    print("Wow", name, ", Saturn, wow I dont think your weight will make much of a difference as you cant stand on it but...")
    print("Your weight on Saturn will be", weight)
elif planet == "5" or planet == "Uranus" or planet == "uranus":
    weight = weight * 0.92
    print("Wow", name, ", Uranus, Brrrrrr thats our coldest planet.")
    print("Your weight on Uranus will be", weight)
elif planet == "6" or planet == "Neptune" or planet == "neptune":
    weight = weight * 1.19
    print("Wow", name, ", Neptune, God of the sea and also the furthest planet from our sun!")
    print("Your weight on Neptune will be", weight)
else: 
    print("Hrmm... something went wrong and I couldn't identify the planet. Please try again. Enter the number or the planets name listed. ", "Hope to see you soon", name)