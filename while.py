# # Looping throuth th Sandwich
#
# sandwitch_orders = ["Egg Sandwitch","Chicken Sandwitch","Grilled Sandwich","Ham Sandwotch","Seafood Sandwich"]
#
# finished_sandwiches = []
#
# while sandwitch_orders:
#     current_sandwich = sandwitch_orders.pop()
#     print(f"I made your {current_sandwich}")
#     finished_sandwiches.append(current_sandwich)
#
# print("Sandwiches that are made :",finished_sandwiches)

# No Pastami Sandwich

sandwitch_orders = ["Egg Sandwitch","Chicken Sandwitch","Grilled Sandwich","Ham Sandwotch","Seafood Sandwich"]
sandwitch_orders.insert(0,"pastami")
sandwitch_orders[2] = "pastami"
sandwitch_orders.append("pastami")
finished_sandwiches = []

print("\n Updated Sandwitch Orders are :",sandwitch_orders)


while sandwitch_orders:
    current_sandwich = sandwitch_orders.pop()

    if current_sandwich == "pastami":
        del current_sandwich
    else:
        finished_sandwiches.append(current_sandwich)

finished_sandwiches.reverse()
print("\n Finished Sand",finished_sandwiches)