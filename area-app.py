"""
>> simple Area App python program do the following

-The user is asked for an area type
-if  't' for triangle ,'r' for rectangle , 'c' for Circle ,'s' for Square
-user can choise , 1 : For Try Again , 2 : For Exit From App
-problems will be triangle , rectangle , Circle and Square
"""


def area(strin,x,y=0):
    # triangle = (0.5 * base * height) where base = x , height = y
    if (strin=='t'):
        return (0.5*x*y)
    #rectangle = (width * height) width =x ,height =y
    elif (strin=='r'):
        return (x*y)
    # Circle= (PI * radius ^ 2)
    elif (strin=='c'):  
        return (3.14*x**2)
    elif (strin=='s'):
        return (x**2)
    
		
def app():
   try:
      strin= input("Please Choise the correct letter :  \n't' : For Triangle\n'r' : For Rectangle \n'c' : For Circle \n's' : For Square \n\t :")
      if (strin=='t'):
         base=eval(input("enter base :")) 
         height=eval(input("enter height :"))
         print("The Area of Triangle Equil : ",area(strin,base,height))

         #rectangle = (width * height) width =x ,height =y
      elif (strin=='r'):
         width=eval(input("enter width :")) 
         height=eval(input("enter height :"))
         print("The Area of Rectangle Equil : ",area(strin,width,height))
      elif (strin=='c'): 
          # Circle= (PI * radius ^ 2)
         radius=eval(input("enter Circle radius : "))
         print("The Area of Circle Equil : ",area(strin,radius))
      elif (strin=='s'): 
         # Circle= (PI * radius ^ 2)
          side=eval(input("enter Square side : "))
          print("The Area of Square Equil : ",area(strin,side))

      else:
          print("please enter what area that you want")
          app()
   except EOFError as e:
      print(end="")

choise=1
while(choise==1):
    app()
    choise=eval(input("Choise Number :- \n1 : For Try Again \n2 : For Exit From App \nChoise : "))
    if(choise==2):
        break
    elif(choise!=1 | choise!=2):
        print("Please Choise the correct Number ")
        choise=eval(input("Choise Number :- \n1 : For Try Again \n2 : For Exit From App \nChoise : "))

 
