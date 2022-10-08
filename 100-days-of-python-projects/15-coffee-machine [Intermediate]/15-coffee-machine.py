MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cost": 0
}

def check_resources( details, initial):
    if initial["water"]>=details["ingredients"]["water"] and initial["milk"]>=details["ingredients"]["milk"] and initial["coffee"]>=details["ingredients"]["coffee"]:
        return True
    
def process_coins():
    quarters_value = 0.25
    dimes_value = 0.1
    nickles_value = 0.05
    pennies_value = 0.01
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickles = int(input("How many nickles? : "))
    pennies = int(input("How many pennies? : "))
    total = quarters*quarters_value + dimes*dimes_value + nickles*nickles_value + pennies*pennies_value
    return total
    
    
def check_transaction(total, itemCost):
    if total<itemCost["cost"]:
        return False
    else:
        return True

def check_change(total, itemCost):
    if total>itemCost["cost"]:
        return round(total-itemCost["cost"], 2)
    elif total == itemCost["cost"]:
        return 'null'
    

def make_coffee(item, resource):
    resource["water"] -= item["ingredients"]["water"]
    resource["milk"] -= item["ingredients"]["milk"]
    resource["coffee"] -= item["ingredients"]["coffee"]
    resource["cost"] += item["cost"]
    
    
def no_resources(details, initial):
    if initial["water"]<details["ingredients"]["water"]:
        return "Sorry there is not enough water. "    
        
    if initial["milk"]<details["ingredients"]["milk"]:
        return "Sorry there is not enough milk. "    
        
    if initial["coffee"]<details["ingredients"]["coffee"]:
        return "Sorry there is not enough coffee. "
        
    
while True:
    #1. prompt user
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    #2. turn off if prompt is 'off'
    if prompt=="off":
        break
    #3. print report, available quantity in resources
    elif prompt== "report":
        print(resources)
    #4. check resources function to compare resources and requinitialed resources for prompted coffee
    elif prompt =="espresso" or prompt =="latte" or prompt =="cappuccino":
        
        if check_resources(MENU.get(prompt), resources):
            print("level1")
            total_cost = process_coins()
            if check_transaction(total_cost, MENU.get(prompt)):
                change = check_change(total_cost, MENU.get(prompt))
                if change == 'null':
                    make_coffee(MENU.get(prompt), resources)
                    print(f"Here's your {prompt}! ")
                else:
                    print(f"Here is ${change} dollars in change.")
                    make_coffee(MENU.get(prompt), resources)
                    print(f"Here's your {prompt}! ")       
            else:
                print("Sorry that's not enough money. Money refunded")       
        else:
            print(no_resources(MENU.get(prompt), resources))
            
            
    
    

#5. Process coins function to calculate coins and return total cost
#6. check transaction function if requinitialed total amount is given, if not say sorry and return, or given, deduct
#7. Make coffee and deduct ingredients rom resources