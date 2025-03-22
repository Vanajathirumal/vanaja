# #############################################################################################
# student marklist
# class Std:
#     def getdata(self):
#         no_std=int(input('enter the number of student :'))
#         students={}
#         for _ in range(no_std):
#             Name=input('enter the Student name:')
#             students[Name] ={}
#             Roll=int(input('enter the Roll number:'))
#             students[Name]['Roll']=Roll
#             Age=int(input('enter the Age:'))
#             students[Name]['Age']=Age
#             eng=int(input('enter the English mark :'))
#             students[Name]['English']=eng
#             math=int(input('enter the Math mark :'))
#             students[Name]['Math']=math
#             sci=int(input('enter the science mark :'))
#             students[Name]['Science']=sci
#             social=int(input('enter the social mark :'))
#             students[Name]['Social']=social
#         self.report(students)
#     def grade_calculate(self,mark):
#         if mark >= 300:
#             return 'A'
#         elif mark >= 200:
#             return 'B'
#         elif mark >= 100:
#             return 'C'
#         else:
#             return 'D'

#     def marks(self,eng,math,sci,social):
#         mark= eng+math+sci+social
#         return mark
        

#     def report(self,students):
#         """Prints a report of the students' grades."""
#         for student in students:
#             data=students[student]
#             print(f"Name: {student}")
#             print(f"Roll: {data['Roll']}")
#             print(f"Age: {data['Age']}")
#             print(f"eng:{data['English']}")
#             print(f"math:{data['Math']}")
#             print(f"sci:{data['Science']}")
#             print(f"social:{data['Social']}")
        
#             total_marks = self.marks(data["English"], data["Math"], data["Science"], data["Social"])
#         print(f"Total Marks: {total_marks}")
#         print(f"Grade: {self.grade_calculate(total_marks)}")

# std1=Std()    
# std1.getdata()

# #############################################################################################

train tickek booking system
class Train:
    def __init__(self, total_seats=10):
        self.seats={seat_num:None for seat_num in range(total_seats+1)} 
    
    def display_tickek(self):
        print('Train seat status')
        for seat,passenger in self.seats.items():
            if passenger :
                print(f'{seat} is reserved')
            else:
                print(f'{seat} is available')
    
    def book_ticket(self,seat_num,passanger_name):
        if seat_num not in self.seats:
            print('the seat number is invalid')
        elif self.seats[seat_num] is not None:
            print('it was reserverd by some person choose other slots')
        else:
            self.seats[seat_num]=passanger_name
            print(f'{seat_num} is succsefuly booked by {passanger_name} ')
    
    def booking_status(self,passanger_name):
        for seat,passanger in self.seats.items():
            if passanger== passanger_name:
                print(f'{passanger_name} , your seat number is {seat}')
        else:
            print(f"❌ No booking found for {passanger_name}.")
    def cancel_ticket(self,passanger_name):
        for seat,passanger in self.seats.items():
            if passanger== passanger_name:
                self.seats[seat]=None
                print(f'{passanger_name} , your seat number is {seat} is canceled')
            

t1=Train(total_seats=11)
t1.book_ticket(2,'vanaja')
t1.booking_status('vanaja')
t1.display_tickek()
t1.cancel_ticket('vanaja')

# #############################################################################################
# cinema tickect book
# class Cinema():
#     def __init__(self, total_seats=10):
#         self.seats = {seat_num: None for seat_num in range(total_seats +1)}
# from abc import ABC ,abstractmethod
# class Vehicle(ABC):
#     def __init__(self,vechicle_id,model,rent_rate):
#         self.vechicle_id=vechicle_id
#         self.model=model
#         self.rent_rate=rent_rate
        
#     @abstractmethod
#     def rent():
#         pass
#     @abstractmethod
#     def return_vehicle():
#         pass

# class Car(Vehicle):
#     def rent(self):

      
#     def return_vehicle(self):  
#         pass
    
# class Bike(Vehicle):
#     def rent(self):
#         pass
#     def return_vehicle(self):  
#         pass
# class Truck(Vehicle):
#     def rent(self):
#         pass
#     def return_vehicle(self):  
#         pass

        


            
                







    
    





    