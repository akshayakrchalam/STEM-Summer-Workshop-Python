name_1 = input("Enter the name of the 1st ingredient: ")
amo_1 = int(input("Enter the amount needed for the 1st ingredient: "))
name_2 = input("Enter the name of the 2nd ingredient: ")
amo_2 = int(input("Enter the amount needed for the 2nd ingredient: "))
name_3 = input("Enter the name of the 3rd ingredient: ")
amo_3 = int(input("Enter the amount needed for the 3rd ingredient: "))

print("First add %d of %s, %d of %s, and %d of %s. Then mix well in the bowl." % (amo_1, name_1, amo_2, name_2, amo_3, name_3))

q_check = input("Press 'q' to quit or 'c' to change the recipe's amounts: ")
if q_check.lower() == 'q':
    print("Thank you for using the pantry recipe. Enjoy your treat!")
while q_check.lower() == 'c':
    change = input("Press 'h' to halve the recipe, 't' to triple it, or 'q' to quit: ")
    if change.lower() == 'h':
        half_1 = amo_1 / 2
        half_2 = amo_2 / 2
        half_3 = amo_3 / 2
        print("Now the recipe is halved. First add %f of %s, %f of %s, and %f of %s. Then mix well in the bowl." % (half_1, name_1, half_2, name_2, half_3, name_3))
    elif change.lower() == 't':
        trip_1 = amo_1 * 3
        trip_2 = amo_2 * 3
        trip_3 = amo_3 * 3
        print("Now the recipe is tripled. First add %f of %s, %f of %s, and %f of %s. Then mix well in the bowl." % (trip_1, name_1, trip_2, name_2, trip_3, name_3))
    else:
        print("Thank you for using the pantry recipe. Enjoy your treat!")
        break
