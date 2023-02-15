# list
amazon_cart= ["notebooks","sunglass","toys","kitchen set","smartphones","earphones","charger"]
print(amazon_cart)
amazon_cart[0] = "laptop"
print(amazon_cart) # it will add the laptop in first position
amazon_cart[3]= "clothes" # it will add clohes in fourth position
print(amazon_cart)

basket=[1,2,3,4,5,6]
new_basket= basket.append(100)
print(basket)
print(new_basket) # it will show none because we didn't make new file we just append the old file
basket.append(45)

new_basket=basket
print(new_basket)
print(basket)
new_basket.append(52)
print(new_basket)
basket.insert(4,500)
print(basket) # by using (insert) we can add products or items anywhere in list

new_basket.extend([200])
print(new_basket) # we can extend through this

# removing
basket.pop(0)
print(basket) # it will remove first item from list

# to find length of list or to check how long is the list:-
print(len(basket))
# clear
new_basket.clear()
print(new_basket) # it will remove all the items from list and shows a empty list

alphabates= ["A","B","C","D","E","G","H","Z","V","R","W","A"]
print("y" in alphabates)# to check that something is in list or not
print("Z" in alphabates)
print("z" in alphabates) # it will show false because it is small letter

print(alphabates.count("A")) # how many times a item or a product in list
alphabates.sort()
print(alphabates) # for arraging

alphabates.reverse()
print(alphabates) # to reverse them

print(list(range(1,20))) # 1 to 100 counting in list
print(list(range(20))) # 0 to 100 counting

# list unpacking
a,b,c,*others=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(a)
print(b)
print(c)
print(others)




