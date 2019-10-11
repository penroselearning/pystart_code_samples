class Reptile():
    def __init__(self,name,region,diet,lifespan):
        self.name = name
        self.region = region
        self.diet = diet
        self.lifespan = lifespan

        print(f'''
        Name: {self.name.title()}
        Regions Found:{self.region}
        Diet :{self.diet}
        Lifespan:{self.lifespan} years
        ---------------------
        ''')

    def eat(self): # Creating a Method start
        print(f'{self.name.title()} has a {self.diet} Diet')


komodo_dragon      = Reptile(name='komodo dragon',region='Indonesia',diet='Carnivorous',lifespan=30)
leatherback_turtle = Reptile(name='leatherback turtle',region='Global',diet='Jellyfish',lifespan=50)

komodo_dragon.eat()
leatherback_turtle.eat()