# class human:
#     eye=2
#     hand=2
#     fingers=10
#     def __init__(self):
# #          print("welcome to human class")
# #     def love(self,per:float):
# #         print("percentage of love is :",per)
# #     def temper(self,per:float):
# #         print("percentage of temper is :",per)

# # vanaja=human()
# # print(vanaja.eye)
# # print(vanaja.love(78.90))
# # print(human.temper(vanaja,55))
# # print(human.fingers)


class bicycle:
    wheels=2
    handbreak=1
    bell=1
    def __init__(self):
         print("welcome to bicycle class")
    def color(self,color:str):
        print(f"{color}  color bicycle")
    def speed(self,speed):
        print(f"{speed} km speed of bicycle")
ladybird=bicycle()
print(ladybird.color("pink"))


# encapsulation
class Shawarma:
    wrap="rumalti rothi"
    vegies=["cabbage","capsicum","carrot","onoion"]
    _chiken_quality="not bad"
    __masala=["x","y","z"]

    def process(self):
        print("finaly chapp grilled chiken withspecial masala and veggies,wraped")
    
    def get_masala(self):
        return Shawarma.__masala
    
    def set_masala(self,value):
        Shawarma.__masala = value

plate1=Shawarma()
print(plate1.set_masala("dfd"))
print(plate1.__masala)