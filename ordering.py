class Menu_item:
     pass
class Order:
     def orderdisplay(self):
          pass
    #  def orderdetial(self):
    #       return f"Order Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
     
class Delivery:
    dict={}
    order={}
    def login(self):
         dusername=input('enter the Delivery user name : ')
         dpassword=input('enter the Delivery password :')
         if dusername==dusername and dpassword==dpassword:
              print('Delivery user logged in')
              Order.orderdetial(self)
              return True
         else:
              print('Delivery user not logged in')
              return False
    def signup(self):
         dusername = input('enter the Delivery user name : ')
         dpassword = input('enter the Delivery password :')
         dconfirm = input('confirm the Delivery password :')
         if dpassword == dconfirm:
              Delivery.dict[dusername] = dpassword
              print('Delivery user created')
              Order.orderdetial(self)
              return True
         else:
              print('Delivery user not created')
              return False
    def update_delivery_status(self):
              print("Delivery status updated")
              print("Order details:")
              print(Order.orderdetial())

    def order(self,item,price):
         self.order[item]=price
         
        