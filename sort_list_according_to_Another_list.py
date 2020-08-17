"""
USAGE:

you have a list and you want to sort it according to another list

Ex:

b=["peter","my","is","name"] # unsorted.. 

a=["my","name","is","jack","peter"] # sorted

sort_list_according_to_Another_list(b,a)

['my', 'name', 'is', 'peter'] #output

"""

def sort_list_according_to_Another_list(your_list,sorted_list):
	return [i for i in sorted_list if i in your_list]


