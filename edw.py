#libs
from termcolor import colored
import os , time , calendar
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
def callback(msg) :
    print(msg+'\n')
    prevCommand["callback"] = msg
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
        "quit$":"callback('quit ... hasta leugo')',quit()",
        "reboot$":"callback('reboot'),os.system('c:\Windows\System32\shutdown.exe /s /t 1')",
        "dir$":"callback(dir(more))",
        "time$":"callback(time.ctime())",
        "clear$":"os.system('cls'),callback('')",
        "chrome$":"os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe'),callback('google chrome opened')",
        "exist$":"callback(os.path.exists(r'{}'.format(more)))",
        "read$":"callback(os.system(f'type {more}'))",
        "calendar$":"callback(calendar.month(int(more[0:more.index(',')]),int(more[more.index(',')+1:])))",
        'calc$':"calback(eval(more))",
        "help$":"calback(list(orders.keys()))",
        "redirect$":"open(more,mode='a').write(prevCommand['input']+'\n'+prevCommand['output'])",
        "save$":"open(more,mode='a).write(sheet)"
    }
# the execution
print(colored("Welcome to edw","red"))
print(colored("-"*50,"blue"),"\r")
while True :
    print(colored(os.getcwd)+"@:","green")
    instrct = input()
    try:
        g = instrct[0:instrct.index("$")+1]
        more = instrct[instrct.index("$")+2:]
        prevCommand["input"] = instrct
        eval(orders[g])
        sheet += str(prevCommand)
    except NameError as msg:
        print(msg)