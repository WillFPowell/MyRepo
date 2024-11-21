## William Felitti-Powell

def sum_of_list(numbers):
    """
    This function takes a list of numbers as input and returns the sum of all the numbers in the list.
    Parameters:
    numbers (list): A list of integers or floats.
    Returns:
    int: The sum of all the numbers in the list.
    """
    return sum(numbers)

def describe_person(name, age, city="Unknown"):
    """
    This function takes a person's name, age, and optionally a city, and returns a descriptive string.
    Parameters:
    name (str): The name of the person.
    age (int): The age of the person.
    city (str): The city where the person lives (optional, defaults to "Unknown").
    Returns:
    str: A string describing the person.
    """
    return f"{name} is {age} years old and lives in {city}."

# Here is wehre i call the fucntions 

if __name__ == "__main__":
    # Example list to pass to the sum_of_list function
    numbers = [1, 2, 3, 4, 5]
    total = sum_of_list(numbers)
    print(f"The sum of the list is: {total}")

    # Example of calling describe_person function
    person_description = describe_person("Alice", 30, "New York")
    print(person_description)
    
    # Calling describe_person with only name and age, it will say unknown since there is no city in the function
    person_description_no_city = describe_person("Bob", 25)
    print(person_description_no_city)