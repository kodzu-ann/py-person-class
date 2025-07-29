class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    new_person_list = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        new_person_list.append(new_person)

    for person in people:
        current = Person.people[person["name"]]

        if "wife" in person and person["wife"] in Person.people:
            current.wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"] in Person.people:
            current.husband = Person.people[person["husband"]]

    return new_person_list
