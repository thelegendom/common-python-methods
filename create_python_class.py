def create_Class(ClassName,init_list_of_Variables=None,func=2):
  
  a=f"class {ClassName}:\n"
  cc="\n".join(["\n  def my func(self):\n    #do whatever" for i in range(func)]) #functions after the init method

  if init_list_of_Variables!=None:
    init_list_of_Variables=[item.replace(" ","_") for item in init_list_of_Variables]  #replace spaces with  underscore in list of init variables__ DELETE  if you don't want 
    #so I said instead to delete it yourself the script will  do it for you :)
    ff=", ".join(init_list_of_Variables) # join by commas in init method parameter
    b=f"  def __init__(self,{ff}):\n" # init method with parameters 
    vb="\n".join([f"    self.{i} = {i}" for i in init_list_of_Variables]) #create  self.variable = variable  for all items of list provided  by the user :)
    finall=a+b+vb+"\n"+cc
  else:
    finall=a+cc
  return finall
