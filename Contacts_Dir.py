contacts={}
key_list=[]

my_path='/Users/ballb/Desktop/Rando_python/this.txt.txt'

def refreshContacts():
    """fills contacts dic with contents of txt file"""
    directory=open(my_path)
    dir_info=((directory.read()).split(','))
    directory.close()
    for string in dir_info:
        holder=string.split()
        contacts[holder[0]]=holder[1]

refreshContacts()

def saveInfo():
    """writes any changes made to the contacts dic into the txt file"""
    things_written=0
    directory=open(my_path, 'w')
    contact_info=contacts.keys()
    for items in contact_info:
        items2=stripCrap(items)
        things_written+=1
        directory.write(items+" "+contacts[items])
        if things_written<len(contacts):
            directory.write(", ")                      
    directory.close()
def done():
    """saves and restarts process"""
    print("done")
    saveInfo()
    start()
    
def stripCrap(string):
    #util
    temp=string
    del(string)
    string1=temp.strip('dict_keys([')
    string2=string1.strip('"')
    string3=string2.strip('])')
    string4=string3.strip("'")
    return string4
    
def addContact():
    """adds new contact into contact dic"""
    name=input("What is their name? ")
    number=input("What is their number? ")
    check_value=input("does this look right: {},{}? Y/N ".format(name,number))
    if check_value=='Y':
        addValue(number,name)
        done()
    else:
        addContact()
def deleteContact():
    """removes contact from dic"""
    name=input("What is their name? ")
    del(contacts[name])
    done()
        
def changeNumber():
    """removes and replaces number of selected contact"""
    key=input("Whos number would you like to change? ")
    removeValue(key)
    addValue(value_added=(input("What would you like {}'s new number to be? ".format(key))),key=key)
    done()
def removeValue(key):
    contacts[key]="null"
def addValue(value_added, key):
    contacts[key]=value_added

def findNumber():
    """searches for name in database"""
    name=input("What is their name? ")
    try:
        print(contacts[name])
    except:
        print("this name is not in your contacts")
        findNumber()
    done()
def start():
    print("options         ")
    print("----------------")
    print("find number")
    print("add contact")
    print('delete contact')
    print("change number")
    print("stop")
    """initilizes and resets process of searching"""
    refreshContacts()
    start_value=input("What would you like to do? ")

    if start_value=="change number":
        changeNumber()
    elif start_value=="add contact":
        addContact()
    elif start_value=="delete contact":
        deleteContact()
    elif start_value=="find number":
        findNumber()
    elif start_value=="stop":
        exit()
    else:
        print("we cannot perform that action")


start()



              


