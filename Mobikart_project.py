from datetime import date
#Mobikart_for_supermarkets
class Mobikart:
	def __init__(self,mart):
		self.mart=mart
		print("Welcome to Mobikart")
	#list of the items in mart
	def list(self):
		print("ITEMS               PRISE")#write this line in biling
		for i,j in self.mart.items():
			print(i," "*(20-len(i)),j)
	#Select the items
	def select(self,item):
		if item in self.mart:
			user[item]=self.mart.get(item)
			print(item,"-is added in your cart")
			print("Continue shoping")
		else:
			print("Item is not availabe")
			print("Please search other items")
	#show the selected items in cart
	def show(self):
		print("ITEMS               PRISE")#write this line in biling
		for i,j in user.items():
			print(i," "*(20-len(i)),j)
	#printing bill		
	def bill(self,name,num,Total,quan,date):
		print(" Name:",name,"\n","Number:",num," "*5,date)

		print("ITEMS               PRISE")
		print("-"*28)
		for i,j in user.items():
			Total=Total+j
			quan=quan+1
			print(i," "*(20-len(i)),j)
		print("-"*28)
		print("Quantity:",quan," "*2,"Total:",Total) #write this line in biling
		print("-"*28)
		print("   Thanks visit again")

#Input_values

dat=date.today()
mart={"rasampowder1kg":50,"chickenmasal100g":50,"biscuits":10,"juice":20,"spray":40}
user={}   
ob=Mobikart(mart)
name=input("Enter your name please")
num=int(input("Enter your phone number"))
while True:
	resp=input("options list=find the item in mart,s=select the items and add to cart,b=bill,e=Exit:-")
	if resp=="list":
		ob.list()
	elif resp=="s":
		item=input("Enter the item which you want")
		print("Select the show for see your cart")
		if item=="show":
			ob.show()
		else:
			ob.select(item)
		
	elif resp=="b":
		ob.bill(name,num,0,0,dat)
		break
	elif resp=="e":
		break
	else:
		print("please follow the instructions")


