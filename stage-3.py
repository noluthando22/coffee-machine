# Write your code here
water = int(input())
milk = int(input())
beans = int(input())
no_of_cups = int(input())
min_cup = min(water // 200, milk // 50, beans // 15)
if no_of_cups == min_cup:
    print("Yes, I can make that amount of coffee")
elif no_of_cups < min_cup:
    print("Yes, I can make that amount of coffee (and even ", min_cup - no_of_cups, "more than that)")
elif no_of_cups > min_cup:
    print("No, I can make only", min_cup, "cups of coffee")

