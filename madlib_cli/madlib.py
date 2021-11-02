import re

def read_template(path): 
  """
  this function will open and read path of the the file with content
  """
  with open (path) as f:
    content=f.read()
  return content
    # try: 
    #    file = open(path)
    # except FileNotFoundError:
    #   content = "sorry file not found"   
    # else:        
    #  content = file.read()      
    #  print(content)   
    #  file.close()     
    # finally:    
     
    #  return content 


def parse_template(name):
  """
  this function will use the regex to take in a template string and returns a string with 
  language parts removed and a separate list of those language parts
  """
  testing=re.findall(r'{(.*?)}',name)
  x= tuple(testing)
  testing1=re.sub(r'{(.*?)}',"{}",name)

  return testing1,x

# # text=read_template("assets/dark_and_stormy_night_template.txt") 
# # print(text.format(Adjective=input('enter Adjective '),Noun=input('enter Noun ')))
"""
merge

 function will take your answers to replace them in order inside the content that we provides 
"""
def merge(file,x):

    testing1=file.format(*x)
    return testing1

def new_file(content):
  """
  open a new file to but the final result for the pragraph 
  """
  with open("assets/result_video_game.txt",'w') as game:
    game.write(content)



if __name__=="__main__":
  print ("\n Welcome to 'Madlib' Game \n it is a simple game\n  first you will be ask to enter some word with specific types\n  please keep entering the words till you get the finall result with your answers \n enjoy it")
  text=read_template("assets/video_game.txt")
  testing=re.findall(r'{(.*?)}',text)
  arrayWanted=[]
  for i in testing:
     userInput=input(f'Please enter a {i} ')
     arrayWanted.append(userInput)

  arrayWanted2=tuple(arrayWanted)
  #print(arrayWanted2)
  textModify=re.sub(r'{(.*?)}',"{}",text)
  #print (textModify)
  print(merge(textModify,arrayWanted2))
  new_file(merge(textModify,arrayWanted2))








# testing=re.findall(r'{(.?)}',name)
#   x= tuple(testing)
# testing1=re.sub(r'{(.?)}',"{}",name)
# print()