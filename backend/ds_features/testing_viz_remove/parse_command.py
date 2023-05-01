import sys
sys.path.append("../")
import grapher

def parser(message):
    command, data = message.split(' ')
    print(command)
    print(data)

if(__name__=="__main__"):
    update(10, "omg")