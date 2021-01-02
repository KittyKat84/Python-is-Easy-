class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = False
        self.tripsSinceMaintenance = 0

    def repair(self):
        self.needsMaintenance = False
        self.tripsSinceMaintenance = 0


class Car(Vehicle):
    def __init__(self, make, model, year, weight):
        super(Car, self).__init__(make, model, year, weight)
        self.isDriving = False

    def drive(self):
        self.isDriving = True
        self.tripsSinceMaintenance += 1

        if self.tripsSinceMaintenance > 100:
            self.needsMaintenance = True

    def stop(self):
        self.isDriving = False


car1 = Car(make='Ford Ranger', model='4x4 XL', year=2018, weight=1931)
car2 = Car(make='Opel', model='Kadett 1.4s', year=1997, weight=885)
car3 = Car(make='Audi', model='RS7', year=2021, weight=2240)

car1.drive()
car1.drive()
car2.drive()
car3.drive()
car1.drive()
car1.drive()
car3.drive()


sentence = '{} is a {} {} built in {} weighing {}kg.\nIt was used {} times since its last maintenance and it is {} that it needs another.\n\n'

print(sentence.format('The Pick Up Truck', car1.make, car1.model, car1.year, car1.weight, car1.tripsSinceMaintenance, str(car1.needsMaintenance).lower()))
print(sentence.format('Family Sedan', car2.make, car2.model, car2.year, car2.weight, car2.tripsSinceMaintenance, str(car2.needsMaintenance).lower()))
print(sentence.format('Leon\'s ride', car3.make, car3.model, car3.year, car3.weight, car3.tripsSinceMaintenance, str(car3.needsMaintenance).lower()))

car3.tripsSinceMaintenance = 100
car3.drive()

print(f'Leon is a prolific driver and it is {str(car3.needsMaintenance).lower()} that his car needs maintenance.\n')


# ---------------------------------extra--------------------------------------------------


class Plane(Vehicle):
    def __init__(self, make, model, year, weight):
        super().__init__(make, model, year, weight)
        self.isFlying = False


    def fly(self):
        if self.needsMaintenance:
            print('This plane cannot take off until repaired.')
        else:
            self.isFlying = True
            self.tripsSinceMaintenance += 1

    def land(self):
        self.isFlying = False


commercialPlane = Plane('Boeing', '737-800', 1994, 41410)

print(sentence.format('The commercial plane', commercialPlane.make, commercialPlane.model, commercialPlane.year, commercialPlane.weight, commercialPlane.tripsSinceMaintenance, str(commercialPlane.needsMaintenance).lower()))

commercialPlane.fly()
print('It is flying:', commercialPlane.isFlying)
commercialPlane.land()
print('The Boeing is flying:', commercialPlane.isFlying)
commercialPlane.needsMaintenance = True
commercialPlane.fly()