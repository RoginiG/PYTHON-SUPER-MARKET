import smtplib
import random
def grain_oils():
    grain_oils=["sugar","turdhal","pasta","cocountoil","oliveoil","vegetable oil"]
    grain_oils_net_price={'sugar':500,'turdhal':250,'pasta':345,'cocountoil':560,'oliveoil':720,'vegetableoil':959}
    grain_oils_original_price={'sugar':400,'turdhal':150,'pasta':245,'cocountoil':300,'oliveoil':400,'vegetableoil':800}
    shopping_item1=input("which item do you want do purchase:")
    cost_netprice=grain_oils_net_price[shopping_item1]
    cost_orginalprice=grain_oils_original_price[shopping_item1]
    import re
    f=open("item_database1.txt","r")
    txt=f.read()
    print(txt)
    available=re.search(shopping_item1,txt)
    print("your item is available")
    quantity=int(input("how much quanity do you want? "))
    print("The bill")
    import datetime
    bill_date=datetime.datetime.now()
    print(bill_date)
    price=cost_netprice*quantity
    print(price)
    print(f"The cost of {shopping_item1}: {price}")
    Gst_price=cost_netprice-cost_orginalprice
    print(f"The Gst cost: {Gst_price}")
    f=open("bill1.txt","w")
    f.write(f"The bill for {shopping_item1} is {price} ")
    def email_sendings():
        try:
          receiver1_mails=["yuvaraja2167@gmail.com"]
          for i in receiver1_mails:
            bill1=cost_netprice
            print(i,bill1)
            s=smtplib.SMTP("smtp.gmail.com",587)
            s.starttls()
            s.login("rogini263@gmail.com","bkad bbja xger njmq")
            message=f"you purchasing item  {shopping_item1}  with quantity of {quantity} the total price is {price} Thank you for visiting come again!"
            s.sendmail("rogini263@gmail.com",i,message)
            s.quit()
            print("mail sends sucessfully")
        except:
           print("mail not sending")
    email_sendings()
    import supermarket
    supermarket.main()
def daily_essential():
    daily_essential=["boost","vim","sunrise","bread","horlicks","soap"]
    daily_essential_net_price={'boost':500,'vim':50,'sunrise':100,'bread':100,'horlicks':500,'soap':230,}
    daily_essential_orginal_price={'boost':300,'vim':30,'sunrise':80,'bread':90,'horlicks':400,'soap':130,}
    shopping_item2=input("which item you want do purchase:")
    cost_Netprice=daily_essential_net_price[shopping_item2]
    cost_Orginalprice=daily_essential_orginal_price[shopping_item2]
    import re
    f=open("item_database2.txt","r")
    txt=f.read()
    print(txt)
    available=re.search(shopping_item2,txt)
    print("your item is available")
    quantity=int(input("how much quanity you want? "))
    print("The bill")
    import datetime
    bill_date=datetime.datetime.now()
    print(bill_date)
    prices=cost_Netprice*quantity
    print(f"The cost of {shopping_item2} is {prices}")
    GST_price=cost_Netprice-cost_Orginalprice
    print(f"The Gst cost is {GST_price}")
    f=open("bill2.txt","w")
    f.write(f"The bill for {shopping_item2} is {prices} ")
    import smtplib
    import random
    def email_sending():
       try:
         receiver_mails=["yuvaraja2167@gmail.com"]
         for i in receiver_mails:
            bill=cost_Netprice
            print(i,bill)
            s=smtplib.SMTP("smtp.gmail.com",587)
            s.starttls()
            s.login("rogini263@gmail.com","bkad bbja xger njmq")
            message=f"you purchasing item {shopping_item2}  with the quantity of {quantity} the price is {prices} Thank you for visiting come again"
            s.sendmail("rogini263@gmail.com",i,message)
            s.quit()
            print("mail sends sucessfully")
       except:
           print("mail not sending")
    email_sending()
    import supermarket
    supermarket.main()
