import csv
from py_edamam import PyEdamam, Edamam


def my_func(k):  # Function that returns calories for each ingredient to the sorting function
    return k['calories']


field_names_food = ['label', 'category', 'quantity', 'nutrients', 'images']  # list field for food
field_names_recipe = ['label', 'link', 'ingredients', 'totalTime', 'yields', 'totalNutrients', 'calories', 'totalDaily',
                      'totalWeight', 'healthLabels', 'dietLabels', 'cautions']  # list field for recipe
data_dict = []  # list for storing data later to be written on a file


def run():
    # object created with app_id and app_key fetched from https://developer.edamam.com/
    e = PyEdamam(recipes_appid='cd41d476',
                 recipes_appkey='91fc7360ff3012549b416af21df4dfcd',
                 food_appid='73cafc31',
                 food_appkey='5680e3abbaa82d57b48d172f156695d1')
    f = Edamam(nutrition_appid='0ff06c93',
               nutrition_appkey='23a10903d1d71d94a4f0bf5ae26cebac')
    print(
        ">>> MENU <<<\nChoose a method for searching\n1.Food Search\n2.Recipe Search\n3.Nutrition Analysis")
    option = input('Enter a method number: ')  # menu
    if option == '1':  # for food search
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
            if choice == "Y" or choice == "y":  # Write values on a file
                with open('food.csv', 'w+') as csv_file:
                    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names_food)
                    spreadsheet.writeheader()
                    spreadsheet.writerows(data_dict)
                print("Data stored.")
    elif option == '2':  # for recipe search
        name = input('Enter a recipe/ingredient name: ')
        health_label = input("Enter health label: ")
        diet_label = input("Enter diet label: ")
        calories = input("Enter maximum calories(in kCal): ")
        recipes = e.search_recipe(name)
        for recipe in recipes:
            if (health_label in recipe.healthLabels) or health_label == "":  # search by health label
                if (diet_label in recipe.dietLabels) or diet_label == "":  # search by diet label
                    if calories == "" or (int(calories) >= int(recipe.calories)):  # search by calories
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
            data_dict.sort(key=my_func)  # sorting the recipes in ascending order based on the calories
            choice = input("Store value?(Y/N): ")
            if choice == "Y" or choice == "y":  # writing values to a file
                with open('recipe.csv', 'w+') as csv_file:
                    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names_recipe)
                    spreadsheet.writeheader()
                    spreadsheet.writerows(data_dict)
                print("Data stored.")
    elif option == "3":  # for nutrition analysis
        items = input("Enter items for calculating nutrient value: ")
        result = f.search_nutrient(items)
        print(result)


run()
