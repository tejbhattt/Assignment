from collections import OrderedDict
def remove_duplicate(sujal):
  return "".join(OrderedDict.fromkeys(sujal))
     
print(remove_duplicate("My Name Is Sujal Mansuri"))
print(remove_duplicate("Mr.handsome"))