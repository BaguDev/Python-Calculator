 print('Python Calculator | By BaguDev')
import itertools
import threading
import time
import sys

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['.', '..', '...', '..']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!')
    print('Type in a number\n')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(3)
done = True

 def is_float(var):
    try:
        float(var)
        return True
    except ValueError:
        return False
def checkoperation(operation):
  if (to_do == "A")or(to_do == "B")or(to_do=="C")or(to_do=="D"):
    return True
  else:
    return False
varA = input("Type In A Number\n")
while is_float(varA) == False:
    varA = input("Incorrect input, try again\n")
    varAfloat = is_float(varA)
varA = float(varA)
varB = input("Type in another number\n")
while is_float(varB) == False:
    varB = input("Incorrect input, try again\n")
varB = float(varB)
to_do = (input("Type A for multiplication, B for division, C for addition, or D for subtraction\n"))
while checkoperation(to_do) == False:
  to_do = input("invalid operator input, try again\n")
if to_do == "A":
    total = varA * varB
elif to_do == "B":
    total = varA / varB
elif to_do == "C":
    total = varA + varB
elif to_do == "D":
    total = varA - varB
else:
    print(to_do)
print(total)
print('Thanks for using Python Calculator!')
