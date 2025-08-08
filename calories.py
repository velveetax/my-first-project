products = {
    "apple": 52,
    "banana": 89,
    "chicken": 165,
    "rice": 130,
    "egg": 155,
    "potato": 87,
    "poridge": 73
}
calories_sum = 0
max_c = float(input("What is your goal in calories today? "))
while True:
    name = input("Enter your product or exit: ")
    if name == "exit":
        break
    if name not in products:
        print("Sorry, we don't have such product in our base yet :(")
        continue
    weight = float(input("How many grammes? "))
    calories_100g = products[name]
    calories = calories_100g * weight / 100
    calories_sum += calories
    calories_left = max_c - calories_sum
    if calories_left > 0:
        print(f"You still have {calories_left:.1f} calories left! Keep going!")
    elif calories_left == 0:
        print("You got it!")
    else:
        print(f"Oops, surplus! You ate {-calories_left:.1f} calories more.")
    print(f"You added {calories:.1f} calories. In all: {calories_sum:.1f}/{max_c}")