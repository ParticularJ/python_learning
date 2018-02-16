# create a mapping of state to abbreviation(缩写)
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-'*10)
print("NY State has:", cities['NY'])
print("OR State has:", cities['OR'])

print('-'*10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('-'*10)
# item 包含字典的key和value
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-'*10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}.")

print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}.")

print('-'*10)
# safely get a abbreviation by state that might not be there
# get（1，2） if 1 在字典则返回对应的值，否则返回2 
state = states.get('Texas',"not in")

#if not state:
print(f"Sorry, no Texas {state}.")

city = cities.get("TX", 'Does Not Exist.')
print(f"The city for the state 'TX' is : {city}.")
