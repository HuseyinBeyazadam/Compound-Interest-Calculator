def calculator(money, percentage, data_time):

    x = percentage / 100 + 1

    for i in range(data_time):
        money2 = money * x
        money = money2


        print(f"{i + 1}. ----> {money2}")
        print()

    
    return money