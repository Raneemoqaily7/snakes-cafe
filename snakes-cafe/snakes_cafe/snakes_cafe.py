from collections import Counter
print(""" **************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears """)
item = input("""
***********************************
** What would you like to order? **
***********************************\n>""" )

print(f' 1 order of {item} have been added to your meal')
list=[]
list.append(item)




 
count=1
 
while True:
      
    item =input (" What would you like to order? \n > ")
    if item =="quit":
        print("Your order of {list} have been added to your meal")
        break
    else:
      list.append(item)
      
      for i in list:
        count+=1
        break
      print(f' {count } order of {list} have been added to your meal')
          
   
 
      
      



#       item =input (" What would you like to order? \n > ")
# list=[]
# list.append(item)
# print (f' 1 order of {item} have been added to your meal')

# # def meal (item):
# count=1 
# if item =="quite":
     
#      exit
# elif item!="quite":
#   while item =="quite":
#       break
#   else:
#       item =input (" What would you like to order? \n > ")
#       list.append(item)
      
#       if item in list:
#        count+=1
#       else:
#        count=1
        
      
#       print(f' {count } order of {item} have been added to your meal')
  
      
      

# meal(item)







