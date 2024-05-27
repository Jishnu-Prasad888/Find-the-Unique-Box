boxes_balls = {}
i = 1
total_weight = 0
while i < 11:
    user_input = input("Enter 10 or 9 for the weight of the balls in the box_" + str(i) +":")
    if user_input== '9'or user_input=='10':
        boxes_balls['BOX = '+str(i)] = user_input
        total_weight = i*int(user_input) + total_weight
        i = i+1
    else:
        print("Please enter a either 10 or 9")
# print(total_weight)
assumed_weight = 550
weight_difference = assumed_weight - total_weight
if weight_difference != 0:
    print("The Box Number " + str(weight_difference) + " has balls with weight 9 grams each")
if weight_difference == 0:
    print("All the boxes have balls weighing 10 grams")
