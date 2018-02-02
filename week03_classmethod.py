from datetime import date


def extract_description(user_string):
    return "открытие чемпионата мира по футболу"


def extract_date(user_string):
    return date(2018, 6, 14)


class Event:
    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return "Event \"{}\" at {}".format(self.description, self.date)

    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        event_date = extract_date(user_input)
        return cls(description, event_date)


event = Event.from_string("добавить в мой календарь открытие чемпионата мира по футболу на 14 июня 2018 года")
print(event)

print(Event("event", "today"))
