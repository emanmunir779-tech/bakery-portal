import os
recipesFile= "recipes.txt"

def initiatingFiles():
    try:
        if not os.path.exists(recipesFile):
            with open(recipesFile,'w') as f:
                f.write('FUDGE BROWNIES\n')
                f.write('Unsalted Butter, 200 ,30\n')
                f.write('Cocoa Powder, 100 ,12\n')
        print('TEXT FILES ARE READY!!')
    except Exception as e:
        print(f"INVALID ERROR..{e}")
initiatingFiles()



def userLogin():
    print("----PORTAL LOGIN----")
    attempts=0
    while attempts < 3:
        userName= input("USERNAME:").strip()
        passWord= input("PASSWORD:").strip()
        if userName== 'owner' and passWord== 'bakers1234':
            print('ACCESS GRANTED SUCESSFULLY.')
            return True
        attempts+=1
        print(f'INVALID USERNAME AND PASSWORD: {3-attempts} LEFT')
    return False



def recipeAdd():
    recipeName = input('Name of the Recipe:').strip()
    print("Enter Ingredient one by one. Type 'done' when finished.")
    with open(recipesFile,'a') as f:
            f.write(f'\n{recipeName}\n')
            while True:
                ingredientName = input('Name of Ingredient:').strip()
                if ingredientName.lower() == 'done':
                    break
                try:
                    grams= float(input("Enter the ingredient in grams:"))
                    price= float(input("Enter the price/grams:"))
                except Exception as e:
                        print(f'ERROR, please enter numbers only {e}')
                        continue
                f.write(f'{ingredientName},{grams},{price}\n')
    print('RECIPE HAS BEEN SAVED SUCCESSFULLY')



def viewRecipes():
    names=[]
    with open(recipesFile, "r") as f:
        for line in f:
            line = line.strip()
            if line and ',' not in line and line not in names:
                names.append(line)
        print("\nSAVED RECIPES")
        for n in names:
            print('-',n)



def costCalculate():
    aim= input("Recipe name that needs costing:").lower().strip()
    total= 0
    found= False
    currentName= None
    with open(recipesFile,'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                currentName = None
                continue
            if ',' not in line:
                currentName = line
                if currentName.lower()== aim:
                    print(f"\n---Cost of {currentName}---")
                    found= True
                continue
            if currentName is None or currentName.lower() != aim:
                continue
            parts = line.split(',')
            if len(parts) != 3:
                continue
            ingredientName, grams, price = parts
            cost= float(grams) * float(price)
            total += cost
            print(f"{ingredientName}:{cost:.2f}")
    if found:
        print(f"TOTAL COST: {total:.2f}")
    else:
        print("Recipe not found..")



def main():
    if not userLogin():
        return
    while True:
        print("\n1. Add recipe\n2. View recipe\n3. Calculate cost\n4. Exit")
        choice = input('SELECT CHOICE(1/2/3/4):')
        if choice == '1':
            recipeAdd()
        elif choice == '2':
            viewRecipes()
        elif choice =='3':
            costCalculate()
        elif choice == '4':
            print('Existing..')
            break 
        else:
            print("INVALID CHOICE")
main()
