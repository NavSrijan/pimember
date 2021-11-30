import tty, sys, termios
file = open("pi", "r")
digits = file.readline()
digits.strip(" ")
def matchDigits(dig):
    if dig==digits[0:len(dig)]:
        return True
    else:
        return False
filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
x = 0
exp = "3."
score = 0
print(exp, end='', flush=True)
while True:
    x=sys.stdin.read(1)[0]
    print(x,end='',flush=True)
    exp+=x
    if matchDigits(exp)==True:
        score+=1
    else:
        print("")
        print("SCORE: {}".format(score))
        print("The next two digits are: {}".format(digits[len(exp)-1:len(exp)+3]))
        break
termios.tcsetattr(sys.stdin, termios.TCSADRAIN,filedescriptors)
