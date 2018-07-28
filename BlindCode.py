import getpass,time,os
import urllib.request as urllib2
from urllib.parse import urlencode
def inpDetails():
    Name=input('Enter Your Name:')
    College=input('Enter Your College Name:')
    Contact=input('Enter Your Contact Number:')
    print('Welcome ',Name,' In Tx18,\n Enter your code after next 5sec:')
    for i in range (0,5):
        print(5-i,'...')
        time.sleep(1)
    return Name,College,Contact

def storeCode(Code,Name):
    Filename=Name+'.c'
    F=open(Filename,"w")
    F.write(Code)
    F.close()
    return Filename

def inpCode(Name):
    t1=time.time()
    x = []
    Timestr=""
    while True:
        os.system('cls')
        temp = getpass.getpass(Timestr)
        if temp:
            x.append(temp)
        else:
            print('you want to exit?? (1/0)')
            y=input()
            if y:
                break
            else:
                continue
    Code = '\n'.join(x)
    t2=time.time()
    t=t2-t1
    Minutes = int(t / 60)
    Seconds = int(t - Minutes * 60.0)
    hseconds = int((t - Minutes * 60.0 - Seconds) * 100)
    Timestr=('%02d:%02d:%02d' % (Minutes, Seconds, hseconds))
    filename=storeCode(Code,Name)
    return filename,Timestr,Code

def WagnerFischer(A, B, insertion=1, deletion=1, substitution=2):
    try:
        from numpy import zeros
        def _zeros(*shape):
            return zeros(shape)
    except ImportError:
        print('numpy error')
    """
    Strings are input as A and B. Costs can be optionally given. Matches are
    always free. Returns A and B plus a list of characters indicating
    insertion, deletion, or substitution.
    #>>> print(WagnerFischer('abcd', 'abxcd'))
    ('ab*cd', 'abxcd', '==^==')
    #>>> print(WagnerFischer('unfreakingbelievable', 'unbelievable'))
    ('unfreakingbelievable', 'un********believable', '==vvvvvvvv==========')
    """
    A = list(A)  # will perform insertion of these...so has to be a list
    B = list(B)
    n_A = len(A)
    n_B = len(B)
    # compute distance matrix
    D = _zeros(n_A + 1, n_B + 1)
    for i in range(n_A):  # cost of deletion
        D[i + 1][0] = D[i][0] + deletion
    for j in range(n_B):  # cost of insertion
        D[0][j + 1] = D[0][j] + insertion
    for i in range(n_A):  # fill out middle of matrix
        for j in range(n_B):  # fill out matrix # 1
            if A[i] == B[j]:  # match
                D[i + 1][j + 1] = D[i][j]  # aka, it's free.
            else:  # no match
                D[i + 1][j + 1] = min(D[i + 1][j] + insertion,
                                      D[i][j + 1] + deletion,
                                      D[i][j] + substitution)
                # traceback
    change = []
    while n_A > 0 and n_B > 0:
        s_cost = D[n_A][n_B]  # substitute or match
        d_cost = D[n_A - 1][n_B]  # delete
        i_cost = D[n_A][n_B - 1]  # insert
        if s_cost < d_cost:
            if s_cost < i_cost:
                if s_cost == D[n_A][n_B]:  # match
                    change.append('=')
                else:  # substitution
                    change.append('*')
                n_A -= 1
                n_B -= 1
            else:  # insertion
                change.append('^')
                A.insert(n_A, '*')  # 1
                n_B -= 1
        else:  # deletion
            change.append('v')
            B.insert(n_B, '*')  # 1
            n_A -= 1
    return ''.join(A), ''.join(B), ''.join(change[::-1])

def test():
    inp=    '#include<stdio.h>\nvid main(){\nprintf("h6llo");\n}'
    orginal='#include<stdio.h>\nvoid main(){\nprintf("hello");\n}'
    print (WagnerFischer(orginal,inp))

def codeComp(Filename,Code):
    f=open("master.c","r")
    master=f.read()
    x,y,z=WagnerFischer(master,Code)
    cmd='gcc '+Filename+' -o a'
    import re, subprocess
    pattern = 'error'
    output = subprocess.getoutput(cmd)
    count=0
    for i in range(len(z)):
        if z[i] is '^':
            if z[i+1] is not 'v':
                count+=1
        elif z[i] is 'v':
            count+=1
    Error = len(re.findall(pattern, output))
    return  Error+count

name,college,contact=inpDetails()
filename,timestr,code=inpCode(name)
print('Thanks ',name,' for participating in Blind code :)')
print('Inform volunteer ')
error=codeComp(filename,code)
contact=int(contact)
url = "https://blindcode.000webhostapp.com/bc.php"
data={'name':name, 'contact':contact,'error':error,'college':college,'timecomplited':timestr}
encoded_data = urlencode(data).encode("utf-8")
website = urllib2.urlopen(url, encoded_data)
print (website.read())