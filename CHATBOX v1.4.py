import os
import time
import pickle
class CHATBOX:
        def getdata(s):
                s.id=raw_input('UserId : ')
                s.pas=raw_input('Password : ')
                s.ph=input('Phone no. : ')
ch=0
k=0
o=CHATBOX()
def cls(n=0):
        time.sleep(n)
        os.system('cls')
def bye():
        cls()
        print '\n\n\n\n\n\n\n'
        print "\t\t\t.______    ____    ____   _______  "
        print "\t\t\t|   _  \   \   \  /   /  |   ____| "
        print "\t\t\t|  |_)  |   \   \/   /   |  |__    "
        print "\t\t\t|   _  <     \_    _/    |   __|   "
        print "\t\t\t|  |_)  |      |  |      |  |____  "
        print "\t\t\t|______/       |__|      |_______| "
        cls(2)
print '\n\n\n\n\n\n\n'
print "\t __    __        _                                   _          "
print "\t/ / /\ \ \  ___ | |  ___   ___   _ __ ___    ___    | |_   ___  "
print "\t\ \/  \/ / / _ \| | / __| / _ \ | '_ \` _ \ / _ \   | __| / _ \ "
print "\t \  /\  / |  __/| || (__ | (_) || | | | | ||  __/   | |_ | (_) |"
print "\t  \/  \/   \___||_| \___| \___/ |_| |_| |_| \___|    \__| \___/ "
cls(1)
print '\n\n\n\n\n\n'
print "\t\t   ____ _   _    _  _____ ____   _____  __"
print "\t\t  / ___| | | |  / \|_   _| __ ) / _ \ \/ /"
print "\t\t | |   | |_| | / _ \ | | |  _ \| | | \  / "
print "\t\t | |___|  _  |/ ___ \| | | |_) | |_| /  \ "
print "\t\t  \____|_| |_/_/   \_\_| |____/ \___/_/\_\ "
cls(2)
if not(os.path.isfile('records.txt')):
        open('records.txt','wb')
if not(os.path.isfile('req.txt')):
        open('req.txt','wb')
if not(os.path.isfile('gd.txt')):
        open('gd.txt','wb')
while ch!='4':
        print '-------------------------------------------------------------------------------'
        print '\t \t \t Welcome \t To \t CHATBOX'
        print '-------------------------------------------------------------------------------'
        print "1> Login"
        print "2> Register"
        print "3> Forgot Password"
        print "4> Exit"
        print '-------------------------------------------------------------------------------'
        try:
                ch=raw_input('> ')
                if ch=='1':
                        cls()
                        fin=open('records.txt','rb')
                        uid=raw_input('UserId : ')
                        try:
                                while True:
                                        o=pickle.load(fin)
                                        if o.id==uid:
                                                upa=raw_input('Password : ')
                                                if o.pas==upa:
                                                        cls()
                                                        k=5
                                                        fin.close()
                                                        break
                                                else:
                                                        print 'Incorrect Password'
                                                        cls(2)
                                                        fin.close()
                                                        break
                        except EOFError:
                                print 'User does not exist \t Plz register'
                                cls(2)
                                fin.close()
                elif ch=='2':
                        cls()
                        p=CHATBOX()
                        p.getdata()
                        fin=open('records.txt','rb')
                        try:
                                while True:
                                        o=pickle.load(fin)
                                        if o.id==p.id:
                                                print 'User already exist plz login'
                                                cls(3)
                                                break
                                        elif o.ph==p.ph:
                                                print 'Phone number already in use'
                                                cls(3)
                                                break
                                        elif len(str(p.ph))!=10:
                                                print 'Enter 10 digit no.'
                                                cls(3)
                                                break
                        except EOFError:
                                os.system('cls')
                                fin.close()
                                fout=open('records.txt','ab')
                                pickle.dump(p,fout)
                                fout.close()
                elif ch=='3':
                        fin=open('records.txt','rb+')
                        fout=open('temp.txt','wb')
                        uid=raw_input('UserId : ')
                        try:
                                while True:
                                        o=pickle.load(fin)
                                        if o.id==uid:
                                                ph=input('Enter your registered phone no. : ')
                                                if o.ph==ph:
                                                        o.getpass(uid,ph)
                                                        print 'password changed'
                                                        cls(3)
                                                else :
                                                        print 'Wrong number'
                                                        cls(3)
                                                pickle.dump(o,fout)
                                        else:
                                                pickle.dump(o,fout)
                        except EOFError:
                                fin.close()
                                fout.close()
                        os.remove('records.txt')
                        os.rename('temp.txt','records.txt')
                elif ch=='4':
                        bye()
                        break
                else:
                        print 'Invalid input'
                        cls(2)
        except:
                print 'Invalid input'
                cls(2)
        while k==5:        
                cls()
                print '-------------------------------------------------------------------------------'
                print '\t','\t','\t','Welcome','\t',uid.upper()
                print '-------------------------------------------------------------------------------'
                print '1> Send Chat request'
                print '2> Chat room'
                print '3> Chat hall'
                print '4> Chat requests'
                print '5> Logout'
                print '-------------------------------------------------------------------------------'
                try:
                        cho=input('>')
                        if cho==1:
                                fin=open('records.txt','rb')
                                i,z=1,[]
                                try:
                                        while True:
                                                f=pickle.load(fin)
                                                e=f.id
                                                name=uid+'-'+e+'.txt'
                                                name1=e+'-'+uid+'.txt'
                                                if f.id!=uid:       
                                                        if not(os.path.isfile(name) or os.path.isfile(name1)):
                                                                print i,'>',f.id
                                                                i+=1
                                                                z.append(f.id)
                                except EOFError:
                                        fin.close()
                                if i==1:
                                        print 'No users found for request!'
                                        cls(2)
                                        continue
                                try:
                                        r=input('Send request to: ')
                                        rid=z[r-1]
                                        q=open('req.txt','a')
                                        q.write(rid+'-'+uid+'\n')
                                        print 'Sent!'
                                        q.close()
                                        cls(2)
                                except IndexError:
                                        print 'Invalid Input'
                                        cls(2)
                                except SyntaxError:
                                        print 'Invalid Input'
                                        cls(2)
                        elif cho==2:
                                fin=open('records.txt','rb')
                                i,l=1,[]
                                try:
                                        while True:
                                                f=pickle.load(fin)
                                                e=f.id
                                                name=uid+'-'+e+'.txt'
                                                name1=e+'-'+uid+'.txt'
                                                if os.path.isfile(name) or os.path.isfile(name1):
                                                        l.append(e)
                                                        print i,'>',e
                                                        i+=1                               
                                except EOFError:
                                        fin.close()
                                if i!=1:
                                        d=raw_input('> ')
                                        if d=='':
                                                print 'Invalid Input'
                                                cls(2)
                                                continue
                                        c=int(d)
                                        nm=uid+'-'+l[c-1]+'.txt'
                                        nm1=l[c-1]+'-'+uid+'.txt'
                                        if os.path.isfile(nm):
                                                name=nm
                                        elif os.path.isfile(nm1):
                                                name=nm1
                                        f=open(name,'a+')
                                        w='\t\t\t'+uid.upper()+' joined the hall'+'\n'
                                        f.write(w)
                                        f.close()
                                        while True:
                                                cls()
                                                print '-------------------------------------------------------------------------------'
                                                print '\t\tpress enter to refresh and .. to go back'
                                                print '-------------------------------------------------------------------------------'
                                                t=open(name,'a+')
                                                l=t.readlines()
                                                for i in l:
                                                        print i
                                                a=raw_input('<you>')
                                                if a=='..':
                                                        w='\t\t\t'+uid.upper()+' left the hall'+'\n'
                                                        t.write(w)
                                                        t.close()
                                                        break
                                                elif a=='cls':
                                                        f=open(name,'w')
                                                        t.close()
                                                elif a!='':
                                                        w='<'+uid+'>'+a+'\n'
                                                        t.write(w)
                                else:
                                        print 'You do not have any friends :/'
                                        cls(2)
                        elif cho==3:
                                f=open('gd.txt','a+')
                                w='\t\t\t'+uid.upper()+' joined the hall'+'\n'
                                f.write(w)
                                f.close()
                                while True:
                                        cls()
                                        print '-------------------------------------------------------------------------------'
                                        print '\t\tpress enter to refresh and .. to go back'
                                        print '-------------------------------------------------------------------------------'
                                        f=open('gd.txt','a+')
                                        l=f.readlines()
                                        for i in l:
                                                print i
                                        a=raw_input('<you>')
                                        if a=='..':
                                                w='\t\t\t'+uid.upper()+' left the hall'+'\n'
                                                f.write(w)
                                                f.close()
                                                break
                                        elif a=='cls':
                                                f=open('gd.txt','w')
                                                f.close()
                                        elif a!='':
                                                w='<'+uid+'>'+a+'\n'
                                                f.write(w)
                        elif cho==4:
                                q=open('req.txt','r')
                                temp,l,i=open('temp.txt','w'),'a',0
                                while True:
                                        l=q.readline()
                                        w=l.split('-')
                                        if w[0]==uid:
                                                i=1
                                                print w[1]
                                                ans=raw_input('Accept(Y/N)')
                                                if ans.upper()=='Y':
                                                        nm=w[0]+'-'+w[1].split('\n')[0]+'.txt'
                                                        fc=open(nm,'w')
                                                        print 'Accepted!'
                                                        cls(2)
                                                elif ans=='':
                                                        temp.write(l)
                                        elif l!='':
                                                temp.write(l)
                                        elif l=='':
                                                q.close()
                                                temp.close()
                                                os.remove('req.txt')
                                                os.rename('temp.txt','req.txt')
                                                break
                                if i==0:
                                        print 'Sorry,you don\'t have any chat requests :|'
                                        cls(2)
                        elif cho==5:
                                ch,k=1,1
                                bye()
                                continue
                        else:
                                print "Invalid Input"
                                cls(2)
                except:
                        print "Invalid input"
                        cls(2)
