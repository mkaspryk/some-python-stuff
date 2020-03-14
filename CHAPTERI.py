# title: CHAPTER I
# version: 1.01
# date: 13/03/2020
# author: Marcin Grzegorz Kaspryk

# Class represents the car object
class Car:

    # Main constructor of class Car
    def __init__(self, pax_count, car_mass, gear_count):
        if isinstance(pax_count,int) and (isinstance(car_mass,int) or isinstance(car_mass,float)) and isinstance(gear_count,int):
            if pax_count>=1 and pax_count<=5 and car_mass<=2000:
                self.pax_count=pax_count
                self.car_mass=car_mass
                self.gear_count=gear_count
                self.total_mass=self.pax_count*70+self.car_mass
            else:
                raise IllegalCarError("Wrong value assigned to pax_count or car_mass (pax_count must be in the range of 1 to 5 and car_mass must be less than 2000)")
        else:
            raise IllegalCarError("pax_count must be set to an integer, car_mass to an integer or a float and gear_count to an integer")

    # Checks and sets pax_count value
    def _set_pax_count(self,value):
        if isinstance(value,int):
            if(value>=1 and value<=5):
                self.__pax_count=value
            else:
                raise IllegalCarError("Wrong value assigned to pax_count (pax_count must be in the range of 1 to 5)")
        else:
            raise IllegalCarError("pax_count must be set to an integer")
    # Gets pax_count value
    def _get_pax_count(self):
        return self.__pax_count
    pax_count = property(_get_pax_count,_set_pax_count)

    # Checks and sets car_mass value
    def _set_car_mass(self,value):
        if isinstance(value,int) or isinstance(value,float):
            if value<=2000:
                self.__car_mass=value
            else:
                raise IllegalCarError("Wrong value assigned to car_mass (correct value for car_mass is less than 2000)")
        else:
            raise IllegalCarError("car_mass must be set to an integer or a float")
    # Gets the car_mass value
    def _get_car_mass(self):
        return self.__car_mass
    car_mass = property(_get_car_mass,_set_car_mass)


# My exception class to raise car exception
class IllegalCarError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        print('Calling str')
        if self.message:
            return 'IllegalCarError, {0} '.format(self.message)
        else:
            return 'IllegalCarError has been raised'

# Test code

c=Car(3,1600,5)
print(c.total_mass)

wrong_car_1=Car(3,2001,5)

c.pax_count=6
print(c.pax_count)

c.car_mass=2001
print(c.car_mass)
