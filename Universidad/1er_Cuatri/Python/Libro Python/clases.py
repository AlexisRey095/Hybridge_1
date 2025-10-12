
#! ejercicio de clases 

class restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'\nRestaurant`s name is {self.restaurant_name} and type is {self.cuisine_type}')
    
    def open_restaurant(self):
        print('The resturant is open')

restaurant1 = restaurant('alexis houses', 'piizas')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = restaurant('karen`s Tabberns ', 'Meets&grills')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

#! Ejercicio 2

class user:
    def __init__(self, name, age, job, city):
        self.name = name
        self.age = age
        self.job = job
        self.city = city
    
    def gree_user(self):
        print(f'\nHi {self.name}, your age is {self.age}, you are {self.job} and you live in {self.city} ')

user1 = user('alexis', 30, 'engineer', 'puebla')
user1.gree_user()

user2 = user('rebeca', 20, 'nourse', 'monterrey')
user2.gree_user()

user3 = user('susana', 40, 'sellwoman', 'Queretaro')
user3.gree_user()

class car:
    def __init__(self,model, name, miles):
        self.model = model
        self.name = name
        self.miles = miles
    
    def summary(self):
        print(f'the is a {self.model}, {self.name} with {self.miles} miles')

class electricar(car):
    def __init__(self, model, name, miles):
        super().__init__(model, name, miles)
        self.battery = 40
    
    def baterry_status (self):
        status = f'this car has {self.battery} khw'
        return status

my_leaf =electricar('byd', 'ppq12', 123)
my_leaf.summary()
print(my_leaf.baterry_status())