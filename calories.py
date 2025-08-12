products = {
    "apple": 52,
    "banana": 89,
    "chicken": 165,
    "rice": 130,
    "egg": 155,
    "potato": 87,
    "poridge": 73
}
print(f"Here is our product list: {products}")
calories_sum = 0
max_c = float(input("What is your goal in calories today? "))
while True:
    name = input("Enter your product or 'exit' to add a new one: ").lower()
    if name == "exit":
        new_product = input("Do you want to add your product? Answer yes or no. ").lower()
        if new_product == "no":
            print("Okay!")
            break
        elif new_product == "yes":
            product_enter = input("Enter your product. ").lower()
            calories_100g = float(input("How much calories does it have in 100g? "))
            products[product_enter] = calories_100g
            print(f"New list: {products}")
    else:
        calories_100g = products[name]
    weight = float(input("How many grammes did you eat? "))
    calories = calories_100g * weight / 100
    calories_sum += calories
    calories_left = max_c - calories_sum
    print(f"You added {calories:.1f} calories. In all: {calories_sum:.1f}/{max_c}")
    if calories_left > 0:
        print(f"You still have {calories_left:.1f} calories left! Keep going!")
    elif calories_left == 0:
        print("You got it!")
    else:
        print(f"Oops, surplus! You ate {-calories_left:.1f} calories more.")
        break
    info = input("Do you want to exit? Answer yes or no. ").lower()
    if info == "no":
        print("Okay! Let's continue!")
    elif info == "yes":
        print("Bye!")
        break
    else:
        print("I don't understand.")
        break