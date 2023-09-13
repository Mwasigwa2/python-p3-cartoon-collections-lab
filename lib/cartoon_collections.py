# roll_call_dwarves
def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, start=1):
        print(f"{i}. {dwarf}")

# summon_captain_planet
def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + "!" for call in planeteer_calls]

# long_planeteer_calls
def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

# find_the_cheese
def find_the_cheese(ingredients):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for ingredient in ingredients:
        if ingredient in cheese_types:
            return ingredient
    return None
