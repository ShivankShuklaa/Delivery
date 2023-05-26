while True:
    def main():
        print("---------------------------------------------------- \n"
              "            Welcome to delivery charge calculator     \n"
              "-------------------------------------------------------")
        purchase_total()
    def purchase_total():
        while True:
            amount=float(input("Please enter purchase total:$ "))
            if amount>=150:
                break
            else:
                print("ERR: Sorry, purchase total need to be above $150.")
                x = input("Do you want to calculate delivery charges for another purchase? (y/n):")
                if x != 'y':
                    print("Thanks for using the delivery charges Calculator!\nSee you again!")
                    sys.exit()
        delivery_charges(amount)
    def delivery_charges(amount):
        items=int(input("Please enter number of the items:"))
        if items<=5:
            days = int(input("Please enter delivery day ([1] for 1st day and [2] for 2nd day): "))
            if days==1:
                charges = 8
                total_cost=amount+charges
                print(f'Delivery charges: ${charges} \nTotal cost: ${total_cost}')
            if days==2:
                charges = items*1.50
                total_cost = amount+charges
                print(f'Delivery charges: ${charges} \nTotal cost: ${total_cost}')
        elif items>=6:
            days = int(input("Please enter delivery day ([1] for 1st day and [2] for 2nd day): "))
            if days == 1:
                charges = items*2.50
                total_cost = amount + charges
                print(f'Delivery charges: ${charges} \nTotal cost: ${total_cost}')
            if days == 2:
                charges = items * 1.20
                total_cost = amount + charges
                print(f'Delivery charges: ${charges} \nTotal cost: ${total_cost}')


    main()
    x =input("Do you want to calculate delivery charges for another purchase? (y/n):")
    if x!='y':
        print("Thanks for using the delivery charges Calculator!\nSee you again!")
        sys.exit()