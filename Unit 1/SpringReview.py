def discount():
    itemPrice = int(input("please enter the item price."))
    if itemPrice >= 50 or itemPrice <=75;
        discount = .15
        sum = itemPrice * discoun
        total = itemPrice - sum
        print("this is your final total" + str(total))
    elif itemPrice >75:
        discount = .25
        sum = itemPrice * discount
        total = itemPrice - sum
        print("this is your final total"+ str(total))
    else:
        print("sorry, you do not get a discount.")

discount()