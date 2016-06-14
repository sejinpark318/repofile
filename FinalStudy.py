
# coding: utf-8

# # 6. 데이터구조 

# ## 1) 1 ~ 1000의 수 가운데 4로 나누어지고 5로 나누어지지 않는 수를 골라서 리스트에 넣기.

# In[1]:

first=list()
for i in range(1,1001):
    if i%4==0 and i%5!=0:
        first.append(i)
print first


# ## 2) 거북이 트랙을 저장하기

# In[2]:

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


def drawSquareAtAndSave(size, pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    mytracks=list()
    for i in range(0,4):
        mytracks.append(t1.pos())
        t1.forward(size)
        t1.right(90)
    return mytracks

t1tracks=drawSquareAtAndSave(50,(100,-100))
print t1tracks


# ## 데이터구조-3: 도형을 데이터구조로 저장하고 그리기

# In[6]:

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


def drawSquareFrom(list):
    for i in range(len(list)):
        t1.goto(list[i])

tracks=list()
tracks=[[100,100],[200,100],[200,200],[100,200],[100,100]]
drawSquareFrom(tracks)


# ## 데이터구조-4: 거북이가 걸어간 트랙을 다시 걷게 하기

# In[8]:

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

tracks=list()

def saveTracks():
    t1.speed(1)
    t1.penup()
    t1.goto(-40,30)

    tracks.append(t1.pos())

    t1.pendown()
    t1.pencolor("Red")
    t1.right(90)
    t1.fd(40)

    tracks.append(t1.pos())

    t1.backward(15)

    tracks.append(t1.pos())

    t1.left(90)
    t1.fd(30)

    tracks.append(t1.pos())

    t1.left(90)
    t1.fd(30)

    tracks.append(t1.pos())

    t1.back(15)

    tracks.append(t1.pos())

    t1.right(90)
    t1.fd(30)

    tracks.append(t1.pos())

    t1.left(90)
    t1.right(90)
    t1.right(90)
    t1.fd(20)

    tracks.append(t1.pos())

    t1.fd(30)

    tracks.append(t1.pos())

    t1.back(10)

    tracks.append(t1.pos())

    t1.left(90)

    t1.fd(20)

    tracks.append(t1.pos())


def replayTracks(mytracks):
    t1.home()
    t1.clear()
    for t in mytracks:
        print t
        t1.setpos(t)
        
mytracks=saveTracks()
replayTracks(mytracks)


# ## 데이터구조-5: 문자열에서 문자를 세기

# In[9]:

word='sangmyung university'
word.split()


# In[13]:

word='sangmyung university'
for c in word:
    print c,


# In[16]:

def countChars(word):
    d = dict()
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d

word=raw_input()
print countChars(word)


# In[30]:

import matplotlib
import matplotlib.pyplot as plt
# 2단계로 나누어 그림
plt.bar(range(len(d)), d.values(), align='center')
plt.xticks(range(len(d)), list(d.keys()))
plt.show()


# ## 데이터구조-6: 문자열에 포함된 문자와 숫자의 개수 세기

# In[32]:

s= raw_input()
d={"DIGITS":0,"LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]


# ## 데이터구조-7: 우리 집에 없지만 친구집에 있는 가전제품 찾기.

# In[18]:

myHome={"TV", "phone", "camera", "fridger", "mixer", "audio", 
        "cd player", "light", "computer", "notebook", "recorder"}
yourHome={"coffee machine", "radio", "camera", "running machine", 
          "ramp", "computer", "notebook", "recorder"}


# In[21]:

# 우리 집에는 있지만 친구 집에 없는 것
print myHome-yourHome
print myHome.difference(yourHome)

# 우리 집에도 있고 친구 집에도 있는 것
print myHome.intersection(yourHome)
print yourHome.intersection(myHome)

# 우리 집에도 있고, 친구 집에도 있는 것.
print myHome.union(yourHome)
print yourHome.union(myHome)

# set를 더하는 것은 안 된다. set은 중복을 허락지 않는 구조
# list로 더할 수 있다.
print len(list(myHome)+list(yourHome))


# ## 데이터구조-8: 서울 경복궁 입구에서 제일 가까운 지하철 역 찾기

# In[28]:

locations=list()
locations=[(37.575790, 126.973463),
           (37.576471, 126.985435),
           (37.571577, 126.976575),
           (37.574564, 126.957738)]
print locations
loc=locations


# In[24]:

for i in locations:
    print i[0],i[1]


# In[29]:

# 거리
import math
x=list()
def closestSta():
    for i in range(1,4):
        x.append(math.sqrt((loc[0][0]-loc[i][0])**2 + (loc[0][1]-loc[i][1])**2))
    print x

    res=min(x)
    return res

closestSta()


# ## 데이터구조-9: 서울에 거주하는 남녀의 구별 합계와 평균구하기

# In[34]:

stat=list()
stat=(
('jongno',80531,83291),
('jung',66755,67574),
('yongsan',121027,126882),
('sungdong',151459,153606),
('kwangjin',183436,191744),
('dongdaemun',185827,187997),
('junglang',208393,210227),
('sungbuk',229183,240377),
('gangbuk',164337,170089),
('dobong',173804,179437),
('nowon',281538,296683),
('eunpyeong',244964,257614),
('seodaemun',156130,166975),
('mapo',190957,207394),
('yangchun',242074,246936),
('kangseo',291216,304475),
('kuro',228201,226403),
('keumchun',131346,124821),
('youngdeungpo',210388,207423),
('dongjak',202165,210609),
('kwanak',266773,262258),
('seocho',217036,234222),
('kangnam',279209,302551),
('songpa',325950,341530),
('kangdong',230851,232470))


# In[42]:

sumM=0
sumF=0
gusum=list()
guname=list()
for i in range(len(stat)):
    gusum.append(stat[i][1]+stat[i][2])
    guname.append(stat[i][0])
    sumM+=stat[i][1]
    sumF+=stat[i][2]
    
aveM=sumM/len(stat)
aveF=sumF/len(stat)

print sumM,sumF
print aveM,aveF
print gusum
print guname

import matplotlib
import matplotlib.pyplot as plt
plt.bar(range(len(gusum)),gusum,align='center')
plt.show


# ## 데이터구조-10: 커피에 Milk를 추가하는 비율구하기

# In[ ]:

allData=list()
allData=(("coffee","Water","Milk","Icecream"),
        ("Espresso","No","No","No"),
        ("Long Black","Yes","No","No"),
        ("Flat White","No","Yes","No"),
        ("Cappuccino","No","Yes","No"),
        ("Affogato","No","No","Yes"))
data=allData[1:6]

def milkPercent(data):
    sWater=0
    sMilk=0
    for i in data:
        if(i[2]=="Yes"):
            sMilk+=1

    fsMilk= float(sMilk)
    percent=fsMilk/len(data)*100
    return "{0}%".format(percent)
milkPercent(data)


# ## 데이터구조-11: 성적데이터의 평균/합계를 구하기.

# In[ ]:

allScore=list()
allScore=[("English","Math"),
       (100,200),
       (200,200),
       (100,300)]
print allScore
Score=allScore[1:]
print Score

def scoreAve():
    English=0
    Math=0
    for i in Score:
        English+=i[0]
        Math+=i[1]

    fEnglish=float(English)
    fMath=float(Math)
    return (fEnglish/len(Score),fMath/len(Score))
scoreAve(Score)


# ## 데이터구조-12: The Beatles 'Let it be' 가사에서 자주 등장하는 단어는?

# In[ ]:

doc=[
    "When I find myself in times of trouble",
    "Mother Mary comes to me",
    "Speaking words of wisdom, let it be",
    "And in my hour of darkness",
    "She is standing right in front of me",
    "Speaking words of wisdom, let it be",
    "Let it be",
    "Let it be",
    "Let it be",
    "Let it be",
    "Whisper words of wisdom, let it be"
]


# In[ ]:

for sentence in doc:
    words=sentence.split()
    for word in words:
        print word,
    print
    
# 위랑 똑같은거
for sentence in doc1:
    for word in sentence:
        print word


# In[ ]:

def countWords(doc):
    d = {}
    for sentence in doc:
        words=sentence.split()
        for word in words:
            if word in d:
                d[word]+=1
            else:
                d[word]=1
    return d

def getWordsFreqGreater(c,d):
    w=list()
    for k in d:
        if d[k]>c:
            w.append(k)
    return w

wordDict=countWords(doc)
freqWordsList=getWordsFreqGreater(2,wordDict)
print "Frequent words: ",freqWordsList


# ## 이벤트-1 키보드 방향기에 따라 거북이를 움직이기

# In[1]:

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def keyup():
    pt=t1.pos()
    print "up",pt
    t1.write(pt)
    t1.forward(45)

def keyleft():
    t1.left(45)
    
def keyright():
    t1.right(45)
    
def keyright():
    p1=t1.pos()
    print "down", pt
    t1.write(pt)
    t1.back(45)
    
def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
    wn.onkey(wn.bye,"q")
    
def gamePlay():
    import turtle
    addKeys()
    wn.listen()
    turtle.mainloop()

def lab10():
    gamePlay()


# ## 이벤트-2: 마우스가 클릭하는 위치에 거북이를 이동하기

# In[ ]:

def mousegoto(x,y):
    msg="mouse clicked {0} {1}".format(x,y)
    wn.title(msg)
    t1.setpos(x,y)
    
def addMouse():
    wn.onclick(mousegoto)
    
def gamePlay():
    import turtle
    addKeys()
    addMouse()
    wn.listen()
    turtle.mainloop()
    
def lab10():
    gamePlay()
    


# ## 이벤트-3 키보드, 마우스로 미로게임 해보기
# ### wn.bgpic("myMaze.gif")

# ## 이벤트-4 거북이가 구역에 들어가면 알려주기

# In[ ]:

def isInRectangle(point,coord):
    x1=coord[0][0]
    x2=coord[1][0]
    y1=coord[0][1]
    y2=coord[1][1]
    xs=min(x1,x2)
    xe=max(x1,x2)
    ys=min(y1,y2)
    ye=max(y1,y2)
    x=point[0]
    y=point[1]
    return (xs<=x<=xe and ys<=y<=ye)


# ## 이벤트-5 거북이가 선을 밟았는지 알려주기

# In[ ]:

def isOnLine(point,pos1,pos2):
    x1=pos1[0]-1
    y1=pos1[1]-1
    x2=pos2[0]+1
    y2=pos2[1]+1
    return isInRectangle(point,[(x1,y1),(x2,y2)])

def isOndiagonal(point,pos1,pos2):
    for i in pos2[0]:
        for j in pos2[1]:
            x1=pos1[0]
            x2=pos1[1]
            y1=pos1[0]+i
            y2=pos1[1]+j
            if isInRectangle(point,[(x1,y1),(x2,y2)]):
                return true


# ## 이벤트-6 거북이가 원에 들어갔는지 알려주기

# In[ ]:

def isInCircle(curpos,radius,pos):
    center=(pos[0],pos[1]+radius)
    distance=getEuclDistance(center,curpos)
    return distance<=radius

def drawCircleAt(radius,pos):
    oldheading=t1.heading()
    t1.setheading(0)
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    t1.circle(radius)
    t1.setheading(oldheading)
    
def getEuclDistance(p1,p2):
    import math
    dtemp=0
    for i in range(len(p1)):
        dtemp+=math.pow(p1[i]-p2[i],2)
    distance=math.sqrt(dtemp)


# ## 파일-1 파일을 읽어서, python단어가 있는 줄을 화면에 출력하기

# In[ ]:

# read()전체, readline()한줄, 
#한줄씩읽기1
myfile=open('python.txt','r')
while(line):
    line=myfile.readline()
    print line
myfile.close()

#2
myfile=open('python.txt','r')
for line in myfile.readlines():
    print line
myfile.close()

#3
with open('python.txt','r') as f:
    for line in f:
        print line


# In[ ]:

# 전체읽기1, read()전체, readline()한줄, readlines()리스트로한줄
myfile=open('python.txt','r')
contents=myfile.read()
myfile.close()
print contents

#2
myfile=open('python.txt','r')
contestns=myfile.readlines()
myfile.close()
print contents


# In[ ]:

#파일의 검색
myfile=open('python.txt')
for line in myfile:
    if line.fine('Python')>=0:
        print line
myfile.close()


# In[ ]:

#오류의 처리
try:
    myfile=open('python.txt')
    for line in myfile:
        if line.lower().find('python')>=0:
            print line
    myfile.close()
except IDError as e:
    print e


# In[ ]:

#오류처리 함수로
def serachFile(aFile, query):
    result=list()
    try:
        myfile=open(aFile)
        for line in myfile:
            if line.lower().find(query)>=0:
                result.append(line)
        myfile.close()
    except IOError as e:
        print e
    return result

import os
mydir=os.getcsw()
filename=os.path.join(myfir,'python.txt')
res=searchFile(filename,'python')
print res


# ## 파일-2: 파일에 있는 python단어를 변경해서 쓰기

# In[5]:

#파일에쓰기
fout=open('output.txt','w')
fout.write("first line\n")
fout.write("\tsecond line\n")
fout.write("third")
fout.close()


# In[6]:

#대문자로 변경하기
fin=open('output.txt','r')
for line in fin:
    words=line.split()
    for word in words:
        if word=='line':
            print word.upper()
        else:
            print word
fout.close()


# In[16]:

fin=open('output.txt','r')
fout=open('outputUpper.txt','w')
for sentence in fin:
    if sentence.find('line')>=0:
        sentence=sentence.replace('line','LINE')
    fout.write(sentence)
fin.close()
fout.close()


# In[ ]:

# %load outputUpper.txt
first LINE
	second LINE
third


# In[22]:

#수정자, 수정시간 표시하기
import time
fin=open('output.txt','r')
fout=open('outputUppper.txt','w')
editFlag='[jsl edited {}]'.format(time.strftime
                                   ("%Y-%m-%d %H-%M-%S"))
for sentence in fin:
    if sentence.find('line')>=0:
        sentence=sentence.replace('line','LINE')
        sentence=editFlag+sentence
    fout.write(sentence)
fin.close()
fout.close()


# In[ ]:

# %load outputUppper.txt
[jsl edited 2016-06-14 14-46-41]first LINE
[jsl edited 2016-06-14 14-46-41]	second LINE
third


# In[ ]:

## 파일-3: 2차원 데이터를 파일로 쓰기


# In[ ]:



