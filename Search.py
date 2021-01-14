import csv
from py_edamam import PyEdamam, Edamam


def my_func(k):  
    return k['calories']


field_names_food = ['label', 'category', 'quantity', 'nutrients', 'images']  
field_names_recipe = ['label', 'link', 'ingredients', 'totalTime', 'yields', 'totalNutrients', 'calories', 'totalDaily',
                      'totalWeight', 'healthLabels', 'dietLabels', 'cautions']  
data_dict = []  

def run():
    e = PyEdamam(recipes_appid='x',
                 recipes_appkey='x',
                 food_appid='x',
                 food_appkey='x')
    f = Edamam(nutrition_appid='x',
               nutrition_appkey='x')
    print(
        ">>> MENU <<<\nChoose a method for searching\n1.Food Search\n2.Recipe Search\n3.Nutrition Analysis")
    option = input('Enter a method number: ')  
    if option == '1':  
        name = input('Enter a food name: ')
        foods = e.search_food(name)
        for food in foods:
            print("Name: ", food.label)
            print("Category: ", food.category)
            print("Quantity: ", food.quantity)
            print("Nutrients: ", food.nutrients)
            print("Image: ", food.image)
            print(" ")
            data_dict.append({'label': food.label, 'category': food.category, 'quantity': food.quantity,
                              'nutrients': food.nutrients, 'images': food.image})
        if len(data_dict) == 0:
            print("Data not found.")
        else:
            choice = input("Store value?(Y/N): ")
            if choice == "Y" or choice == "y":  
                with open('food.csv', 'w+') as csv_file:
                    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names_food)
                    spreadsheet.writeheader()
                    spreadsheet.writerows(data_dict)
                print("Data stored.")
    elif option == '2':  
        name = input('Enter a recipe/ingredient name: ')
        health_label = input("Enter health label: ")
        diet_label = input("Enter diet label: ")
        calories = input("Enter maximum calories(in kCal): ")
        recipes = e.search_recipe(name)
        for recipe in recipes:
            if (health_label in recipe.healthLabels) or health_label == "":  
                if (diet_label in recipe.dietLabels) or diet_label == "":  
                    if calories == "" or (int(calories) >= int(recipe.calories)):  
                        print("Name: ", recipe.label)
                        print("Link: ", recipe.url)
                        print("Ingredients: ", recipe.ingredient_names)
                        print("Total prep time: ", recipe.totalTime)
                        print("Yields: ", recipe.yields)
                        print("Total nutrients: ", recipe.totalNutrients)
                        print("Calories: ", recipe.calories)
                        print("Total daily: ", recipe.totalDaily)
                        print("Total weight: ", recipe.totalWeight)
                        print("Health Labels: ", recipe.healthLabels)
                        print("Diet Labels: ", recipe.dietLabels)
                        print("Cautions: ", recipe.cautions)
                        print(" ")
                        data_dict.append(
                            {'label': recipe.label, 'link': recipe.url, 'ingredients': recipe.ingredient_names,
                             'totalTime': recipe.totalTime, 'yields': recipe.yields,
                             'totalNutrients': recipe.totalNutrients, 'calories': recipe.calories,
                             'totalDaily': recipe.totalDaily,
                             'totalWeight': recipe.totalWeight,
                             'healthLabels': recipe.healthLabels,
                             'dietLabels': recipe.dietLabels, 'cautions': recipe.cautions})
        if len(data_dict) == 0:
            print("Data not found.")
        else:
            data_dict.sort(key=my_func)  
            choice = input("Store value?(Y/N): ")
            if choice == "Y" or choice == "y":  
                with open('recipe.csv', 'w+') as csv_file:
                    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names_recipe)
                    spreadsheet.writeheader()
                    spreadsheet.writerows(data_dict)
                print("Data stored.")
    elif option == "3":  
        items = input("Enter items for calculating nutrient value: ")
        result = f.search_nutrient(items)
        print(result)


run()
