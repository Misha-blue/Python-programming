import os
import csv


class CarBase:
    ix_car_type = 0
    ix_brand = 1
    ix_passenger_seats_count = 2
    ix_photo_file_name = 3
    ix_body_whl = 4
    ix_carrying = 5
    ix_extra = 6

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        _, file_extension = os.path.splitext(self.photo_file_name)
        return file_extension


class Car(CarBase):
    car_type = "car"

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

    @classmethod
    def from_tuple(cls, row):
        return cls(row[cls.ix_brand],
                   row[cls.ix_photo_file_name],
                   row[cls.ix_carrying],
                   row[cls.ix_passenger_seats_count])


class Truck(CarBase):
    car_type = "truck"

    def __init__(self, brand, photo_file_name, carrying, body_whl=None):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.body_length, self.body_width, self.body_height = [float(i) for i in body_whl.split("x")]
        except ValueError:
            self.body_length, self.body_width, self.body_height = (.0, .0, .0)

    def get_body_volume(self):

        return float(self.body_length) * float(self.body_width) * float(self.body_height)

    @classmethod
    def from_tuple(cls, row):
        return cls(row[cls.ix_brand],
                   row[cls.ix_photo_file_name],
                   row[cls.ix_carrying],
                   row[cls.ix_body_whl])


class SpecMachine(CarBase):
    car_type = "spec_machine"

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

    @classmethod
    def from_tuple(cls, row):
        return cls(row[cls.ix_brand],
                   row[cls.ix_photo_file_name],
                   row[cls.ix_carrying],
                   row[cls.ix_extra])


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        create_strategy = {car_class.car_type: car_class for car_class in (Car, Truck, SpecMachine)}
        for row in reader:
            print(row)
            try:
                car_type = row[CarBase.ix_car_type]
            except IndexError:
                continue
            try:
                car_class = create_strategy[car_type]
            except KeyError:
                continue
            try:
                car_list.append(car_class.from_tuple(row).__dict__)
            except (ValueError, IndexError):
                pass
    return car_list


if __name__ == "__main__":
    print(get_car_list("coursera_week3_cars.csv"))
