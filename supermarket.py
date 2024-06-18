import market
def main():
    try:
        print("*GJ super market*")
        want_to_purchase=input(("Do you want to purchase:"))
        if want_to_purchase=="yes":
            print("*Welcome to GJ super market*")
            customer=input("Tell your purchase section:")
            if customer=="grain_oils":
               market.grain_oils()
            if customer=="daily_essential":
                market.daily_essential()
        else:
            print("Thank you for visiting!!")
    except:
        print("choose avaliable item in super market")
main()
