"""A full list of apps."""
import json

with open('database.json', 'r', encoding="UTF-8") as file:
    tools = json.load(file)["tools"]
with open('database.json', 'r', encoding="UTF-8") as file:
    batteries = json.load(file)["batteries"]
with open('database.json', 'r', encoding="UTF-8") as file:
    chargers = json.load(file)["chargers"]

class Tool():
    """Class used to describe a tool with all important parameters"""
    catalog_id: str
    use: str
    brushless: bool
    owned: bool
    high_power: bool
    wanted: bool
    price: int

class Battery():
    """Class used to describe a battery with all important parameters"""
    catalog_id: str
    capacity: float
    owned: bool
    high_power: bool
    high_energy: bool
    wanted: bool
    price: int

class Charger():
    """Class used to describe a charger with all important parameters"""
    catalog_id: str
    power: float
    owned: bool
    ports_count: bool
    wanted: bool
    price: int

def missing_items():
    """Function returning any items that are wanted but not owned"""
    list_missing_items = []
    for tool in tools:
        if tool['wanted']:
            if not tool['owned']:
                tool_id = (tool['catalog_id'])
                list_missing_items.append(tool_id)
    for battery in batteries:
        if battery['wanted']:
            if not battery['owned']:
                tool_id  = (battery['catalog_id'])
                list_missing_items.append(tool_id)
    for charger in chargers:
        if charger['wanted']:
            if not charger['owned']:
                tool_id  = (charger['catalog_id'])
                list_missing_items.append(tool_id)
    print(f"Oto numery katalogowe wszystkich przedmiotów które trzeba dokupić {list_missing_items}")

def missing_tools():
    '''Function designed to return not owned but wanted Ryobi tools.'''
    missing_tools_list = []
    for tool in tools:
        if tool['wanted']:
            if not tool['owned']:
                missing_tools_list.append(tool['catalog_id'])
    print(f'Oto numery katalogowe narzędzi które trzeba dokupić: {missing_tools_list}' )

def battery_charge_time():
    """Function designed to count charge time with any owned charger"""
    id_battery = input("Proszę podaj numer katalogowy baterii. \
        Nie podawaj nic aby zobaczyć pełną listę")
    for battery in batteries:
        if id_battery in battery["catalog_id"]:
            for charger in chargers:
                time_needed = (battery["capacity"]) * (charger["power"])
                name_charger = charger["catalog_id"]
                name_battery = battery["catalog_id"]
                print(f"Czas potrzebny na naładowanie akumulatora {name_battery} to: {time_needed},\
                na ładowarce {name_charger}")
def toolbox():
    """Function used to return inventory in my toolbox"""
    #tools
    owned_tools = []
    for tool in tools:
        if tool["owned"]:
            owned_tools.append(tool["catalog_id"])
    # nieudana próba skrócenia owned_tools.append((t["catalog_id"]) for t in tools if t["owned"])
    #batteries
    owned_batteries = []
    for battery in batteries:
        if battery["owned"]:
            owned_batteries.append(battery["catalog_id"])
    #chargers
    owned_chargers = []
    for charger in chargers:
        if charger["owned"]:
            owned_chargers.append(charger["catalog_id"])
    print(f"Oto lista posiadanych narzędzi:\nNarzędzia: {owned_tools}\n\
Baterie: {owned_batteries}\nŁadowarki: {owned_chargers}")

def tool_appending(tool: Tool):
    """NOT WORKING Function designed to append a new tool into the database"""
    new_tool = {
        "catalog_id": tool.catalog_id,
        "use": tool.use,
        "brushless": tool.brushless,
        "owned": tool.owned,
        "high_power": tool.high_power,
        "wanted": tool.wanted,
        "price": tool.price
    }
    tools.append(new_tool)
    with open('database.json', 'w', encoding="UTF-8") as new_file:
        json.dump(tools, new_file)

def value():
    """Function used to print a full value of owned tools"""
    sum_value = 0
    for tool in tools:
        if tool["owned"]:
            sum_value += tool["price"]
    for battery in batteries:
        if battery["owned"]:
            sum_value += battery["price"]
    for charger in chargers:
        if charger["owned"]:
            sum_value += charger["price"]
    print(f"Sumaryczna wartość posiadanych produktów Ryobi to {sum_value} złotych")

def money_buy():
    """function returning money needed to buy all tools which are not owned but wanded."""
    sum_value = 0
    for tool in tools:
        if not tool["owned"]:
            if tool["wanted"]:
                sum_value += tool["price"]
    for battery in batteries:
        if not battery["owned"]:
            if battery["wanted"]:
                sum_value += battery["price"]
    for charger in chargers:
        if not charger["owned"]:
            if charger["wanted"]:
                sum_value += charger["price"]
    print(f"Sumaryczna wartość produktów Ryobi, które trzeba dokupić to {sum_value} złotych")
