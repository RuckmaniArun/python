#Grocery Bill splitter project

#List

shop_Items = {
    'Milk':30,
    'Sugar':15,
    'Lentils':20,
    'Rice':40,
    'Coffee':15,
    'Wheat':35
}
    
total_Items=len(shop_Items)

print(f"Total number of items in the shop : {total_Items}")
print(f"These are available items and price")
for item, price in shop_Items.items():
    print(item,":",price)
    

#Get customer items

Grocery_Bag={}
Populate_Bill=[]

Total_customer_Items=int(input("Get total items from customer"))
for i in range(Total_customer_Items):
    Customer_list=input("Scan the Grocery Bag..")
    weight=float(input("Add the weight..."))
    Grocery_Bag[Customer_list]=weight*shop_Items.get(Customer_list,0)
    print(Grocery_Bag)
    
    generate_bill=(
        Customer_list, 
        f"{weight}*{shop_Items.get(Customer_list,0)}",
        Grocery_Bag.get(Customer_list)
    )
        
    Populate_Bill.append(generate_bill)
   
Bill_amount=sum(Grocery_Bag.values())
print(f"Total bill amount : {Bill_amount}")

#Generate Receipt
print(f"Item,weight,price,payment")
print("----------------------------")
print(f"Customer Receipt : {Populate_Bill}")


 
