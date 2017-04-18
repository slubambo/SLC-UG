class Car:
    def __init__(self, car_type, model="GM", car_name="General"):
        self.__speed = 0
        self.car_type = car_type
        self.model = model
        self.car_name = car_name

    def car_properties(self):
        return [self.car_type, self.model, self.car_name]

    def num_of_doors(self):
        if self.car_type == "Porshe" or self.car_type == "Koenigsegg":
            return 2
        else:
            return 4

    def car_wheels(self):
        if self.car_type == "trailer":
            return 8
        else:
            return 4

    def is_saloon(self):
        if self.car_type == "trailer":
            return False
        else:
            return True

    def speed(self):
        return self.__speed

    def drive(self, speed):
        if self.car_type == "trailer":
            self.__speed = 11 * speed
            return 11 * speed

        if self.car_name == "Mercedes":
            self.__speed = 1000
            return 1000
        else:
            return self.__speed

    def moving_man_instance(self, object_to_test):

        if isinstance(object_to_test, Car):
            return True
        else:
            return False

    def moving_man_type(self, object_to_test):
        if type(object_to_test) == Car:
            return True
        else:
            return False
