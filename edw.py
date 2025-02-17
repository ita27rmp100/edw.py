#libs
from termcolor import colored
import os , time , calendar , sqlite3 , platform
from data import *
# connection & set-up with DB
connection = sqlite3.connect("histrory.db")
db = connection.cursor()
try :
    db.execute("create table history (command varchar(200))")
except :
    pass
#fnctns
def dir(place):
    dirList = ''
    for i in os.listdir(place):
        dirList +='\n'+i
    return dirList
    # callbacks to include with commands in redirection
prevCommand = {
    'input':"",
    'callback':""
}
sheet = ''
def displayHis():
    db.execute("select * from history")
    data = db.fetchall()
    history = ''
    for his in data :
        history +=str(his[0]+'\n')
    print(history)
    return history
def callback(msg) :
    print(msg+'\n')
    prevCommand["callback"] = msg
    db.execute(f"INSERT INTO history VALUES ('{prevCommand['input']}')")
def restart() :
    if platform.system()=="Windows" :
        os.system("shutdown /r")
    else :
        os.system("sudo reboot")
def infoSys(arg) :
    result = ''
    if " -r" in arg :
        result += platform.release()
    if " -s" in arg :
        result += platform.system()
    if " -v" in arg :
        result += platform.version()
    return result
# the execution
print(colored(greeting,"red"))
print(colored("-"*50,"blue"),"\r")
while True :
    instrct = input(colored(os.getcwd()+"@: ","green"))
    try:
        g = instrct[0:instrct.index("$")+1]
        more = instrct[instrct.index("$")+2:]
        prevCommand["input"] = instrct
        eval(orders[g])
        sheet += str(prevCommand)
    except NameError as msg:
        print(msg)