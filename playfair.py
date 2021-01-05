import numpy as np

key=[]
data=[]
temp=[[]]
key=input("키 값을 입력하세요:")
for j in key: #키 값의 중복 제거 (set 사용시 순서 바뀜)


    if (data.count(j)==1):
            continue
    else:
        data.append(j)


Table= [['0'] * 5 for i in range(5)] #5x5 배열 생성

for j in range(26): #키값에 있는 알파벳을 제외하고 데이터에 저장
    if(data.count(chr(97+j))==1):
        continue
    else:
        data.append(chr(97+j))

sub=[]
sub=input("암호화 시 묶을 두 글자를 입력하세요(슬라이스로 알파벳 구분해서 알파벳 순으로 입력):")
temp=[]

p=0
data.remove(sub[2]) #데이터값에서 묶을 알파벳 중 두번째 알파벳 삭제 

for i in range(5): #암호화테이블안에 데이터값 삽입 
    for j in range(5):  
        if (data[p]==sub[0]):
            Table[i][j]=sub[0]
            temp=data[p]
            temp+=sub[2]
            
     
        elif(data[p]!=sub[2]):
            Table[i][j]=data[p]
        p+=1

print("------플레이페어 암호화 테이블------") #암호화테이블 출력 

for i in range(5):
    for j in range(5):

        if(Table[i][j])==sub[0]:

            
            print('%5s' % (temp), end= '  ')
        else:
            print('%5s' % (Table[i][j]), end='  ')
            
    print('\n')


exam=[]
exam=input("암호화할 문장을 입력하세요:")
exam=exam.replace(' ','') #문장에서 공백 제거 
exam=exam.lower() #문장을 모두 소문자로 
sl=[]
for x in range(0,len(exam)+1,2):
    if x < len(exam)-1:
        if exam[x]==exam[x+1]: #묶인 알파벳이 같으면 사이에 x삽입 
            exam=exam[:x+1]+'x'+exam[x+1:]
exam=list(exam)
if len(exam)%2!=0: #평문안의 알파벳이 홀수면 마지막에 x삽입 
    exam.append('x')
    
for x in range(0,len(exam),2): #sl배열에 평문 속 알파벳 두개씩 묶기 
    sl.append(exam[x:x+2])


l=np.shape(sl)
sh=np.array(Table) #numpy로 테이블 5x5배열화 
row=l[1]
col=l[0]


amho=[]

for i in range(col):
    for j in range(5):
        
        shcol=sh[j,:] #한 행씩 자르기
        shrow=sh[:,j] #한 열씩 자르기 
        f=sl[i][0] #암호화할 글자1
        s=sl[i][1] #암호화할 글자2
        if(f == sub[2] or s== sub[2]):
            if(f==sub[2]):
                f=sub[0]
            elif(s==sub[2]):
                s=sub[0]
        cnt=0
        
        #sh내에서 f,s의 인덱스 구하기 (몇 행,몇 열인지) 
        z=int((np.where(sh==f)[0]))
        y=int((np.where(sh==f)[1]))
        z1=int((np.where(sh==s)[0]))
        y1=int((np.where(sh==s)[1]))

        if ((np.any(f in shcol)) and (np.any(s in shcol))): #f와 s가 같은 행에 있을 경우 
            p=int((np.where(shcol==f)[0])+1) #한칸씩 옆으로 밀기 
            q=int((np.where(shcol==s)[0])+1)
            #알파벳이 마지막 행에 있을 경우 첫번째 행으로 
            if (p==5):
                p=0
            elif(q==5):
                q=0
            amho.append(shcol[p])
            amho.append(shcol[q])
            
        elif ((np.any(f in shrow)) and (np.any(s in shrow))): #f와 s가 같은 열에 있을 경우 
            p=int((np.where(shrow==f)[0])+1)
            q=int((np.where(shrow==s)[0])+1)
            if (p==5):
                p=0
            elif(q==5):
                q=0           
            amho.append(shrow[p])
            amho.append(shrow[q])
        
        
        elif (z!=z1 and y!=y1): #f와 s가 행,열 모두 다를 경우 
            
      
            amho.append(Table[z1][y])
            amho.append(Table[z][y1])
            break
              
amho=str.join(' ',amho) #리스트를 문자열화 
print(amho)
