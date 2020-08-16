"""usage
--in:
myList=["hello","world","from","python"]
enum_letters(myList,"A")
--out:
[('A', 'hello'), ('B', 'world'), ('C', 'from'), ('D', 'python')]
__________________________________________________________________

enum_letters(myList,"N")
--out:
[('N', 'hello'), ('O', 'world'), ('P', 'from'), ('Q', 'python')]

Hope You like it (O-O)
                   |
                 |___|
"""




def enum_letters(lst,st="a"):
	a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	b=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	if len(lst)<26 and len(lst)>1:
		if st.islower()==True:
			x=a.index(st)
			return list(zip(a[x:x+len(lst)],lst))
		else:
			x=b.index(st)
			return list(zip(b[x:x+len(lst)],lst))
