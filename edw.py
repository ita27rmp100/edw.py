#libs
from termcolor import colored
import os , time , calendar , sqlite3 , platform
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
#vars
orders={"write$":"callback(more)",
        "open$":r"os.system(more),callback('opened'+more)",
        "go$":r"os.chdir(more),callback('you are in ',os.getcwd())",
        "where$":r"callback(os.getcwd())",
        "rename$":"os.rename(more[0:more.index(',')],more[more.index(',')+1:]),callback('renamed to'+more[more.index(',')+1:])",
        "rfo$":"os.rmdir(more),callback('removed'+more)",
        "cfo$": "os.mkdir(more),print('created folder with name : '+more)",
        "rfi$": "os.remove(more),print('removed'+more)",
        "cfi$": "open(more,mode='x'),print('created file with name : '+more)",
        "quit$":"callback('goodbye'),quit()",
        "reboot$":"callback('reboot'),os.system('c:\Windows\System32\shutdown.exe /s /t 1')",
        "dir$":"callback(listdir(more))", #
        "time$":"callback(time.ctime())",
        "clear$":"os.system('cls'),callback('')",
        "chrome$":"os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe'),callback('google chrome opened')",
        "exist$":"callback(os.path.exists(r'{}'.format(more)))",
        "read$":"callback(os.system(f'type {more}'))",
        "calendar$":"callback(calendar.month(int(more[0:more.index(',')]),int(more[more.index(',')+1:])))",
        'calc$':"calback(eval(more))",
        "help$":"calback(list(orders.keys()))",
        # from here the new commands
        "redirect$":"open(more,mode='w').write(prevCommand['input']+'\n'+prevCommand['output'])",
        "redirect -ow$":"open(more,mode='a').write(prevCommand['input']+'\n'+prevCommand['output'])",
        "save$":"open(more,mode='a).write(sheet)",
        "history$":"callback(displayHis())",
        "delhis$":"db.execute(delete from history)",
        "chtime$":"callback(os.system('time'))",
        "restart$":"restart()", # supported only for windows and linux
        "sysinfo$":"callback(infoSys(more))"
    }
greeting = """
#  .............._............................_..................._......................
#  __......_____|.|.___.___.._.__.___...___..|.|_.___.....___..__|.__......___.__.._..._.
#  \.\./\././._.|.|/.__/._.\|.'_.`._.\./._.\.|.__/._.\.../._.\/._`.\.\./\./.|.'_.\|.|.|.|
#  .\.V..V.|..__|.|.(_|.(_).|.|.|.|.|.|..__/.|.||.(_).|.|..__|.(_|.|\.V..V._|.|_).|.|_|.|
#  ..\_/\_/.\___|_|\___\___/|_|.|_|.|_|\___|..\__\___/...\___|\__,_|.\_/\_(_|..__/.\__,.|
#  .........................................................................|_|....|___/.
"""
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