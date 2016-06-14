{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# 6. 데이터구조\n",
    "\n",
    "## 6.1 학습내용\n",
    "\n",
    "### 6.1.1 목표\n",
    "\n",
    "* 데이터구조를 사용하여 프로그램할 수 있다.\n",
    "* 데이터구조\n",
    "    * list\n",
    "    * tuple\n",
    "    * set\n",
    "    * dictionary\n",
    "* n차원의 구성\n",
    "    * 1차원, 2차원, n차원\n",
    "    * n차원의 반복문\n",
    "\n",
    "### 6.1.2 문제\n",
    "\n",
    "* 데이터구조-1 4로 나누어지고 5로 나누어지지 않는 수 골라서 배열에 넣기.\n",
    "* 데이터구조-2 거북이 트랙을 저장하기\n",
    "* 데이터구조-3 도형을 데이터로 저장하기\n",
    "* 데이터구조-4 거북이가 걸어간 트랙을 다시 걷게 하기\n",
    "* 데이터구조-5 문자열에서 문자를 세기\n",
    "* 데이터구조-6 문자열에 포함된 문자와 숫자의 개수 세기\n",
    "* 데이터구조-7 자신과 친구의 방에 있는 가전제품을 10개 이상 나열해서, 차이 구하기.\n",
    "* 데이터구조-8 광화문 반경에서 가까운 역 찾기.\n",
    "* 데이터구조-9 서울에 거주하는 남녀의 구별 합계와 평균구하기\n",
    "* 데이터구조-10 커피에 Milk를 추가하는 비율 구하기\n",
    "* 데이터구조-11 성적 평균, 합계 구하기.\n",
    "* 데이터구조-12 비틀즈 랫잇비 가사에서 자주 등장하는 단어 구하기.\n",
    "* 데이터구조-13 시간표를 데이터구조로 저장하기\n",
    "\n",
    "### 6.1.3 연습문제\n",
    "\n",
    "* 서울 학교생활 만족도 평균 구하기.\n",
    "* 대통령 연설에서 자주 등장하는 단어 차이 분석하기. 단어빈도 그래프 그리기.\n",
    "* (자습) 이메일 자주 보내는 사람 찾기."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6.2 환경\n",
    "\n",
    "* plantuml 설정\n",
    "    * plantuml.jar 설정 확인\n",
    "    * 경로설정 확인"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/Users/media/Code/git/p2/lib\n",
      "The environment variable GRAPHVIZ_DOT has been set to /opt/local/bin/dot\n",
      "Dot executable is /opt/local/bin/dot\n",
      "Dot version: dot - graphviz version 2.38.0 (20140413.2041)\n",
      "Installation seems OK. File generation OK\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import glob\n",
    "\n",
    "mywd=%pwd\n",
    "myplantdir=os.path.join(mywd,'lib')\n",
    "mydotdir=!which dot\n",
    "mydot=mydotdir[0]\n",
    "# mydot=\"C:\\\\Program Files (x86)\\\\Graphviz2.38\\\\bin\\\\dot.exe\"\n",
    "\n",
    "# plantuml.jar파일이 존재하는지 확인한후, 테스트\n",
    "%cd {myplantdir}\n",
    "glob.glob(r'./*.jar')\n",
    "# dot 실행파일이 저장된 곳을 인식 못하는 경우, Python명령어를 이용해 환경변수를 설정할 수 있다.\n",
    "os.environ['GRAPHVIZ_DOT']=mydot\n",
    "# 리눅스 예: 앞 느낌표는 쉘 명령어. {myplantdir}는 쉘에서 변수값을 읽어오는 것.\n",
    "!java -jar {myplantdir}/plantuml.jar -testdot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Installed plantuml_magics.py. To use it, type:\n",
      "  %load_ext plantuml_magics\n"
     ]
    }
   ],
   "source": [
    "%install_ext https://raw.githubusercontent.com/sberke/ipython-plantuml/master/plantuml_magics.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "%load_ext plantuml_magics"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6.3 데이터구조란?\n",
    "\n",
    "### 6.3.1 왜 필요할까?\n",
    "\n",
    "* 2개 이상의 연관된 값을 저장하기 위해서 사용한다.\n",
    "    * 변수는 2개 이상의 값을 동시에 저장하지 못한다. 데이터구조는 2개 이상을 저장할 수 있다.\n",
    "    * 값을 저장해서 사용하는 예를 설명한다.\n",
    "        * 1부터 10까지의 수를 저장하는 경우\n",
    "        * for 반복문을 이용해서 쉽게 출력할 수 있다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 4 5 6 7 8 9 10\n"
     ]
    }
   ],
   "source": [
    "for i in range(1,11):\n",
    "    print i,"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 1~10까지의 숫자를 저장해서 다시 사용한다고 생각해보자.\n",
    "* 어떻게 저장할 것인가?\n",
    "* 앞서 배웠던 변수를 사용해보자. 그렇다면 10개의 변수가 필요하다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "x10=10\n",
    "x9=9\n",
    "x8=8\n",
    "x7=7\n",
    "x6=6\n",
    "x5=5\n",
    "x4=4\n",
    "x3=3\n",
    "x2=2\n",
    "x1=1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* x1 ~ x10, 10개의 변수를 이용해서 숫자를 저장했다.\n",
    "* 출력은 어떻게 할 것인가? 하나씩 한다면 모두 20줄의 명령어가 필요하다. 중복이 많아서 낭비적이다.\n",
    "* 중복을 줄이는 방법이 있을까? 데이터구조를 이용하면 해결할 수 있다."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* List라고 하는 데이터구조를 사용해보자.\n",
    "* 아래와 같이, 변수명에 대괄호를 이용하여 번호를 매기고 (인덱스라고 한다), 연관된 값을 저장한다.\n",
    "* 오류가 났다. 그 이유는 선언을 하지 않았기 때문이다 ('NameError')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'x' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-4-ac371d512433>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mx\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'x' is not defined"
     ]
    }
   ],
   "source": [
    "x[0]=0"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 사용하기 전 사용하려는 자료형을 선언하는 것이 필요하다.\n",
    "    * x=list() 또는 x=[]라고 선언한다.\n",
    "    * 즉, x에는 리스트 구조로 데이터를 저장한다는 의미이다.\n",
    "    * 그러나 리스트 구조에 저장되는 데이터의 자료형은 선언하지 않는다.\n",
    "    * 숫자, 문자 어느 자료형을 사용할 수 있다. Python과 같은 스크립트언어의 특징을 보여준다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "x=list()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 선언한 List에 데이터를 넣을 경우, append()함수를 사용한다.\n",
    "* append()는 데이터를 맨 뒤에 추가한다는 의미로, 순서가 있는 리스트 데이터구조의 성격을 나타내고 있다고 이해한다.\n",
    "* 아래는 x가 리스트 구조를 사용한다고 선언하고, 1을 저장하였다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1]\n"
     ]
    }
   ],
   "source": [
    "x=list()\n",
    "x.append(1)\n",
    "print x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 이제 10개의 값을 저장해보자."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n"
     ]
    }
   ],
   "source": [
    "x=list()\n",
    "x.append(1)\n",
    "x.append(2)\n",
    "x.append(3)\n",
    "x.append(4)\n",
    "x.append(5)\n",
    "x.append(6)\n",
    "x.append(7)\n",
    "x.append(8)\n",
    "x.append(9)\n",
    "x.append(10)\n",
    "print x,"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 동일한 변수명으로 연관된 값을 묶어 저장하는 것은 만족스럽지만, 아직 10줄이나 반복하는 것은 문제이다.\n",
    "* 이 때 숫자를 하나씩 증가하여 저장하는 패턴을 볼 수 있다. 반복문을 사용하여 중복을 제거할 수 있다.\n",
    "    * x의 리스트 데이터구조를 선언하고 사용.\n",
    "    * index방식으로는 list에 데이터를 넣지 못함. 값을 넣으려고 하지만 그 배열항목이 존재하지 않음 (IndexError)\n",
    "    * append()함수를 이용한다. 이와 같이 데이터구조 별로 특징적인 1) 데이터를 생성하고, 2) 읽고, 3) 수정하고, 4) 삭제하는 방식이 있다는 것을 유의하자."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "list assignment index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-7-aa2b70af590f>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mlist\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m11\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m     \u001b[0mx\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;32mprint\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mIndexError\u001b[0m: list assignment index out of range"
     ]
    }
   ],
   "source": [
    "x=list()\n",
    "for i in range(1,11):\n",
    "    x[i]=i\n",
    "print x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n"
     ]
    }
   ],
   "source": [
    "x=list()\n",
    "for i in range(1,11):\n",
    "    x.append(i)\n",
    "print x,"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* print 명령문을 들여써서, for의 body에 속하게 하면 데이터가 추가되는 과정을 볼 수 있다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1]\n",
      "[1, 2]\n",
      "[1, 2, 3]\n",
      "[1, 2, 3, 4]\n",
      "[1, 2, 3, 4, 5]\n",
      "[1, 2, 3, 4, 5, 6]\n",
      "[1, 2, 3, 4, 5, 6, 7]\n",
      "[1, 2, 3, 4, 5, 6, 7, 8]\n",
      "[1, 2, 3, 4, 5, 6, 7, 8, 9]\n",
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n"
     ]
    }
   ],
   "source": [
    "x=list()\n",
    "for i in range(1,11):\n",
    "    x.append(i)\n",
    "    print x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 다음 프로그램은 인덱스를 이용하여 출력하는 사례이다. 그러나 오류가 발생한다. 그 이유는 무엇일까?\n",
    "* range명령문에 따라 1부터 시작한다.\n",
    "    ```\n",
    "    x.append(1)\n",
    "    ```\n",
    "* 이 명령문은 x[0]에 1을 저장한다는 의미이다.\n",
    "* 그 다음 명령어는 없는 데이터를 출력하려고 하기 때문에 index범위초과 오류가 발생한다.\n",
    "    ```\n",
    "    print x[1]\n",
    "    ```\n",
    "* 이 오류는 논리적으로 생각해서, range명령문을 0부터 시작하면 해결할 수 있다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-10-f3149a16c5e2>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m11\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m     \u001b[0mx\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m     \u001b[0;32mprint\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "x=list()\n",
    "for i in range(1,11):\n",
    "    x.append(i)\n",
    "    print x[i],"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1 2 3 4 5 6 7 8 9\n"
     ]
    }
   ],
   "source": [
    "x=list()\n",
    "for i in range(0,10):\n",
    "    x.append(i)\n",
    "    print x[i],"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 주의: 사람은 1부터 숫자를 세는 것이 보통이지만, 컴퓨터는 0부터 시작한다.\n",
    "* 리스트는 값을 저장할 때 대괄호를 사용한다.\n",
    "* 대괄호에 들어가는 수를 인덱스 index라고 한다.\n",
    "* 인덱스는 정수 값. 0부터 시작!\n",
    "    * 음수는 사용하지 않는다.\n",
    "    * 소수도 사용하지 않는다.\n",
    "    * 일반적으로 문자를 사용하지 않는다 (Python에서는 'associative array'라고 사용한다.)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 데이터구조는 변수와 무엇이 다른가?\n",
    "    * 변수x는 1개 값만 저장. 1~10 값을 모두 저장하려면 변수로는 불가능.\n",
    "    * 변수는 값을 1개만 갖는다.\n",
    "    * 변수에 1 ~ 10의 값은 저장할 수 없슴. 저장공간이 1개이기 때문에, 가능하지 못함.\n",
    "    * 새로운 값을 저장하면, 이전의 값은 없어짐.\n",
    "    * 이런 경우 배열을 이용하면, 동일한 변수명으로 여러 값을 묶어서 저장할 수 있슴."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 6.3.2 데이터구조의 선언\n",
    "\n",
    "* 지금까지 데이터구조가 필요한 이유를 설명하였다. 변수는 연관된 값을 묶어서 저장하지 못한다. 리스트의 예로 설명하였다.\n",
    "* 스크립트언어는 컴파일언어와 달리 대개 선언을 하지 않지 않음. Python도 변수의 자료형을 선언하지 않아도 되는 loosely coupled 언어.\n",
    "    * 그러나 데이터구조는 선언이 필요하다.\n",
    "    * 어떤 구조를 사용할 것인지 미리 선언하도록 한다.\n",
    "    * 자료에 저장되는 데이터형은 명시하지 않아도 된다.\n",
    "    * 리스트를 사용하는 예를 들어보자. 다음과 같이 선언하고 사용한다. 그러나 d에 숫자 또는 문자가 저장할지 밝히지 않는다.\n",
    "    ```\n",
    "    x=list()\n",
    "    ```\n",
    "* 자료형 (data type)을 미리 선언하는 것은 메모리공간을 확보하기 위함.\n",
    "* 데이터구조의 선언은 여러 데이터를 저장하겠다는 의미.\n",
    "    * 따라서 2개 이상을 어떤 방식으로 저장할 것인지 미리 선언하는 것이 필요."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### 6.3.3. 많이 사용하는 데이터구조\n",
    "\n",
    "* 많이 사용하는 데이터구조는 다음과 같다.\n",
    "\n",
    "데이터구조 | 특징 | 선언 | index\n",
    "----|---|---|---\n",
    "list (array)| 배열. 순서가 있슴. 데이터 수정가능 (mutable) | x=list() or x=[] | yes (예: x[0])\n",
    "tuple | 수정할 수 없는 배열 (immutable) | x=tuple() or x=() | yes (예: x[0])\n",
    "set | 수학의 세트 | x=set() | no\n",
    "dictionary | key-value. 배열과 비슷. 문자를 인덱스로 사용할 수 있슴. | x=dict() or x={} | no\n",
    "\n",
    "    * list는 순서가 있어서, 정수 인덱스를 사용하여 읽거나, 수정할 수 있다.\n",
    "    * tuple은 list이지만, 데이터처리를 빠르게하기 위해, 값이 정해지면 수정할 수 없는 특징.\n",
    "    * set은 순서가 없어 인덱스를 사용하지 못함. 데이터중복이 없고 하나만 있다는 점에서 key와 같은 의미 (key로만 구성이 된 dictionary)\n",
    "    * dictionary는 key-value가 1:1로 구성함. 특정 key가 어떤 값을 갖는지 사전식으로 저장.\n",
    "\n",
    "데이터구조 | 생성 | 읽기 | 수정 | 삭제\n",
    "----|---|---|---|---\n",
    "list (array)| append() | index | index (또는 insert() | remove() (pop()은 예외적)\n",
    "tuple | 선언하면서 데이터 생성 | index | 불가능 | size줄이지 못함\n",
    "set | add() | index | index | pop()\n",
    "dictionary | key-value. update() | key-value | key-value | \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false,
    "scrolled": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "list:  <type 'list'>\n",
      "tuple:  <type 'tuple'>\n",
      "set:  <type 'set'>\n",
      "dict:  <type 'dict'>\n"
     ]
    }
   ],
   "source": [
    "# 변수를 선언하고 자료형 확인하기.\n",
    "x=list()\n",
    "print \"list: \",type(x)\n",
    "x=tuple()\n",
    "print \"tuple: \",type(x)\n",
    "x=set()\n",
    "print \"set: \",type(x)\n",
    "x=dict()\n",
    "print \"dict: \",type(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 리스트\n",
    "\n",
    "* 리스트는 설명하였다.\n",
    "* 생성, 읽기, 수정, 삭제를 차례로 실행해 본다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "x=list()\n",
    "for i in range(0,10):\n",
    "    x.append(i)\n",
    "print x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "print x[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 3.141592653589793, 2, 3, 4, 5, 6, 7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "x.insert(2,math.pi)\n",
    "print x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 3.14, 2, 3, 4, 5, 6, 7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "x[2]=3.14\n",
    "print x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* remove()는 값을 삭제한다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "x.remove(3.14)\n",
    "print x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 튜플\n",
    "\n",
    "* 튜플은 데이터가 수정할 수 없기 때문에 추가, 삭제, 수정하는 방법이 없다.\n",
    "* 튜플은 선언하면서 생성한다.\n",
    "* 튜플은 생성하고 나면, 수정하지 않고 사용한다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)\n"
     ]
    }
   ],
   "source": [
    "x=(1,2,3,4,5,6,7,8,9,10)\n",
    "print x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "print x[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Set\n",
    "\n",
    "* set은 데이터를 추가할 때는 add()를 사용한다.\n",
    "* 순서가 없기 때문에 add()를 사용한다. list는 순서가 있어서 append()를 사용한다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x=set()\n",
    "for i in range(0,10):\n",
    "    x.add(i)\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* set는 key값을 저장한다.\n",
    "* key값이란 unique, 중복 값이 존재하지 않는다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "set([1, 2, 10, 5])\n"
     ]
    }
   ],
   "source": [
    "x=set([1,1,1,2,2,5,10])\n",
    "print x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.pop()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Dictinoary\n",
    "\n",
    "* dict는 키와 값으로 구성한다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'n': 1}\n"
     ]
    }
   ],
   "source": [
    "x=dict()\n",
    "x.update({'n':1})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "x=({'name':'jsl','stno':201611111})\n",
    "print x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "print x['stno']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 지금까지 하나씩 데이터구조를 훓어보았다.\n",
    "* 사용하는 괄호가 서로 다르다는 점에 주목하자.\n",
    "    * list []\n",
    "    * tuple ()\n",
    "    * set ([])\n",
    "    * dictionary {key:value}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 데이터구조-1\n",
    "\n",
    "### 1-1. 배열 생성하기\n",
    "* 1 ~ 1000의 수 가운데 4로 나누어지고 5로 나누어지지 않는 수를 골라서 리스트에 넣기.\n",
    "\n",
    "### 1-2. 배열에 있는 수의 합계를 구하기\n",
    "\n",
    "* 1-1에서 만든 배열을 사용해서 합계를 구한다.\n",
    "* 1-2에서 반복문을 사용해서 문제를 푼다.\n",
    "\n",
    "* 프로그래밍 요소\n",
    "    * List\n",
    "    * 다른 구조와의 차이를 이해, 어느 경우 사용해야 좋은지 이해\n",
    "    * 함수는 재사용가능한 모듈인 합계만 만듦.\n",
    "* 주의\n",
    "    * 자료구조 형을 미리 선언해야 함.\n",
    "    * 배열요소를 입력할 경우, 없는 요소를 넣지 못함 (예: x=[]하면 비어 있는 List. 이 경우, x[0]=1하면 오류)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "image/svg+xml": [
       "<svg height=\"893px\" style=\"width:274px;height:893px;\" version=\"1.1\" viewBox=\"0 0 274 893\" width=\"274px\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\"><defs><filter height=\"300%\" id=\"f1\" width=\"300%\" x=\"-1\" y=\"-1\"><feGaussianBlur result=\"blurOut\" stdDeviation=\"2.0\"/><feColorMatrix in=\"blurOut\" result=\"blurOut2\" type=\"matrix\" values=\"0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .4 0\"/><feOffset dx=\"4.0\" dy=\"4.0\" in=\"blurOut2\" result=\"blurOut3\"/><feBlend in=\"SourceGraphic\" in2=\"blurOut3\" mode=\"normal\"/></filter></defs><g><ellipse cx=\"146\" cy=\"20\" fill=\"#000000\" filter=\"url(#f1)\" rx=\"10\" ry=\"10\" style=\"stroke: none; stroke-width: 1.0;\"/><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"62\" x=\"115\" y=\"50\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"42\" x=\"125\" y=\"71.6016\">set i=0</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"87\" x=\"102.5\" y=\"104.1328\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"67\" x=\"112.5\" y=\"125.7344\">initialize list</text><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"81.5,202.2656,210.5,202.2656,222.5,214.2656,210.5,226.2656,81.5,226.2656,69.5,214.2656,81.5,202.2656\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"11\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"129\" x=\"81.5\" y=\"218.4229\">i divisable by 4, not by 5</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"99\" x=\"10\" y=\"236.2656\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"79\" x=\"20\" y=\"257.8672\">add i to array</text><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"146,276.3984,158,288.3984,146,300.3984,134,288.3984,146,276.3984\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"77\" x=\"107.5\" y=\"335.3984\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"57\" x=\"117.5\" y=\"357\">add 1 to i</text><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"146,158.2656,158,170.2656,146,182.2656,134,170.2656,146,158.2656\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"129.5,389.5313,162.5,389.5313,174.5,401.5313,162.5,413.5313,129.5,413.5313,117.5,401.5313,129.5,389.5313\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"11\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"33\" x=\"129.5\" y=\"405.6885\">i&lt;101</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"67\" x=\"112.5\" y=\"433.5313\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"47\" x=\"122.5\" y=\"455.1328\">print list</text><rect fill=\"#FFFFFF\" filter=\"url(#f1)\" height=\"367.5313\" style=\"stroke: #000000; stroke-width: 2.0;\" width=\"173.5\" x=\"54.5\" y=\"478.6641\"/><path d=\"M87.5,479.6641 L87.5,485.6641 L77.5,495.6641 L54.5,495.6641 \" fill=\"#FFFFFF\" style=\"stroke: #000000; stroke-width: 2.0;\"/><text fill=\"#000000\" font-family=\"Serif\" font-size=\"14\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"23\" x=\"57.5\" y=\"490.1641\">sum</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"62\" x=\"115\" y=\"512.6641\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"42\" x=\"125\" y=\"534.2656\">sum=0</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"144\" x=\"74\" y=\"581.7969\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"124\" x=\"84\" y=\"603.3984\">maxiter=length of list</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"115\" x=\"88.5\" y=\"698.9297\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"95\" x=\"98.5\" y=\"720.5313\">sum=sum+list[i]</text><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"119.5,650.9297,172.5,650.9297,184.5,662.9297,172.5,674.9297,119.5,674.9297,107.5,662.9297,119.5,650.9297\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"11\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"53\" x=\"119.5\" y=\"667.0869\">i&lt;maxiter</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"75\" x=\"108.5\" y=\"792.0625\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"55\" x=\"118.5\" y=\"813.6641\">print sum</text><ellipse cx=\"146\" cy=\"876.1953\" fill=\"none\" filter=\"url(#f1)\" rx=\"10\" ry=\"10\" style=\"stroke: #000000; stroke-width: 1.0;\"/><ellipse cx=\"146.5\" cy=\"876.6953\" fill=\"#000000\" filter=\"url(#f1)\" rx=\"6\" ry=\"6\" style=\"stroke: none; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"146\" x2=\"146\" y1=\"30\" y2=\"50\"/><polygon fill=\"#A80036\" points=\"142,40,146,50,150,40,146,44\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"146\" x2=\"146\" y1=\"84.1328\" y2=\"104.1328\"/><polygon fill=\"#A80036\" points=\"142,94.1328,146,104.1328,150,94.1328,146,98.1328\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"69.5\" x2=\"59.5\" y1=\"214.2656\" y2=\"214.2656\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"59.5\" x2=\"59.5\" y1=\"214.2656\" y2=\"236.2656\"/><polygon fill=\"#A80036\" points=\"55.5,226.2656,59.5,236.2656,63.5,226.2656,59.5,230.2656\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"222.5\" x2=\"232.5\" y1=\"214.2656\" y2=\"214.2656\"/><polygon fill=\"#A80036\" points=\"228.5,241.332,232.5,251.332,236.5,241.332,232.5,245.332\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"232.5\" x2=\"232.5\" y1=\"214.2656\" y2=\"288.3984\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"232.5\" x2=\"158\" y1=\"288.3984\" y2=\"288.3984\"/><polygon fill=\"#A80036\" points=\"168,284.3984,158,288.3984,168,292.3984,164,288.3984\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"59.5\" x2=\"59.5\" y1=\"270.3984\" y2=\"288.3984\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"59.5\" x2=\"134\" y1=\"288.3984\" y2=\"288.3984\"/><polygon fill=\"#A80036\" points=\"124,284.3984,134,288.3984,124,292.3984,128,288.3984\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"146\" x2=\"146\" y1=\"300.3984\" y2=\"335.3984\"/><polygon fill=\"#A80036\" points=\"142,325.3984,146,335.3984,150,325.3984,146,329.3984\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"146\" x2=\"146\" y1=\"182.2656\" y2=\"202.2656\"/><polygon fill=\"#A80036\" points=\"142,192.2656,146,202.2656,150,192.2656,146,196.2656\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"174.5\" x2=\"269.5\" y1=\"401.5313\" y2=\"401.5313\"/><polygon fill=\"#A80036\" points=\"265.5,319.8984,269.5,309.8984,273.5,319.8984,269.5,315.8984\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"269.5\" x2=\"269.5\" y1=\"170.2656\" y2=\"401.5313\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"269.5\" x2=\"158\" y1=\"170.2656\" y2=\"170.2656\"/><polygon fill=\"#A80036\" points=\"168,166.2656,158,170.2656,168,174.2656,164,170.2656\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"146\" x2=\"146\" y1=\"369.5313\" y2=\"389.5313\"/><polygon fill=\"#A80036\" points=\"142,379.5313,146,389.5313,150,379.5313,146,383.5313\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"146\" x2=\"146\" y1=\"138.2656\" y2=\"158.2656\"/><polygon fill=\"#A80036\" points=\"142,148.2656,146,158.2656,150,148.2656,146,152.2656\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"146\" x2=\"146\" y1=\"413.5313\" y2=\"433.5313\"/><polygon fill=\"#A80036\" points=\"142,423.5313,146,433.5313,150,423.5313,146,427.5313\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"146\" x2=\"146\" y1=\"546.7969\" y2=\"581.7969\"/><polygon fill=\"#A80036\" points=\"142,571.7969,146,581.7969,150,571.7969,146,575.7969\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"146\" x2=\"146\" y1=\"674.9297\" y2=\"698.9297\"/><polygon fill=\"#A80036\" points=\"142,688.9297,146,698.9297,150,688.9297,146,692.9297\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"146\" x2=\"146\" y1=\"733.0625\" y2=\"745.0625\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"146\" x2=\"215.5\" y1=\"745.0625\" y2=\"745.0625\"/><polygon fill=\"#A80036\" points=\"211.5,713.9961,215.5,703.9961,219.5,713.9961,215.5,709.9961\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"215.5\" x2=\"215.5\" y1=\"662.9297\" y2=\"745.0625\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"215.5\" x2=\"184.5\" y1=\"662.9297\" y2=\"662.9297\"/><polygon fill=\"#A80036\" points=\"194.5,658.9297,184.5,662.9297,194.5,666.9297,190.5,662.9297\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"107.5\" x2=\"76.5\" y1=\"662.9297\" y2=\"662.9297\"/><polygon fill=\"#A80036\" points=\"72.5,699.9961,76.5,709.9961,80.5,699.9961,76.5,703.9961\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"76.5\" x2=\"76.5\" y1=\"662.9297\" y2=\"757.0625\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"76.5\" x2=\"146\" y1=\"757.0625\" y2=\"757.0625\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"146\" x2=\"146\" y1=\"757.0625\" y2=\"792.0625\"/><polygon fill=\"#A80036\" points=\"142,782.0625,146,792.0625,150,782.0625,146,786.0625\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"146\" x2=\"146\" y1=\"615.9297\" y2=\"650.9297\"/><polygon fill=\"#A80036\" points=\"142,640.9297,146,650.9297,150,640.9297,146,644.9297\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"146\" x2=\"146\" y1=\"467.6641\" y2=\"512.6641\"/><polygon fill=\"#A80036\" points=\"142,502.6641,146,512.6641,150,502.6641,146,506.6641\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"146\" x2=\"146\" y1=\"826.1953\" y2=\"866.1953\"/><polygon fill=\"#A80036\" points=\"142,856.1953,146,866.1953,150,856.1953,146,860.1953\" style=\"stroke: #A80036; stroke-width: 1.0;\"/></g></svg>"
      ],
      "text/plain": [
       "<IPython.core.display.SVG object>"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%plantuml\n",
    "@startuml\n",
    "start\n",
    ":set i=0;\n",
    ":initialize list;\n",
    "repeat\n",
    "if(i divisable by 4, not by 5)\n",
    ":add i to array;\n",
    "endif\n",
    ":add 1 to i;\n",
    "repeat while(i<101)\n",
    ":print list;\n",
    "partition sum {\n",
    "    :sum=0;\n",
    "    :maxiter=length of list;\n",
    "    while(i<maxiter)\n",
    "    :sum=sum+list[i];\n",
    "    endwhile\n",
    "    :print sum;\n",
    "}\n",
    "stop\n",
    "@enduml"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 조건에 맞는 x를 출력할 수 있다.\n",
    "* 그러나 print명령문을 사용하면 출력만 하고, 값이 사라진다. 저장되지 않는다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4 8 12 16 24 28 32 36 44 48 52 56 64 68 72 76 84 88 92 96\n"
     ]
    }
   ],
   "source": [
    "x=list()\n",
    "for x in range(1,100):\n",
    "    if(x%4==0) and (x%5!=0):\n",
    "        print x,"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* mylist를 이용해서 값을 저장한다.\n",
    "* mylist는 리스트 데이터구조를 사용한다. 따라서 append()함수를 사용하여 값을 추가할 수 있다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 8, 12, 16, 24, 28, 32, 36, 44, 48, 52, 56, 64, 68, 72, 76, 84, 88, 92, 96]\n"
     ]
    }
   ],
   "source": [
    "mylist=[]\n",
    "for i in range(1,100):\n",
    "    if(i%4==0) and (i%5!=0):\n",
    "        mylist.append(i)\n",
    "print mylist"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* for문을 사용해서 저장된 값의 합계를 구한다.\n",
    "* 합계를 구하려면, 데이터구조에 몇 개의 자료가 있는지 알아야 한다.\n",
    "* 몇 개를 출력하나\n",
    "    ```\n",
    "    for j in range(0,??\n",
    "    ```\n",
    "* len()함수를 사용하면 데이터를 가지고 있는지, 몇 개 있는지 알 수 있다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n",
      "empty\n",
      "length empty\n"
     ]
    }
   ],
   "source": [
    "x=[]\n",
    "print x\n",
    "if not x:\n",
    "    print \"empty\"\n",
    "else:\n",
    "    print \"not empty\"\n",
    "\n",
    "# 다른 방식: 그래도 위 방식이 더 낫다.\n",
    "if len(x)==0:\n",
    "    print \"length empty\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "1000\n"
     ]
    }
   ],
   "source": [
    "# 학습을 위해 maxiter index를 사용.\n",
    "sum=0\n",
    "maxiter=len(mylist)\n",
    "print maxiter\n",
    "for i in range(0,maxiter):\n",
    "    sum=sum+mylist[i]\n",
    "print sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1000\n"
     ]
    }
   ],
   "source": [
    "#보다 간단하게. 배열의 길이를 별도로 세지 않음.\n",
    "sum=0\n",
    "for i in mylist:\n",
    "    sum+=i\n",
    "print sum"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 함수로\n",
    "\n",
    "* 가능한 오류 생각해보기 - 배열이 비어 있는 경우\n",
    "* len 길이로 확인하지만 더 간단한 표현으로 가능 (아래 참조)\n",
    "* 합계만 함수로 만듦 - 어느 List나 입력하면 합계 출력하는 기능.\n",
    "\n",
    "* 함수로 만들어 보기\n",
    "    * 함수이름 sumList\n",
    "    * 입력 리스트\n",
    "    * 출력 합계값\n",
    "    ```\n",
    "    def sumList(aList):\n",
    "        ...\n",
    "        return sum\n",
    "    def lab6():\n",
    "        x=[1,2,3]\n",
    "        mysum=sumList(x)\n",
    "        print mysum\n",
    "    def main()\n",
    "        lab6()\n",
    "    ```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "def sumList(aList):\n",
    "    mySum=0\n",
    "    for i in aList:\n",
    "        mySum+=i\n",
    "    return mySum\n",
    "\n",
    "def lab6():\n",
    "    \"\"\"programmin is really ha ha ha fun\"\"\"\n",
    "    myList=[]\n",
    "    for i in range(1,1000):\n",
    "        if(i%4==0) and (i%5!=0):\n",
    "            myList.append(i)\n",
    "    total=sumList(myList)\n",
    "    print \"total: \", total\n",
    "\n",
    "def main():\n",
    "    lab6()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 이와 같이 구조를 만들면, 보다 큰 프로그램을 만들 때 유용하다.\n",
    "* 호출할 때는 main()을 사용한다.\n",
    "* 함수이름 밑 따옴표는 도움말을 작성하는 것이고, help로 확인할 수 있다.\n",
    "* 함수의 실행순서\n",
    "    * main()을 호출하면 줄16으로 간다.\n",
    "    * 그리고 줄17의 lab6()이 실행된다.\n",
    "    * 줄7의 lab6()이 실행된다.\n",
    "    * 줄8부터 실행된다.\n",
    "    * 줄 13이 실행된다. 거기서 만나는 줄1 함수 sumList()이 실행된다.\n",
    "    * 이와 같이 사람은 줄1부터 읽어내려가지만, 컴퓨터는 함수로 구성하면, 함수의 순서에 따라 실행해나간다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total:  100000\n"
     ]
    }
   ],
   "source": [
    "main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on function lab6 in module __main__:\n",
      "\n",
      "lab6()\n",
      "    programmin is really ha ha ha fun\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(lab6)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 데이터구조-2: 거북이 트랙을 저장하기\n",
    "\n",
    "* 자신이 만들었던 drawSquareAt()을 수정해서, 사각형의 모서리 위치를 저장한다.\n",
    "* 함수\n",
    "    * 함수명 drawSquareAtSave()\n",
    "    * 입력\n",
    "        * 그림의 크기 size\n",
    "        * 위치 pos\n",
    "    * 출력 tracks\n",
    "\n",
    "* 프로그래밍 요소\n",
    "    * 사각형 모서리는 4개의 점을 가진다. 용도에 맞는 데이터구조를 선택한다.\n",
    "    * 자료는 모든 위치(x,y)를 가지고 있는 목록이다\n",
    "\n",
    "* 생각해보기\n",
    "    * tracks를 전역으로 할지, 지역으로 할지\n",
    "    * list를 반환하면 출력을 어떻게 하는지?\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 프로그래밍 순서\n",
    "\n",
    "* 앞서 drawSquareAt()을 복사한다.\n",
    "* 먼저 어떤 데이터구조를 사용할지 결정\n",
    "    * 순서가 있는 구조이다. 사각형은 그리는 순서가 있다.\n",
    "    * 걸어간 위치는 하나씩 저장하면서, 자료목록이 늘어난다.\n",
    "    * 리스트는 자료가 추가되면서, 고무줄처럼 늘어날 수 있다.\n",
    "\n",
    "* 선언하는 것을 생각해보자\n",
    "    * 어느 때 선언하면 적당할까?\n",
    "    * 아래 for문 앞 4,5줄 사이\n",
    "        ```\n",
    "        tracks=list()\n",
    "        ```\n",
    "* 어느 때 저장하면 적당할까?\n",
    "    * 사각형은 거북이가 사각형 모서리에 멈추는 때 저장한다.\n",
    "    * for문 다음 (line 5) 움직이기 전 (lin6)\n",
    "    * 거북이 위치는 pos()함수로 위치를 읽는다.\n",
    "        ```\n",
    "        tracks.append(t1.pos())\n",
    "        ```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def drawSquareAt(size, pos):\n",
    "    t1.penup()\n",
    "    t1.setpos(pos)\n",
    "    t1.pendown()\n",
    "    for i in range(0,4):\n",
    "        t1.forward(size)\n",
    "        t1.right(90)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(150.00,-100.00), (150.00,-150.00), (100.00,-150.00), (100.00,-100.00)]\n"
     ]
    }
   ],
   "source": [
    "def drawSquareAtAndSave(size, pos):\n",
    "    t1.penup()\n",
    "    t1.setpos(pos)\n",
    "    t1.pendown()\n",
    "    tracks=list()\n",
    "    for i in range(0,4):\n",
    "        tracks.append(t1.pos())\n",
    "        t1.forward(size)\n",
    "        t1.right(90)\n",
    "    return tracks\n",
    "\n",
    "import turtle\n",
    "wn=turtle.Screen()\n",
    "t1=turtle.Turtle()\n",
    "mytracks=drawSquareAtAndSave(50, (100,-100))\n",
    "print mytracks"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 구조를 만들어 준다.\n",
    "    * 사용하는 부분을 함수로 만들어 추가한다.\n",
    "    * global은 전역변수를 말한다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "global t1\n",
    "def drawSquareAtAndSave(size, pos):\n",
    "    t1.penup()\n",
    "    t1.setpos(pos)\n",
    "    t1.pendown()\n",
    "    tracks=list()\n",
    "    for i in range(0,4):\n",
    "        tracks.append(t1.pos())\n",
    "        t1.forward(size)\n",
    "        t1.right(90)\n",
    "    return tracks\n",
    "\n",
    "def lab6a():\n",
    "    global t1\n",
    "    import turtle\n",
    "    wn=turtle.Screen()\n",
    "    t1=turtle.Turtle()\n",
    "    mytracks=drawSquareAtAndSave(50, (100,-100))\n",
    "    print mytracks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(100.00,-100.00), (150.00,-100.00), (150.00,-150.00), (100.00,-150.00)]\n"
     ]
    }
   ],
   "source": [
    "lab()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 데이터구조-3: 도형을 데이터구조로 저장하고 그리기\n",
    "\n",
    "### 3-1 도형을 데이터구조로 저장하기\n",
    "* 자신이 사각형 위치를 임의로 데이터구조로 생성해서 저장한다.\n",
    "\n",
    "### 3-1 저장한 데이터구조를 사용해서 사각형을 그린다.\n",
    "* 사각형 위치가 저장된 데이터구조를 함수에 전달한다.\n",
    "* 함수\n",
    "    * 함수명 drawSquareFrom()\n",
    "    * 입력 argument\n",
    "        * 4점을 가지고 있는 구조 tracks\n",
    "    * 출력 none\n",
    "\n",
    "* 프로그래밍 요소\n",
    "    * 데이터구조를 생성할 수 있다.\n",
    "    * 데이터구조를 함수에 전달할 수 있다.\n",
    "    * 전달하는 값의 의미가 컴퓨터에서는 특별하다.\n",
    "    * 값이 전달되는 것인지, 값이 저장된 메모리 값이 전달되는지 구별한다. 지금은 자세한 설명을 생략한다.\n",
    "    * 값이 전달되는 것을 (pass by value), 메모리 값이 전달되는 것과 (pass by reference)와 구별한다.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(100, 100), (200, 100), (200, 200), (100, 200), (100, 100)]\n",
      "<type 'list'>\n"
     ]
    }
   ],
   "source": [
    "tracks=[(100,100), (200,100), (200,200), (100,200), (100,100)]\n",
    "print tracks\n",
    "print type(tracks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* tracks는 튜플 데이터구조를 사용하고 있다.\n",
    "* tracks를 출력해보자\n",
    "    * range(0,4)를 이용해서 사각형 위치를 출력한다.\n",
    "    * range(0,4)는 변수 값을 사용하기 때문에 4개의 점이 아닌 경우 오류가 발생할 수 있다.\n",
    "    * range(0,len(tracks))는 크기가 변해도 사용할 수 있다는 장점이 있다.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(100, 100) (200, 100) (200, 200) (100, 200)\n"
     ]
    }
   ],
   "source": [
    "for t in range(0,4):\n",
    "    print tracks[t],"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(100, 100) (200, 100) (200, 200) (100, 200) (100, 100)\n"
     ]
    }
   ],
   "source": [
    "for t in range(0,len(tracks)):\n",
    "    print tracks[t],"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 리스트 구조를 사용할 수 있다.\n",
    "* tracks는 tuple로 선언되어 있고, 이를 수정하지 못한다.\n",
    "* 리스트 데이터를 넣으려고 하면 오류가 발생한다 ('TypeError')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "list indices must be integers, not tuple",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-47-f7b05b21c67b>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mtracks\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m100\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m100\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;36m200\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m100\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;36m100\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m200\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;36m100\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m200\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;36m100\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m100\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: list indices must be integers, not tuple"
     ]
    }
   ],
   "source": [
    "tracks=[[100,100], [200,100] [100,200], [100,200], [100,100]]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 리스트구조를 만들어서 tracks를 사용한다.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[100, 100], [200, 100], [100, 200], [100, 200], [100, 100]]\n",
      "<type 'list'>\n"
     ]
    }
   ],
   "source": [
    "tracks=list()\n",
    "tracks=[[100,100], [200,100], [100,200], [100,200], [100,100]]\n",
    "print tracks\n",
    "print type(tracks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 함수로 만들어 본다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def drawSquareFrom(tracks):\n",
    "    t1.penup()\n",
    "    t1.pendown()\n",
    "    for t in range(0,len(tracks)):\n",
    "        t1.setpos(t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "global t1\n",
    "def drawSquareFrom(tracks):\n",
    "    t1.penup()\n",
    "    t1.pendown()\n",
    "    for t in range(0,len(tracks)):\n",
    "        t1.setpos(t)\n",
    "def lab6b():\n",
    "    global t1\n",
    "    #import turtle\n",
    "    #wn=turtle.Screen()\n",
    "    #t1=turtle.Turtle()\n",
    "    tracks=list()\n",
    "    tracks=[[100,100], [200,100], [200,200], [100,200], [100,100]]\n",
    "    drawSquareFrom(tracks)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "lab6b()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 데이터구조-4: 거북이가 걸어간 트랙을 다시 걷게 하기\n",
    "\n",
    "### 4-1 거북이가 걸어간 트랙을 저장하기\n",
    "\n",
    "* wk2에 작성했던 myMaze.py의 위치를 모두 저장한다.\n",
    "* 함수\n",
    "    * 함수명 saveTracks()\n",
    "    * 입력 none\n",
    "    * 출력 tracks\n",
    "\n",
    "\n",
    "### 4-2 트랙을 자동으로 걷게 하기\n",
    "\n",
    "* 앞서 저장된 트랙을 걷게 한다.\n",
    "* 함수 replayTracks(tracks)\n",
    "    * 입력 mytracks\n",
    "    * 출력\n",
    "\n",
    "* 저장된 위치가 몇 개인지 어떻게 알 수 있을까?\n",
    "    * tracks라는 데이터 구조명을 사용한다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import turtle\n",
    "wn=turtle.Screen()\n",
    "t1=turtle.Turtle()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "tracks=list()\n",
    "\n",
    "t1.speed(1)\n",
    "t1.penup()\n",
    "t1.goto(-400,300)\n",
    "\n",
    "tracks.append(t1.pos())\n",
    "\n",
    "t1.pendown()\n",
    "t1.pencolor(\"Red\")\n",
    "t1.right(90)\n",
    "t1.fd(400)\n",
    "\n",
    "tracks.append(t1.pos())\n",
    "\n",
    "t1.backward(150)\n",
    "\n",
    "tracks.append(t1.pos())\n",
    "\n",
    "t1.left(90)\n",
    "t1.fd(300)\n",
    "\n",
    "tracks.append(t1.pos())\n",
    "\n",
    "t1.left(90)\n",
    "t1.fd(300)\n",
    "\n",
    "tracks.append(t1.pos())\n",
    "\n",
    "t1.back(150)\n",
    "\n",
    "tracks.append(t1.pos())\n",
    "\n",
    "t1.right(90)\n",
    "t1.fd(300)\n",
    "\n",
    "tracks.append(t1.pos())\n",
    "\n",
    "t1.left(90)\n",
    "t1.right(90)\n",
    "t1.right(90)\n",
    "t1.fd(200)\n",
    "\n",
    "tracks.append(t1.pos())\n",
    "\n",
    "t1.fd(300)\n",
    "\n",
    "tracks.append(t1.pos())\n",
    "\n",
    "t1.back(100)\n",
    "\n",
    "tracks.append(t1.pos())\n",
    "\n",
    "t1.left(90)\n",
    "\n",
    "t1.fd(200)\n",
    "\n",
    "tracks.append(t1.pos())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(-400.00,300.00)\n",
      "(-400.00,-100.00)\n",
      "(-400.00,50.00)\n",
      "(-100.00,50.00)\n",
      "(-100.00,350.00)\n",
      "(-100.00,200.00)\n",
      "(200.00,200.00)\n",
      "(200.00,0.00)\n",
      "(200.00,-300.00)\n",
      "(200.00,-200.00)\n",
      "(400.00,-200.00)\n"
     ]
    }
   ],
   "source": [
    "for t in tracks:\n",
    "    print t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false,
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(-400.00,300.00)\n",
      "(-400.00,-100.00)\n",
      "(-400.00,50.00)\n",
      "(-100.00,50.00)\n",
      "(-100.00,350.00)\n",
      "(-100.00,200.00)\n",
      "(200.00,200.00)\n",
      "(200.00,0.00)\n",
      "(200.00,-300.00)\n",
      "(200.00,-200.00)\n",
      "(400.00,-200.00)\n"
     ]
    }
   ],
   "source": [
    "for t in range(0,11):\n",
    "    print tracks[t]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "for t in range(0,len(mytracks)):\n",
    "    print mytracks[t]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "for t in mytracks:\n",
    "    print t"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 함수로 구성할 경우 컴퓨터가 실행하는 순서를 살펴보자"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import turtle\n",
    "wn=turtle.Screen()\n",
    "#wn.bgpic(\"myMaze.gif\")\n",
    "t1=turtle.Turtle()\n",
    "\n",
    "def saveTracks():\n",
    "    t1.speed(1)\n",
    "    t1.penup()\n",
    "    mytracks=list()\n",
    "    t1.goto(-400,300)\n",
    "    mytracks.append(t1.pos())\n",
    "    t1.pendown()\n",
    "    t1.pencolor(\"Red\")\n",
    "    t1.right(90)\n",
    "    t1.fd(400)\n",
    "    mytracks.append(t1.pos())\n",
    "    t1.backward(150)\n",
    "    mytracks.append(t1.pos())\n",
    "    t1.left(90)\n",
    "    t1.fd(300)\n",
    "    mytracks.append(t1.pos())\n",
    "    t1.left(90)\n",
    "    t1.fd(300)\n",
    "    mytracks.append(t1.pos())\n",
    "    t1.back(150)\n",
    "    mytracks.append(t1.pos())\n",
    "    t1.right(90)\n",
    "    t1.fd(300)\n",
    "    mytracks.append(t1.pos())\n",
    "    t1.left(90)\n",
    "    t1.right(90)\n",
    "    t1.right(90)\n",
    "    t1.fd(200)\n",
    "    mytracks.append(t1.pos())\n",
    "    t1.fd(300)\n",
    "    mytracks.append(t1.pos())\n",
    "    t1.back(100)\n",
    "    mytracks.append(t1.pos())\n",
    "    t1.left(90)\n",
    "    t1.fd(200)\n",
    "    mytracks.append(t1.pos())\n",
    "    return mytracks\n",
    "\n",
    "def replayTracks(mytracks):\n",
    "    t1.home()\n",
    "    t1.clear()\n",
    "    for t in mytracks:\n",
    "        print t\n",
    "        t1.setpos(t)\n",
    "\n",
    "def lab7():\n",
    "    mytracks=saveTracks()\n",
    "    replayTracks(mytracks)\n",
    "\n",
    "def main():\n",
    "    lab7()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(-400.00,300.00)\n",
      "(-400.00,-100.00)\n",
      "(-400.00,50.00)\n",
      "(-100.00,50.00)\n",
      "(-100.00,350.00)\n",
      "(-100.00,200.00)\n",
      "(200.00,200.00)\n",
      "(200.00,0.00)\n",
      "(200.00,-300.00)\n",
      "(200.00,-200.00)\n",
      "(400.00,-200.00)\n"
     ]
    }
   ],
   "source": [
    "main()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## 데이터구조-5: 문자열에서 문자를 세기\n",
    "\n",
    "* 데이터구조-5-1: 문자열을 입력 받아서, 각 문자의 갯수를 세기\n",
    "* 데이터구조-5-2: 문자의 갯수를 막대그래프로 그리기\n",
    "* 프로그래밍 요소\n",
    "    * dict\n",
    "    * 왜 list보다 dict가 보다 적합한 구조일까? list는 key가 없고, 정수인덱스로 값을 읽어 오는 특성.\n",
    "* 주의:\n",
    "    * 존재하지 않는 key의 값을 넣을 경우: +1은 불가능. 없는 값에 '더하기 1'은 안 된다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "image/svg+xml": [
       "<svg height=\"553px\" style=\"width:324px;height:553px;\" version=\"1.1\" viewBox=\"0 0 324 553\" width=\"324px\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\"><defs><filter height=\"300%\" id=\"f1\" width=\"300%\" x=\"-1\" y=\"-1\"><feGaussianBlur result=\"blurOut\" stdDeviation=\"2.0\"/><feColorMatrix in=\"blurOut\" result=\"blurOut2\" type=\"matrix\" values=\"0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .4 0\"/><feOffset dx=\"4.0\" dy=\"4.0\" in=\"blurOut2\" result=\"blurOut3\"/><feBlend in=\"SourceGraphic\" in2=\"blurOut3\" mode=\"normal\"/></filter></defs><g><ellipse cx=\"141.5\" cy=\"20\" fill=\"#000000\" filter=\"url(#f1)\" rx=\"10\" ry=\"10\" style=\"stroke: none; stroke-width: 1.0;\"/><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"209\" x=\"37\" y=\"50\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"189\" x=\"47\" y=\"71.6016\">set word='sangmyung university'</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"127\" x=\"78\" y=\"104.1328\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"107\" x=\"88\" y=\"125.7344\">initialize dictionary</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"49\" x=\"117\" y=\"158.2656\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"29\" x=\"127\" y=\"179.8672\">i = 0</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"149\" x=\"67\" y=\"256.3984\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"129\" x=\"77\" y=\"278\">get ith char from word</text><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"70,310.5313,213,310.5313,225,322.5313,213,334.5313,70,334.5313,58,322.5313,70,310.5313\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"11\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"143\" x=\"70\" y=\"326.6885\">char does not exist in keys</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"76\" x=\"10\" y=\"344.5313\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"56\" x=\"20\" y=\"366.1328\">value = 1</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"124\" x=\"173\" y=\"344.5313\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"104\" x=\"183\" y=\"366.1328\">value = value + 1</text><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"141.5,384.6641,153.5,396.6641,141.5,408.6641,129.5,396.6641,141.5,384.6641\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"77\" x=\"103\" y=\"428.6641\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"57\" x=\"113\" y=\"450.2656\">add 1 to i</text><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"141.5,212.3984,153.5,224.3984,141.5,236.3984,129.5,224.3984,141.5,212.3984\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"83,482.7969,200,482.7969,212,494.7969,200,506.7969,83,506.7969,71,494.7969,83,482.7969\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"11\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"117\" x=\"83\" y=\"498.9541\">i &lt;= last char of word</text><ellipse cx=\"141.5\" cy=\"536.7969\" fill=\"none\" filter=\"url(#f1)\" rx=\"10\" ry=\"10\" style=\"stroke: #000000; stroke-width: 1.0;\"/><ellipse cx=\"142\" cy=\"537.2969\" fill=\"#000000\" filter=\"url(#f1)\" rx=\"6\" ry=\"6\" style=\"stroke: none; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"141.5\" x2=\"141.5\" y1=\"30\" y2=\"50\"/><polygon fill=\"#A80036\" points=\"137.5,40,141.5,50,145.5,40,141.5,44\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"141.5\" x2=\"141.5\" y1=\"84.1328\" y2=\"104.1328\"/><polygon fill=\"#A80036\" points=\"137.5,94.1328,141.5,104.1328,145.5,94.1328,141.5,98.1328\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"141.5\" x2=\"141.5\" y1=\"138.2656\" y2=\"158.2656\"/><polygon fill=\"#A80036\" points=\"137.5,148.2656,141.5,158.2656,145.5,148.2656,141.5,152.2656\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"58\" x2=\"48\" y1=\"322.5313\" y2=\"322.5313\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"48\" x2=\"48\" y1=\"322.5313\" y2=\"344.5313\"/><polygon fill=\"#A80036\" points=\"44,334.5313,48,344.5313,52,334.5313,48,338.5313\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"225\" x2=\"235\" y1=\"322.5313\" y2=\"322.5313\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"235\" x2=\"235\" y1=\"322.5313\" y2=\"344.5313\"/><polygon fill=\"#A80036\" points=\"231,334.5313,235,344.5313,239,334.5313,235,338.5313\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"48\" x2=\"48\" y1=\"378.6641\" y2=\"396.6641\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"48\" x2=\"129.5\" y1=\"396.6641\" y2=\"396.6641\"/><polygon fill=\"#A80036\" points=\"119.5,392.6641,129.5,396.6641,119.5,400.6641,123.5,396.6641\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"235\" x2=\"235\" y1=\"378.6641\" y2=\"396.6641\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"235\" x2=\"153.5\" y1=\"396.6641\" y2=\"396.6641\"/><polygon fill=\"#A80036\" points=\"163.5,392.6641,153.5,396.6641,163.5,400.6641,159.5,396.6641\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"141.5\" x2=\"141.5\" y1=\"290.5313\" y2=\"310.5313\"/><polygon fill=\"#A80036\" points=\"137.5,300.5313,141.5,310.5313,145.5,300.5313,141.5,304.5313\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"141.5\" x2=\"141.5\" y1=\"408.6641\" y2=\"428.6641\"/><polygon fill=\"#A80036\" points=\"137.5,418.6641,141.5,428.6641,145.5,418.6641,141.5,422.6641\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"141.5\" x2=\"141.5\" y1=\"236.3984\" y2=\"256.3984\"/><polygon fill=\"#A80036\" points=\"137.5,246.3984,141.5,256.3984,145.5,246.3984,141.5,250.3984\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"212\" x2=\"319\" y1=\"494.7969\" y2=\"494.7969\"/><polygon fill=\"#A80036\" points=\"315,393.5977,319,383.5977,323,393.5977,319,389.5977\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"319\" x2=\"319\" y1=\"224.3984\" y2=\"494.7969\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"319\" x2=\"153.5\" y1=\"224.3984\" y2=\"224.3984\"/><polygon fill=\"#A80036\" points=\"163.5,220.3984,153.5,224.3984,163.5,228.3984,159.5,224.3984\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"141.5\" x2=\"141.5\" y1=\"462.7969\" y2=\"482.7969\"/><polygon fill=\"#A80036\" points=\"137.5,472.7969,141.5,482.7969,145.5,472.7969,141.5,476.7969\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"141.5\" x2=\"141.5\" y1=\"192.3984\" y2=\"212.3984\"/><polygon fill=\"#A80036\" points=\"137.5,202.3984,141.5,212.3984,145.5,202.3984,141.5,206.3984\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"141.5\" x2=\"141.5\" y1=\"506.7969\" y2=\"526.7969\"/><polygon fill=\"#A80036\" points=\"137.5,516.7969,141.5,526.7969,145.5,516.7969,141.5,520.7969\" style=\"stroke: #A80036; stroke-width: 1.0;\"/></g></svg>"
      ],
      "text/plain": [
       "<IPython.core.display.SVG object>"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%plantuml\n",
    "@startuml\n",
    "start\n",
    ":set word='sangmyung university';\n",
    ":initialize dictionary;\n",
    ":i = 0;\n",
    "repeat\n",
    ":get ith char from word;\n",
    "if (char does not exist in keys)\n",
    ":value = 1;\n",
    "else\n",
    ":value = value + 1;\n",
    "endif\n",
    ":add 1 to i;\n",
    "repeat while(i <= last char of word)\n",
    "stop\n",
    "@enduml"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### Dictionary\n",
    "\n",
    "* 선언을 하고 사용.\n",
    "* key-value로 구성.\n",
    "* 사용하는 경우\n",
    "    * 자료가 필드, 값으로 구성된 경우\n",
    "        * 예: 이름-'홍길동'. key -> '이름', value -> '홍길동'. key-value는 수, 문자 모두 가능.\n",
    "    * 자료의 갯수를 세는 경우\n",
    "        * 데이터에 각 단어가 발생하는 빈도수를 세는 경우"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'd' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-17-4dbb6651e4d1>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0md\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'name'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'jsl'\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'd' is not defined"
     ]
    }
   ],
   "source": [
    "# 선언하지 않고 key-value를 넣게 되면 오류\n",
    "d['name']='jsl'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "# 선언하고 사용.\n",
    "d=dict()\n",
    "d['name']='jsl'\n",
    "print \"d =\",d"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 문자열의 문자 갯수 세기\n",
    "\n",
    "* 문자 갯수를 세려면, 문자열을 문자로 분리한다.\n",
    "* 분리한 문자열의 문자갯수를 세기\n",
    "    * 문자를 키, 문자의 갯수를 값으로 저장하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['sangmyung', 'university']"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "word = 'sangmyung university'\n",
    "word.split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['s', 'a', 'n', 'g', 'm', 'y', 'u', 'n', 'g', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']\n"
     ]
    }
   ],
   "source": [
    "word = 'sangmyung university'\n",
    "allChars=list(word)\n",
    "print allChars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "s a n g m y u n g   u n i v e r s i t y\n"
     ]
    }
   ],
   "source": [
    "word = 'sangmyung university'\n",
    "for c in word:\n",
    "    print c,"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "mydict=dict()\n",
    "mydict['s']=1\n",
    "mydict['a']=1\n",
    "mydict['n']=1\n",
    "mydict['g']=1\n",
    "mydict['m']=1\n",
    "mydict['y']=1\n",
    "mydict['u']=1\n",
    "mydict['n']+=1\n",
    "print mydict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "d=dict()\n",
    "for c in allchars:\n",
    "    if c=='s':\n",
    "        d[c]=1\n",
    "    elif c=='a':\n",
    "        d[c]=1\n",
    "\n",
    "print d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "print 'a' in d\n",
    "print 'b' in d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "d=dict()\n",
    "for c in allchars:\n",
    "    if c not in d:\n",
    "        d[c]=1\n",
    "    else:\n",
    "        d[c]=d[c]+1\n",
    "print d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "키-키값 {'a': 1, ' ': 1, 'e': 1, 'g': 2, 'i': 2, 'm': 1, 'n': 3, 's': 2, 'r': 1, 'u': 2, 't': 1, 'v': 1, 'y': 2}\n",
      " 저장된 문자의 갯수 (중복을 빼고) 13\n",
      "키:  ['a', ' ', 'e', 'g', 'i', 'm', 'n', 's', 'r', 'u', 't', 'v', 'y']\n",
      "키값: [1, 1, 1, 2, 2, 1, 3, 2, 1, 2, 1, 1, 2]\n"
     ]
    }
   ],
   "source": [
    "word = 'sangmyung university'\n",
    "d = dict()\n",
    "for c in word:\n",
    "    if c not in d:\n",
    "        d[c]=1\n",
    "    else:\n",
    "        d[c]=d[c]+1\n",
    "print \"키-키값\",d\n",
    "print \" 저장된 문자의 갯수 (중복을 빼고)\", len(d)\n",
    "print \"키: \",d.keys()\n",
    "print \"키값:\", d.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Seoul is so beautiful and lovely\n",
      "{'a': 2, ' ': 5, 'b': 1, 'e': 3, 'd': 1, 'f': 1, 'i': 2, 's': 2, 'l': 4, 'o': 3, 'n': 1, 'S': 1, 'u': 3, 't': 1, 'v': 1, 'y': 1}\n"
     ]
    }
   ],
   "source": [
    "def countChars(word):\n",
    "    d = dict()\n",
    "    for c in word:\n",
    "        if c not in d:\n",
    "            d[c]=1\n",
    "        else:\n",
    "            d[c]=d[c]+1\n",
    "    return d\n",
    "\n",
    "word=raw_input()\n",
    "print countChars(word)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### 그래프 그리기\n",
    "\n",
    "* matplotlib을 사용\n",
    "* bargraph는 bar객체를 사용\n",
    "* x축은 문자\n",
    "    * dictionary의 key는 문자열. 따라서 순서를 가지는 x축으로 사용할 수 없슴.\n",
    "    * 우선 x축에 사용될 문자의 수를 세어 놓는다.\n",
    "        * range((len(d))\n",
    "    * 레이블을 x축에 적는다.\n",
    "        * xticks로 key값으로 레이블을 만들어 줌.\n",
    "* y축 문자 갯수\n",
    "    * d.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]\n"
     ]
    }
   ],
   "source": [
    "print range(len(d))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "키-키값 {'a': 1, ' ': 1, 'e': 1, 'g': 2, 'i': 2, 'm': 1, 'n': 3, 's': 2, 'r': 1, 'u': 2, 't': 1, 'v': 1, 'y': 2}\n",
      "키:  ['a', ' ', 'e', 'g', 'i', 'm', 'n', 's', 'r', 'u', 't', 'v', 'y']\n",
      "키값: [1, 1, 1, 2, 2, 1, 3, 2, 1, 2, 1, 1, 2]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fc4d7f0bd10>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "%matplotlib inline\n",
    "\n",
    "import matplotlib\n",
    "import matplotlib.pyplot as plt\n",
    "# 2단계로 나누어 그림\n",
    "plt.bar(range(len(d)), d.values(), align='center')\n",
    "plt.xticks(range(len(d)), list(d.keys()))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### 아래는 학생의 프로그래밍\n",
    "\n",
    "* 중첩for문을 사용하지 않아도 풀 수 있는 문제.\n",
    "* 중첩for는 반복횟수를 2n이 아니라, n*n으로 증가시킴."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['s', 'a', 'n', 'g', 'm', 'y', 'u', 'n', 'g', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']\n",
      "{'a': 1, ' ': 1, 'e': 1, 'g': 2, 'i': 2, 'm': 1, 'n': 3, 's': 2, 'r': 1, 'u': 2, 't': 1, 'v': 1, 'y': 2}\n"
     ]
    }
   ],
   "source": [
    "text='sangmyung university'\n",
    "text_cut = list(text)\n",
    "sdict = {}\n",
    "for i in range(0,len(text_cut)):\n",
    "    temp = 0\n",
    "    for j in range(0,len(text_cut)):\n",
    "        if (text_cut[i] == text_cut[j]):\n",
    "            temp += 1\n",
    "    sdict[text_cut[i]] = temp\n",
    "print text_cut    \n",
    "print sdict"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## 데이터구조-6: 문자열에 포함된 문자와 숫자의 개수 세기\n",
    "\n",
    "* 문자열을 입력받고, 그 문자열에 포함된 숫자와 문자의 갯수를 세기\n",
    "\n",
    "* 프로그래밍 요소\n",
    "    * 컴퓨터가 문자를 식별하는 방식을 이해한다.\n",
    "    * dict를 사용하여 빈도를 계산할 수 있다.\n",
    "* 함수\n",
    "    * 함수명 countDigitsLetters\n",
    "    * 입력 문자열 word\n",
    "    * 출력 dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world 456\n",
      "LETTERS 10\n",
      "DIGITS 3\n"
     ]
    }
   ],
   "source": [
    "# 입력문자열에서 문자와 숫자의 갯수를 출력\n",
    "# dictionary를 이해\n",
    "\n",
    "s = raw_input()\n",
    "d={\"DIGITS\":0, \"LETTERS\":0}\n",
    "for c in s:\n",
    "    if c.isdigit():\n",
    "        d[\"DIGITS\"]+=1\n",
    "    elif c.isalpha():\n",
    "        d[\"LETTERS\"]+=1\n",
    "    else:\n",
    "        pass \n",
    "print \"LETTERS\", d[\"LETTERS\"]\n",
    "print \"DIGITS\", d[\"DIGITS\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LETTERS 10\n",
      "DIGITS 1\n"
     ]
    }
   ],
   "source": [
    "# 입력문자열에서 문자와 숫자의 갯수를 출력\n",
    "# dictionary를 이해\n",
    "\n",
    "\n",
    "def countDigitsLetters(word):\n",
    "    d={\"DIGITS\":0, \"LETTERS\":0}\n",
    "    for c in word:\n",
    "        if c.isdigit():\n",
    "            d[\"DIGITS\"]+=1\n",
    "        elif c.isalpha():\n",
    "            d[\"LETTERS\"]+=1\n",
    "        else:\n",
    "            pass \n",
    "    return d\n",
    "d=countDigitsLetters('7 hongji dong')\n",
    "print \"LETTERS\", d[\"LETTERS\"]\n",
    "print \"DIGITS\", d[\"DIGITS\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### isDigit의 구현원리\n",
    "\n",
    "* ascii문자표의 숫자 영역(48-57)에 있는지 확인\n",
    "* space 코드 값은 32"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "32\n"
     ]
    }
   ],
   "source": [
    "print ord(' ')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 대소문자의 변환원리는 32를 더하거나 뺀다.\n",
    "* 소문자 'a'의 코드 값은 97, 대문자 'A'는 65이다.\n",
    "* ord, chr함수를 이용하면 코드 값을 확인할 수 있다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "97\n",
      "65\n"
     ]
    }
   ],
   "source": [
    "print ord('a')\n",
    "print ord('A')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\n"
     ]
    }
   ],
   "source": [
    "print chr(97)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\n",
      "A\n"
     ]
    }
   ],
   "source": [
    "print chr(ord('A')+32)\n",
    "print chr(ord('a')-32)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "h 104\n",
      "e 101\n",
      "l 108\n",
      "l 108\n",
      "o 111\n",
      "1 49\n",
      "2 50\n",
      "3 51\n",
      "w 119\n",
      "i 105\n",
      "t 116\n",
      "h 104\n",
      "4 52\n",
      "5 53\n",
      "6 54\n",
      "numbers:  ['1', '2', '3', '4', '5', '6']\n",
      "chars:  ['h', 'e', 'l', 'l', 'o', 'w', 'i', 't', 'h']\n",
      "counter:  {'char': 9, 'num': 6}\n"
     ]
    }
   ],
   "source": [
    "s='hello123with456'\n",
    "numList=list()\n",
    "charList=list()\n",
    "counter={'num':0,'char':0}\n",
    "for c in s:\n",
    "    asciicode=ord(c)\n",
    "    print c,asciicode\n",
    "    if asciicode>47 and asciicode<58:\n",
    "        numList.append(c)\n",
    "        counter['num']+=1\n",
    "    else:\n",
    "        charList.append(c)\n",
    "        counter['char']+=1\n",
    "print \"numbers: \",numList\n",
    "print \"chars: \",charList\n",
    "print \"counter: \",counter\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "UPPER CASE 2\n",
      "LOWER CASE 8\n"
     ]
    }
   ],
   "source": [
    "s = \"Hello World!\"\n",
    "d={\"UPPER CASE\":0, \"LOWER CASE\":0}\n",
    "for c in s:\n",
    "    if c.isupper():\n",
    "        d[\"UPPER CASE\"]+=1\n",
    "    elif c.islower():\n",
    "        d[\"LOWER CASE\"]+=1\n",
    "    else:\n",
    "        pass\n",
    "print \"UPPER CASE\", d[\"UPPER CASE\"]\n",
    "print \"LOWER CASE\", d[\"LOWER CASE\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false,
    "scrolled": true,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x10e1558d0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "%matplotlib inline\n",
    "\n",
    "import matplotlib\n",
    "import matplotlib.pyplot as plt\n",
    "# 2단계로 나누어 그림\n",
    "plt.bar(range(len(d)), d.values(), align='center')\n",
    "plt.xticks(range(len(d)), list(d.keys()))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## 데이터구조-7: 우리 집에 없지만 친구집에 있는 가전제품 찾기.\n",
    "\n",
    "* 7-1 한 집에만 있는 제품을 나열하기\n",
    "* 7-2 모든 집에 같이 있는 제품 나열하기\n",
    "* 7-3 어느 집에라도 있는 제품을 나열하기\n",
    "* 7-4 모든 가전제품의 갯수를 세어보기 (집이 2개이므로, 갯수는 1 또는 2)\n",
    "\n",
    "* 자신의 방과 친구의 방에 있는 가전제품을 10개 이상 나열하여 자료구조로 만들기 (영어).\n",
    "    * 우리 집: TV, phone, camera, fridger, mixer, audio, cd player, light, computer, notebook, recorder\n",
    "    * 친구 집: coffee machine, radio, camera, running machine, ramp, computer, notebook, recorder\n",
    "\n",
    "\n",
    "* 주의\n",
    "    * 많은 학생이 list, compare를 사용하려고 함. 한 요소를 선택하고 다른 모든 요소와 비교해서 존재 여부를 확인.\n",
    "    * 이 방식은 중첩for문과 같은 비교횟수\n",
    "    * set은 인덱스가 없다.\n",
    "    * set의 합집합은 중복을 제외한다. 가전제품의 합집합은 두 집에 있는 가전제품의 갯수를 2로 표현하지 않는다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "set(['TV', 'light', 'mixer', 'phone', 'fridger', 'cd player', 'audio'])\n",
      "set(['TV', 'light', 'mixer', 'phone', 'fridger', 'cd player', 'audio'])\n",
      "set(['camera', 'recorder', 'computer', 'notebook'])\n",
      "set(['TV', 'light', 'ramp', 'notebook', 'mixer', 'running machine', 'phone', 'computer', 'fridger', 'coffee machine', 'cd player', 'radio', 'recorder', 'audio', 'camera'])\n",
      "19\n",
      "{'TV': 1, 'light': 1, 'ramp': 1, 'running machine': 1, 'notebook': 2, 'coffee machine': 1, 'phone': 1, 'computer': 2, 'fridger': 1, 'mixer': 1, 'cd player': 1, 'radio': 1, 'recorder': 2, 'audio': 1, 'camera': 2}\n"
     ]
    }
   ],
   "source": [
    "myHome={\"TV\", \"phone\", \"camera\", \"fridger\", \"mixer\", \"audio\", \"cd player\", \"light\", \"computer\", \"notebook\", \"recorder\"}\n",
    "yourHome={\"coffee machine\", \"radio\", \"camera\", \"running machine\", \"ramp\", \"computer\", \"notebook\", \"recorder\"}\n",
    "\n",
    "# 우리 집에는 있지만 친구 집에 없는 것\n",
    "print myHome-yourHome\n",
    "print myHome.difference(yourHome)\n",
    "\n",
    "# 우리 집에도 있고 친구 집에도 있는 것\n",
    "print myHome.intersection(yourHome)\n",
    "\n",
    "# 우리 집에도 있고, 친구 집에도 있는 것.\n",
    "print myHome.union(yourHome)\n",
    "\n",
    "# set를 더하는 것은 안 된다. set은 중복을 허락지 않는 구조\n",
    "# list로 더할 수 있다.\n",
    "print len(list(myHome)+list(yourHome))\n",
    "\n",
    "d={}\n",
    "for x in (list(myHome) + list(yourHome)):\n",
    "    if x not in d:\n",
    "        d[x]=1\n",
    "    else:\n",
    "        d[x]+=1\n",
    "print d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "set(['new jersey', 'new york'])\n",
      "set(['connecticut'])\n",
      "set(['new jersey', 'new york'])\n",
      "set(['pennsylvania', 'connecticut', 'new york', 'new jersey', 'maine'])\n"
     ]
    }
   ],
   "source": [
    "a = {\"new york\", \"connecticut\", \"new jersey\"}\n",
    "b = {\"connecticut\", \"pennsylvania\", \"maine\"}\n",
    "print a-b\n",
    "print a.intersection(b)\n",
    "print a.difference(b)\n",
    "print a.union(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "set(['Lee', 'Kim', 'Choi', 'Lim', 'Park', 'Sung', 'Jung'])\n"
     ]
    }
   ],
   "source": [
    "#1개 이상 존재하는 성을 찾으면? -> key값을 만듦.\n",
    "a={\"Lim\",\"Lee\",\"Kim\",\"Park\",\"Choi\",\"Lee\",\"Kim\",\"Lim\",\"Park\",\"Jung\",\"Choi\",\n",
    "\"Lee\",\"Park\",\"Choi\",\"Sung\"}\n",
    "print set(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "set(['Lim'])\n"
     ]
    }
   ],
   "source": [
    "s1={\"Lim\",\"Lee\",\"Kim\",\"Park\",\"Choi\"}\n",
    "s2={\"Lee\",\"Kim\",\"Park\",\"Jung\",\"Choi\",\"Lee\",\"Park\",\"Choi\",\"Sung\"}\n",
    "#elements in s1 but not in s2\n",
    "print s1-s2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "# This dictionary contains key-value pairs.\n",
    "dictionary = {\"cat\": 1, \"dog\": 2, \"bird\": 3}\n",
    "print(dictionary)\n",
    "\n",
    "# This set contains just the dictionary's keys.\n",
    "keys = set(dictionary)\n",
    "print(keys)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 데이터구조-8: 서울 경복궁 입구에서 제일 가까운 지하철 역 찾기\n",
    "\n",
    "* 지도에서 경복궁과 인근 지하철역 5개의 위치를 수집한다.\n",
    "* 거리 계산을 하여, 경복궁과 제일 가까운 역을 찾는다.\n",
    "\n",
    "* 프로그래밍 요소\n",
    "    * Tuple 데이터구조를 사용할 수 있다.\n",
    "    * 2차원 구조를 사용할 수 있다.\n",
    "        * list of tuples\n",
    "    * 거리 계산을 할 수 있다.\n",
    "    * 최소 값을 구할 수 있다.\n",
    "\n",
    "    * 자료구조를 처리할 때 python 방식으로 1줄로 처리할 수 있다.\n",
    "    * tuple\n",
    "        * 왜 list가 아니고, tuple을 사용할까?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "* 위치를 저장하려면, 어떤 데이터구조를 사용할 것인가?\n",
    "    * 위치는 수정불가능(immutable)\n",
    "    * 튜플은 왜 수정불가능하게 만들었을까?\n",
    "        * 성능\n",
    "        * 변경이 될 경우, 문제가 될 수 있는 경우 (예: dict에서 key값이 변경되면 어떻게 되나)\n",
    "\n",
    "* 좌표 구하기 - 구글 지도 > 마우스 오른쪽 버튼 > 화면 하단에 좌표 표시됨.\n",
    "    * 경복궁 ky 37.575869, 126.976637\n",
    "    * 안국역 ak 37.576549, 126.985520\n",
    "    * 광화문역 kw 37.571618, 126.976551\n",
    "    * 독립문역 37.574577, 126.957754"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Tuple 복습\n",
    "    * Tuple은 수정할 수 없고, 리스트는 수정할 수 있다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'tuple' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-16-413c6d8d8a2d>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;31m# This causes an error.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0manimals\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'feline'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: 'tuple' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "animals = ('cat', 'dog', 'mouse')\n",
    "\n",
    "# This causes an error.\n",
    "animals[0] = 'feline'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['feline', 'dog', 'mouse']\n"
     ]
    }
   ],
   "source": [
    "animals = ['cat', 'dog', 'mouse']\n",
    "\n",
    "# This causes an error.\n",
    "animals[0] = 'feline'\n",
    "print animals"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 2차원 구조의 이해\n",
    "    * 시간표와 같이 가로축, 세로축이 있는 2차원 데이터 구조\n",
    "    * 가로축과 세로축 인덱스를 사용하여 자료를 읽을 수 있다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "my2dlist=[\n",
    "    [1,2],\n",
    "    [3,4],\n",
    "    [5,6]\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1, 2], [3, 4], [5, 6]]\n"
     ]
    }
   ],
   "source": [
    "print my2dlist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "print my2dlist[0][0]\n",
    "print my2dlist[1][0]\n",
    "print my2dlist[2][0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 반복문을 이용하여 세로축 출력하기\n",
    "* 반복문은 파이프에 자료를 넣고 꺼내는 것으로 이해\n",
    "    * 첫째 반복문은 위치객체가 파이프에 차례로 들어간다\n",
    "        * 따라서 위치 (X,Y)의 각 값을 얻기 위해서 인덱스를 사용해야 한다.\n",
    "    * 두번째는 인덱스가 파이프에 들어가 있다고 생각하면 된다.\n",
    "        * 따라서 인덱스를 중첩해서 자료를 꺼내온다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2]\n",
      "[3, 4]\n",
      "[5, 6]\n"
     ]
    }
   ],
   "source": [
    "for i in my2dlist:\n",
    "    print i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "for i in my2dlist:\n",
    "    print i[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* i를 loc으로 변수명을 변경해서 사용할 수 있고, 그러면 이해하기 쉽다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "for loc in my2dlist:\n",
    "    print loc[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "for i in range(0,len(my2dlist)):\n",
    "    print my2dlist[i][0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 튜플의 리스트를 이해해 본다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "callingCodes = [(82,\"South Korea\"),(81,\"Japan\"),(1,\"United States of America\"),(44,\"United Kingdom\")]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "82\n",
      "81\n"
     ]
    }
   ],
   "source": [
    "print callingCodes[0][0]\n",
    "print callingCodes[1][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "82\n",
      "81\n",
      "1\n",
      "44\n"
     ]
    }
   ],
   "source": [
    "for c in callingCodes:\n",
    "    print c[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[82, 81, 1, 44]"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[x[0] for x in callingCodes]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* dict를 사용해서 2차원 구조를 표현할 수 있다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "cdict=dict(callingCodes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{81: 'Japan', 82: 'South Korea', 44: 'United Kingdom', 1: 'United States of America'}\n"
     ]
    }
   ],
   "source": [
    "print cdict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'United Kingdom'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict(callingCodes)[44]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 4, 6, 8, 10]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# single line of for statement - condition in it!\n",
    "[ x for x in range(1,11) if x%2==0 ]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* (1,2) (3,4)의 거리"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "print math.sqrt((1-3)**2 + (2-4)**2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "37.575869\n",
      "[(37.576549, 126.98552), (37.571618, 126.976551), (37.574577, 126.957754)]\n",
      "[0.008908989224370846, 0.004251869823967939, 0.018927148570244013]\n",
      "0.00425186982397\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "#위치측정\n",
    "myloc=(37.575869, 126.976637)\n",
    "print myloc[0]\n",
    "locations=[(37.576549, 126.985520),\n",
    "    (37.571618, 126.976551),\n",
    "    (37.574577, 126.957754)]\n",
    "print locations\n",
    "\n",
    "#거리 측정\n",
    "dist=[]\n",
    "for (x,y) in locations:\n",
    "    dist.append(math.sqrt((myloc[0]-x)**2 + (myloc[1]-y)**2))\n",
    "print dist\n",
    "\n",
    "# 최소값\n",
    "print min(dist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.00425186982397\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "def getNearLocation(myLoc,locations):\n",
    "    #거리 측정\n",
    "    dist=[]\n",
    "    for (x,y) in locations:\n",
    "        dist.append(math.sqrt((myloc[0]-x)**2 + (myloc[1]-y)**2))\n",
    "    return min(dist)\n",
    "myLoc=(37.575869, 126.976637)\n",
    "locations=[(37.576549, 126.985520),\n",
    "    (37.571618, 126.976551),\n",
    "    (37.574577, 126.957754)]\n",
    "print getNearLocation(myLoc,Locations)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 데이터구조-9: 서울에 거주하는 남녀의 구별 합계와 평균구하기\n",
    "\n",
    "* 9-1 남자의 합계와 평균을 구하기\n",
    "* 9-2 여자의 합계와 평균을 구하기.\n",
    "* 9-3 구별 인구합계를 구하고, 그래프 그리기\n",
    "\n",
    "* 프로그래밍 요소\n",
    "    * 2차원 데이터 구조를 사용할 수 있다.\n",
    "        * 데이터 구조의 차원만큼 반복문을 사용하는 것이 좋다. 1차원은 for문 1개, 2차원은 for문 중첩.\n",
    "    * 데이터구조에 저장된 값을 사용하여 연산을 할 수 있다.\n",
    "\n",
    "* 자료\n",
    "    * 서울 열린데이터 광장 http://data.seoul.go.kr에서 가져온 서울시 주민등록 구별/성별 통계 (2015년 3월 30일)\n",
    "\n",
    "```\n",
    "구    남     여\n",
    "종로구  74,425 76,326\n",
    "중구    61,164 61,636\n",
    "용산구  109,688 115,744\n",
    "성동구  144,796 146,776\n",
    "광진구  174,996 181,676\n",
    "동대문구        177,841 177,434\n",
    "중랑구  204,630 205,980\n",
    "성북구  223,373 232,245\n",
    "강북구  161,055 166,130\n",
    "도봉구  171,576 176,735\n",
    "노원구  279,169 293,772\n",
    "은평구  239,450 251,066\n",
    "서대문구        148,690 156,510\n",
    "마포구  182,977 196,992\n",
    "양천구  237,792 242,641\n",
    "강서구  283,869 296,762\n",
    "구로구  209,344 210,282\n",
    "금천구  118,965 114,441\n",
    "영등포구        186,503 186,856\n",
    "동작구  195,734 203,014\n",
    "관악구  254,381 249,472\n",
    "서초구  212,401 229,111\n",
    "강남구  271,654 295,354\n",
    "송파구  319,197 335,045\n",
    "강동구  229,829 231,671\n",
    "```\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[74425, 76326], [61164, 61636], [109688, 115744], [144796, 146776], [174996, 181676], [177841, 177434], [204630, 205980], [223373, 232245], [161055, 166130], [171576, 176735], [279169, 293772], [239450, 251066], [148690, 156510], [182977, 196992], [237792, 242641], [283869, 296762], [209344, 210282], [118965, 114441], [186503, 186856], [195734, 203014], [254381, 249472], [212401, 229111], [271654, 295354], [319197, 335045], [229829, 231671]]\n"
     ]
    }
   ],
   "source": [
    "data=[\n",
    "    [74425, 76326],\n",
    "    [61164, 61636],\n",
    "    [109688, 115744],\n",
    "    [144796, 146776],\n",
    "    [174996, 181676],\n",
    "    [177841, 177434],\n",
    "    [204630, 205980],\n",
    "    [223373, 232245],\n",
    "    [161055, 166130],\n",
    "    [171576, 176735],\n",
    "    [279169, 293772],\n",
    "    [239450, 251066],\n",
    "    [148690, 156510],\n",
    "    [182977, 196992],\n",
    "    [237792, 242641],\n",
    "    [283869, 296762],\n",
    "    [209344, 210282],\n",
    "    [118965, 114441],\n",
    "    [186503, 186856],\n",
    "    [195734, 203014],\n",
    "    [254381, 249472],\n",
    "    [212401, 229111],\n",
    "    [271654, 295354],\n",
    "    [319197, 335045],\n",
    "    [229829, 231671]\n",
    "]\n",
    "print data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[74425, 76326] [61164, 61636] [109688, 115744] [144796, 146776] [174996, 181676] [177841, 177434] [204630, 205980] [223373, 232245] [161055, 166130] [171576, 176735] [279169, 293772] [239450, 251066] [148690, 156510] [182977, 196992] [237792, 242641] [283869, 296762] [209344, 210282] [118965, 114441] [186503, 186856] [195734, 203014] [254381, 249472] [212401, 229111] [271654, 295354] [319197, 335045] [229829, 231671]\n"
     ]
    }
   ],
   "source": [
    "for gu in data:\n",
    "    print gu,"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "74425 76326\n",
      "61164 61636\n",
      "109688 115744\n",
      "144796 146776\n",
      "174996 181676\n",
      "177841 177434\n",
      "204630 205980\n",
      "223373 232245\n",
      "161055 166130\n",
      "171576 176735\n",
      "279169 293772\n",
      "239450 251066\n",
      "148690 156510\n",
      "182977 196992\n",
      "237792 242641\n",
      "283869 296762\n",
      "209344 210282\n",
      "118965 114441\n",
      "186503 186856\n",
      "195734 203014\n",
      "254381 249472\n",
      "212401 229111\n",
      "271654 295354\n",
      "319197 335045\n",
      "229829 231671\n"
     ]
    }
   ],
   "source": [
    "for gu in data:\n",
    "    for mf in gu:\n",
    "        print mf,\n",
    "    print"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "74425 76326\n",
      "61164 61636\n",
      "109688 115744\n",
      "144796 146776\n",
      "174996 181676\n",
      "177841 177434\n",
      "204630 205980\n",
      "223373 232245\n",
      "161055 166130\n",
      "171576 176735\n",
      "279169 293772\n",
      "239450 251066\n",
      "148690 156510\n",
      "182977 196992\n",
      "237792 242641\n",
      "283869 296762\n",
      "209344 210282\n",
      "118965 114441\n",
      "186503 186856\n",
      "195734 203014\n",
      "254381 249472\n",
      "212401 229111\n",
      "271654 295354\n",
      "319197 335045\n",
      "229829 231671\n"
     ]
    }
   ],
   "source": [
    "for gu in data:\n",
    "    print gu[0],gu[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "61636\n"
     ]
    }
   ],
   "source": [
    "print data[1][1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4873499 5033671\n",
      "average= 194939.96\n"
     ]
    }
   ],
   "source": [
    "sumM=0\n",
    "sumF=0\n",
    "for gu in data:\n",
    "    sumM+=gu[0]\n",
    "    sumF+=gu[1]\n",
    "print sumM,sumF\n",
    "print \"average=\",float(sumM)/len(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[150751, 122800, 225432, 291572, 356672, 355275, 410610, 455618, 327185, 348311, 572941, 490516, 305200, 379969, 480433, 580631, 419626, 233406, 373359, 398748, 503853, 441512, 567008, 654242, 461500]\n"
     ]
    }
   ],
   "source": [
    "sumGu=list()\n",
    "for gu in data:\n",
    "    sumGu.append(gu[0]+gu[1])\n",
    "print sumGu,\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\nSUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x10e155b90>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "%matplotlib inline\n",
    "\n",
    "import matplotlib\n",
    "import matplotlib.pyplot as plt\n",
    "# 2단계로 나누어 그림\n",
    "plt.bar(range(len(sumGu)), sumGu, align='center')\n",
    "#plt.xticks(range(len(d)), list(d.keys()))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## 데이터구조-10: 커피에 Milk를 추가하는 비율 구하기\n",
    "\n",
    "* 문자로 구성된 2차원 데이터구조의 빈도를 세어서, 백분율을 구하기\n",
    "* 데이터\n",
    "    ```\n",
    "    \"Coffee\",\"Water\",\"Milk\",\"Icecream\"\n",
    "    \"Espresso\",\"No\",\"No\",\"No\"\n",
    "    \"Long Black\",\"Yes\",\"No\",\"No\"\n",
    "    \"Flat White\",\"No\",\"Yes\",\"No\"\n",
    "    \"Cappuccino\",\"No\",\"Yes - Frothy\",\"No\"\n",
    "    \"Affogato\",\"No\",\"No\",\"Yes\"\n",
    "    ```\n",
    "* 프로그래밍 요소\n",
    "    * 2차원 list\n",
    "    * 문자열 데이터의 평균은 빈도를 세어서 한다. 숫자 데이터는 합계를 갯수로 나누어서 구하는 것과 다르다.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "# 2차원 배열.\n",
    "allData=[\n",
    "    [\"Coffee\",\"Water\",\"Milk\",\"Icecream\"],\n",
    "    [\"Espresso\",\"No\",\"No\",\"No\"],\n",
    "    [\"Long Black\",\"Yes\",\"No\",\"No\"],\n",
    "    [\"Flat White\",\"No\",\"Yes\",\"No\"],\n",
    "    [\"Cappuccino\",\"No\",\"Yes\",\"No\"],\n",
    "    [\"Affogato\",\"No\",\"No\",\"Yes\"]\n",
    "]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 데이터 첫 행은 명칭을 가지고 있으므로 제거한다.\n",
    "\n",
    "* 인덱스를 이용하여 전체 데이터에서 첫째행만 제거하고 저장한다.\n",
    "* for문을 이용해서 저장할 수 있다.\n",
    "    * enumerate를 사용하면 몇 번째 데이터인지 추적할 수 있다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['Espresso', 'No', 'No', 'No'], ['Long Black', 'Yes', 'No', 'No'], ['Flat White', 'No', 'Yes', 'No'], ['Cappuccino', 'No', 'Yes', 'No'], ['Affogato', 'No', 'No', 'Yes']]\n"
     ]
    }
   ],
   "source": [
    "data1=allData[1:]\n",
    "print data1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 ['Coffee', 'Water', 'Milk', 'Icecream']\n",
      "1 ['Espresso', 'No', 'No', 'No']\n",
      "2 ['Long Black', 'Yes', 'No', 'No']\n",
      "3 ['Flat White', 'No', 'Yes', 'No']\n",
      "4 ['Cappuccino', 'No', 'Yes', 'No']\n",
      "5 ['Affogato', 'No', 'No', 'Yes']\n"
     ]
    }
   ],
   "source": [
    "data2=list()\n",
    "for i,d in enumerate(allData):\n",
    "    print i,d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['Espresso', 'No', 'No', 'No'], ['Long Black', 'Yes', 'No', 'No'], ['Flat White', 'No', 'Yes', 'No'], ['Cappuccino', 'No', 'Yes', 'No'], ['Affogato', 'No', 'No', 'Yes']]\n"
     ]
    }
   ],
   "source": [
    "data2=list()\n",
    "for i,d in enumerate(allData):\n",
    "    if i>0:\n",
    "        data2.append(d)\n",
    "print data2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2차원 데이터 slicing\n",
    "\n",
    "* 정수 인덱스로 값을 읽음.\n",
    "* 인덱스 ':' 로 시작과 끝을 지정할 수 있슴. 없으면 처음부터 끝까지 읽음.\n",
    "* 2번째 배열인덱스를 고정하면 열데이터를 읽을 수 있슴\n",
    "* 1번째 배열인덱스를 고정하면 행데이터를 읽을 수 있슴."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Espresso', 'No', 'No', 'No']\n"
     ]
    }
   ],
   "source": [
    "print data[0][:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['No', 'No']\n"
     ]
    }
   ],
   "source": [
    "print data[0][1:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Espresso\n",
      "Long Black\n",
      "Flat White\n",
      "Cappuccino\n",
      "Affogato\n"
     ]
    }
   ],
   "source": [
    "for i in data1:\n",
    "    print i[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 커피 종류를 출력해 본다.\n",
    "    * 커피 종류는 첫째 열에 있다. 출력하려면 인덱스 0을 사용한다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Espresso\n",
      "Long Black\n",
      "Flat White\n",
      "Cappuccino\n",
      "Affogato\n"
     ]
    }
   ],
   "source": [
    "for i in data1:\n",
    "    print i[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 커피에 우유를 넣는지 확인해 본다.\n",
    "    * 우유를 넣는지는 2번째 열에 있다. Yes는 우유를 넣고, No는 넣지 않는다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No\n",
      "No\n",
      "Yes\n",
      "Yes\n",
      "No\n"
     ]
    }
   ],
   "source": [
    "print data[0][2]\n",
    "print data[1][2]\n",
    "print data[2][2]\n",
    "print data[3][2]\n",
    "print data[4][2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No\n",
      "No\n",
      "Yes\n",
      "Yes\n",
      "No\n"
     ]
    }
   ],
   "source": [
    "for i in data1:\n",
    "    print i[2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 우유를 넣는 커피를 출력해 본다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Flat White Yes\n",
      "Cappuccino Yes\n"
     ]
    }
   ],
   "source": [
    "for i in data1:\n",
    "    if i[2]==\"Yes\":\n",
    "        print i[0],i[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Flat White Yes\n",
      "Cappuccino Yes\n"
     ]
    }
   ],
   "source": [
    "for i in data1:\n",
    "    if i[2].upper()==\"YES\":\n",
    "        print i[0],i[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of Coffee adding Milk 2\n",
      "% of coffee with milk:  40.0\n"
     ]
    }
   ],
   "source": [
    "count=0\n",
    "for i in data1:\n",
    "    if i[2].upper()=='YES':\n",
    "        count+=1\n",
    "print \"Number of Coffee adding Milk\",count\n",
    "print \"% of coffee with milk: \",100*count/float(len(data1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## 데이터구조-11: 성적데이터의 평균/합계를 구하기.\n",
    "\n",
    "\n",
    "    Subject,scores\n",
    "    English, 100\n",
    "    Math, 80\n",
    "    English, 70\n",
    "    Math, 100\n",
    "    English, 82.3\n",
    "    Math, 98.5\n",
    "\n",
    "* 프로그래밍 요소\n",
    "    * list\n",
    "    * 숫자와 문자가 혼합된 리스트\n",
    "    * 다음 주제인 파일 처리를 연습으로 해 봄.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "image/svg+xml": [
       "<svg height=\"668px\" style=\"width:351px;height:668px;\" version=\"1.1\" viewBox=\"0 0 351 668\" width=\"351px\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\"><defs><filter height=\"300%\" id=\"f1\" width=\"300%\" x=\"-1\" y=\"-1\"><feGaussianBlur result=\"blurOut\" stdDeviation=\"2.0\"/><feColorMatrix in=\"blurOut\" result=\"blurOut2\" type=\"matrix\" values=\"0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .4 0\"/><feOffset dx=\"4.0\" dy=\"4.0\" in=\"blurOut2\" result=\"blurOut3\"/><feBlend in=\"SourceGraphic\" in2=\"blurOut3\" mode=\"normal\"/></filter></defs><g><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"77\" x=\"141.5\" y=\"10\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"57\" x=\"151.5\" y=\"31.6016\">read data</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"83\" x=\"138.5\" y=\"64.1328\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"63\" x=\"148.5\" y=\"85.7344\">engSum=0</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"91\" x=\"134.5\" y=\"118.2656\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"71\" x=\"144.5\" y=\"139.8672\">mathSum=0</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"78\" x=\"141\" y=\"172.3984\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"58\" x=\"151\" y=\"194\">engCnt=0</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"86\" x=\"137\" y=\"226.5313\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"66\" x=\"147\" y=\"248.1328\">mathCnt=0</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"82\" x=\"139\" y=\"324.6641\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"62\" x=\"149\" y=\"346.2656\">read a line</text><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"71.5,378.7969,95.5,378.7969,107.5,390.7969,95.5,402.7969,71.5,402.7969,59.5,390.7969,71.5,378.7969\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"11\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"20\" x=\"73.5\" y=\"394.9541\">eng</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"115\" x=\"26\" y=\"422.7969\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"95\" x=\"36\" y=\"444.3984\">engSum+=mark</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"88\" x=\"39.5\" y=\"476.9297\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"68\" x=\"49.5\" y=\"498.5313\">engCnt+=1</text><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"209,378.7969,236,378.7969,248,390.7969,236,402.7969,209,402.7969,197,390.7969,209,378.7969\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"11\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"27\" x=\"209\" y=\"394.9541\">math</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"123\" x=\"161\" y=\"422.7969\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"103\" x=\"171\" y=\"444.3984\">mathSum+=mark</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"96\" x=\"174.5\" y=\"476.9297\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"76\" x=\"184.5\" y=\"498.5313\">mathCnt+=1</text><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"161,280.6641,199,280.6641,211,292.6641,199,304.6641,161,304.6641,149,292.6641,161,280.6641\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"11\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"38\" x=\"161\" y=\"296.8213\">i&lt;=eof</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"153\" x=\"103.5\" y=\"573.0625\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"133\" x=\"113.5\" y=\"594.6641\">print engSum,mathSum</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"253\" x=\"53.5\" y=\"627.1953\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"233\" x=\"63.5\" y=\"648.7969\">print engSum/engCnt,mathSum/mathCnt</text><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"180\" x2=\"180\" y1=\"44.1328\" y2=\"64.1328\"/><polygon fill=\"#A80036\" points=\"176,54.1328,180,64.1328,184,54.1328,180,58.1328\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"180\" x2=\"180\" y1=\"98.2656\" y2=\"118.2656\"/><polygon fill=\"#A80036\" points=\"176,108.2656,180,118.2656,184,108.2656,180,112.2656\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"180\" x2=\"180\" y1=\"152.3984\" y2=\"172.3984\"/><polygon fill=\"#A80036\" points=\"176,162.3984,180,172.3984,184,162.3984,180,166.3984\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"180\" x2=\"180\" y1=\"206.5313\" y2=\"226.5313\"/><polygon fill=\"#A80036\" points=\"176,216.5313,180,226.5313,184,216.5313,180,220.5313\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"83.5\" x2=\"83.5\" y1=\"456.9297\" y2=\"476.9297\"/><polygon fill=\"#A80036\" points=\"79.5,466.9297,83.5,476.9297,87.5,466.9297,83.5,470.9297\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"222.5\" x2=\"222.5\" y1=\"456.9297\" y2=\"476.9297\"/><polygon fill=\"#A80036\" points=\"218.5,466.9297,222.5,476.9297,226.5,466.9297,222.5,470.9297\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"83.5\" x2=\"83.5\" y1=\"402.7969\" y2=\"422.7969\"/><polygon fill=\"#A80036\" points=\"79.5,412.7969,83.5,422.7969,87.5,412.7969,83.5,416.7969\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"83.5\" x2=\"83.5\" y1=\"511.0625\" y2=\"531.0625\"/><polygon fill=\"#A80036\" points=\"79.5,521.0625,83.5,531.0625,87.5,521.0625,83.5,525.0625\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"222.5\" x2=\"222.5\" y1=\"402.7969\" y2=\"422.7969\"/><polygon fill=\"#A80036\" points=\"218.5,412.7969,222.5,422.7969,226.5,412.7969,222.5,416.7969\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"222.5\" x2=\"222.5\" y1=\"511.0625\" y2=\"531.0625\"/><polygon fill=\"#A80036\" points=\"218.5,521.0625,222.5,531.0625,226.5,521.0625,222.5,525.0625\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"107.5\" x2=\"197\" y1=\"390.7969\" y2=\"390.7969\"/><polygon fill=\"#A80036\" points=\"187,386.7969,197,390.7969,187,394.7969,191,390.7969\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"180\" x2=\"180\" y1=\"358.7969\" y2=\"363.7969\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"180\" x2=\"83.5\" y1=\"363.7969\" y2=\"363.7969\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"83.5\" x2=\"83.5\" y1=\"363.7969\" y2=\"378.7969\"/><polygon fill=\"#A80036\" points=\"79.5,368.7969,83.5,378.7969,87.5,368.7969,83.5,372.7969\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"248\" x2=\"319\" y1=\"390.7969\" y2=\"390.7969\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"319\" x2=\"319\" y1=\"390.7969\" y2=\"531.0625\"/><polygon fill=\"#A80036\" points=\"315,521.0625,319,531.0625,323,521.0625,319,525.0625\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"83.5\" x2=\"319\" y1=\"531.0625\" y2=\"531.0625\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"180\" x2=\"180\" y1=\"304.6641\" y2=\"324.6641\"/><polygon fill=\"#A80036\" points=\"176,314.6641,180,324.6641,184,314.6641,180,318.6641\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"180\" x2=\"180\" y1=\"531.0625\" y2=\"541.0625\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"180\" x2=\"346\" y1=\"541.0625\" y2=\"541.0625\"/><polygon fill=\"#A80036\" points=\"342,440.8633,346,430.8633,350,440.8633,346,436.8633\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"346\" x2=\"346\" y1=\"292.6641\" y2=\"541.0625\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"346\" x2=\"211\" y1=\"292.6641\" y2=\"292.6641\"/><polygon fill=\"#A80036\" points=\"221,288.6641,211,292.6641,221,296.6641,217,292.6641\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"149\" x2=\"14\" y1=\"292.6641\" y2=\"292.6641\"/><polygon fill=\"#A80036\" points=\"10,426.8633,14,436.8633,18,426.8633,14,430.8633\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"14\" x2=\"14\" y1=\"292.6641\" y2=\"553.0625\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"14\" x2=\"180\" y1=\"553.0625\" y2=\"553.0625\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"180\" x2=\"180\" y1=\"553.0625\" y2=\"573.0625\"/><polygon fill=\"#A80036\" points=\"176,563.0625,180,573.0625,184,563.0625,180,567.0625\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"180\" x2=\"180\" y1=\"260.6641\" y2=\"280.6641\"/><polygon fill=\"#A80036\" points=\"176,270.6641,180,280.6641,184,270.6641,180,274.6641\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"180\" x2=\"180\" y1=\"607.1953\" y2=\"627.1953\"/><polygon fill=\"#A80036\" points=\"176,617.1953,180,627.1953,184,617.1953,180,621.1953\" style=\"stroke: #A80036; stroke-width: 1.0;\"/></g></svg>"
      ],
      "text/plain": [
       "<IPython.core.display.SVG object>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%plantuml\n",
    "@startuml\n",
    ":read data;\n",
    ":engSum=0;\n",
    ":mathSum=0;\n",
    ":engCnt=0;\n",
    ":mathCnt=0;\n",
    "while(i<=eof)\n",
    ":read a line;\n",
    "if (eng)\n",
    ":engSum+=mark;\n",
    ":engCnt+=1;\n",
    "elseif (math)\n",
    ":mathSum+=mark;\n",
    ":mathCnt+=1;\n",
    "endif\n",
    "endwhile\n",
    ":print engSum,mathSum;\n",
    ":print engSum/engCnt,mathSum/mathCnt;\n",
    "@enduml"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "marks=[\n",
    "    ['Subject','scores'],\n",
    "    ['English', 100],\n",
    "    ['Math', 80],\n",
    "    ['English', 70],\n",
    "    ['Math', 100],\n",
    "    ['English', 82.3],\n",
    "    ['Math', 98.5]\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "marks=marks[1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "278 252\n",
      "92.0 84.0\n"
     ]
    }
   ],
   "source": [
    "# reading and compute average\n",
    "englishSum=0\n",
    "mathSum=0\n",
    "englishCount=0\n",
    "mathCount=0\n",
    "for row in marks:\n",
    "    subj = row[0]\n",
    "    mark = int(row[1])\n",
    "    if subj==\"English\":\n",
    "        englishSum+=mark\n",
    "        englishCount+=1\n",
    "    elif subj==\"Math\":\n",
    "        mathSum+=mark\n",
    "        mathCount+=1\n",
    "    else:\n",
    "        pass\n",
    "print mathSum,englishSum\n",
    "print float(mathSum/mathCount),float(englishSum/englishCount)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 파일로 처리하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing marks.csv\n"
     ]
    }
   ],
   "source": [
    "%%file marks.csv\n",
    "English, 100\n",
    "Math, 200\n",
    "English, 200\n",
    "Math, 200\n",
    "English, 100\n",
    "Math, 300"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# csv reading\n",
    "import csv\n",
    "csvfile=open('marks.csv', 'rb')\n",
    "marks=csv.reader(csvfile, delimiter=',')\n",
    "for row in marks:\n",
    "    print row\n",
    "csvfile.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['English', ' 100']\n",
      "['Math', ' 200']\n",
      "['English', ' 200']\n",
      "['Math', ' 200']\n",
      "['English', ' 100']\n",
      "['Math', ' 300']\n",
      "700 400\n",
      "233.0 133.0\n"
     ]
    }
   ],
   "source": [
    "# reading and compute average\n",
    "csvfile=open('marks.csv', 'rb')\n",
    "marks=csv.reader(csvfile, delimiter=',')\n",
    "englishSum=0\n",
    "mathSum=0\n",
    "englishCount=0\n",
    "mathCount=0\n",
    "for row in marks:\n",
    "    subj = row[0]\n",
    "    mark = int(row[1])\n",
    "    if subj==\"English\":\n",
    "        englishSum+=mark\n",
    "        englishCount+=1\n",
    "    elif subj==\"Math\":\n",
    "        mathSum+=mark\n",
    "        mathCount+=1\n",
    "    else:\n",
    "        pass\n",
    "csvfile.close()\n",
    "print mathSum,englishSum\n",
    "print float(mathSum/mathCount),float(englishSum/englishCount)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## 데이터구조-12: The Beatles 'Let it be' 가사에서 자주 등장하는 단어는?\n",
    "\n",
    "* 20번 이상 사용된 단어를 출력\n",
    "* 프로그래밍 요소\n",
    "    * dict, list\n",
    "* 주의\n",
    "    * 텍스트 처리: 단어 -> 문장 -> 문서"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "image/svg+xml": [
       "<svg height=\"917px\" style=\"width:339px;height:917px;\" version=\"1.1\" viewBox=\"0 0 339 917\" width=\"339px\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\"><defs><filter height=\"300%\" id=\"f1\" width=\"300%\" x=\"-1\" y=\"-1\"><feGaussianBlur result=\"blurOut\" stdDeviation=\"2.0\"/><feColorMatrix in=\"blurOut\" result=\"blurOut2\" type=\"matrix\" values=\"0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .4 0\"/><feOffset dx=\"4.0\" dy=\"4.0\" in=\"blurOut2\" result=\"blurOut3\"/><feBlend in=\"SourceGraphic\" in2=\"blurOut3\" mode=\"normal\"/></filter></defs><g><ellipse cx=\"181\" cy=\"20\" fill=\"#000000\" filter=\"url(#f1)\" rx=\"10\" ry=\"10\" style=\"stroke: none; stroke-width: 1.0;\"/><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"67\" x=\"147.5\" y=\"50\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"47\" x=\"157.5\" y=\"71.6016\">set data</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"139\" x=\"111.5\" y=\"104.1328\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"119\" x=\"121.5\" y=\"125.7344\">initialize dictionary d</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"134\" x=\"114\" y=\"202.2656\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"114\" x=\"124\" y=\"223.8672\">get a line from data</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"132\" x=\"115\" y=\"300.3984\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"112\" x=\"125\" y=\"322\">split line into words</text><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"153,354.5313,209,354.5313,221,366.5313,209,378.5313,153,378.5313,141,366.5313,153,354.5313\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"11\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"56\" x=\"153\" y=\"370.6885\">words in d</text><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"11\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"18\" x=\"123\" y=\"364.2109\">yes</text><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"11\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"14\" x=\"221\" y=\"364.2109\">no</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"87\" x=\"87.5\" y=\"388.5313\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"67\" x=\"97.5\" y=\"410.1328\">count += 1</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"73\" x=\"194.5\" y=\"388.5313\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"53\" x=\"204.5\" y=\"410.1328\">count =1</text><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"181,428.6641,193,440.6641,181,452.6641,169,440.6641,181,428.6641\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"169,256.3984,193,256.3984,205,268.3984,193,280.3984,169,280.3984,157,268.3984,169,256.3984\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"11\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"19\" x=\"171.5\" y=\"272.5557\">line</text><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"169,158.2656,193,158.2656,205,170.2656,193,182.2656,169,182.2656,157,170.2656,169,158.2656\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"11\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"23\" x=\"169.5\" y=\"174.4229\">data</text><rect fill=\"#FFFFFF\" filter=\"url(#f1)\" height=\"362.3984\" style=\"stroke: #000000; stroke-width: 2.0;\" width=\"322\" x=\"10\" y=\"507.6641\"/><path d=\"M76,508.6641 L76,514.6641 L66,524.6641 L10,524.6641 \" fill=\"#FFFFFF\" style=\"stroke: #000000; stroke-width: 2.0;\"/><text fill=\"#000000\" font-family=\"Serif\" font-size=\"14\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"56\" x=\"13\" y=\"519.1641\">frequency</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"81\" x=\"140.5\" y=\"541.6641\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"61\" x=\"150.5\" y=\"563.2656\">set criteria</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"99\" x=\"131.5\" y=\"658.7969\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"79\" x=\"141.5\" y=\"680.3984\">get frequency</text><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"99,727.9297,263,727.9297,275,739.9297,263,751.9297,99,751.9297,87,739.9297,99,727.9297\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"11\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"164\" x=\"99\" y=\"744.0869\">frequency greater than criteria</text><rect fill=\"#FEFECE\" filter=\"url(#f1)\" height=\"34.1328\" rx=\"12.5\" ry=\"12.5\" style=\"stroke: #A80036; stroke-width: 1.5;\" width=\"46\" x=\"54\" y=\"761.9297\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"12\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"26\" x=\"64\" y=\"783.5313\">save</text><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"181,802.0625,193,814.0625,181,826.0625,169,814.0625,181,802.0625\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><polygon fill=\"#FEFECE\" filter=\"url(#f1)\" points=\"169,610.7969,193,610.7969,205,622.7969,193,634.7969,169,634.7969,157,622.7969,169,610.7969\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><text fill=\"#000000\" font-family=\"sans-serif\" font-size=\"11\" lengthAdjust=\"spacingAndGlyphs\" textLength=\"7\" x=\"177.5\" y=\"626.9541\">d</text><ellipse cx=\"181\" cy=\"900.0625\" fill=\"none\" filter=\"url(#f1)\" rx=\"10\" ry=\"10\" style=\"stroke: #000000; stroke-width: 1.0;\"/><ellipse cx=\"181.5\" cy=\"900.5625\" fill=\"#000000\" filter=\"url(#f1)\" rx=\"6\" ry=\"6\" style=\"stroke: none; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"181\" y1=\"30\" y2=\"50\"/><polygon fill=\"#A80036\" points=\"177,40,181,50,185,40,181,44\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"181\" y1=\"84.1328\" y2=\"104.1328\"/><polygon fill=\"#A80036\" points=\"177,94.1328,181,104.1328,185,94.1328,181,98.1328\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"141\" x2=\"131\" y1=\"366.5313\" y2=\"366.5313\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"131\" x2=\"131\" y1=\"366.5313\" y2=\"388.5313\"/><polygon fill=\"#A80036\" points=\"127,378.5313,131,388.5313,135,378.5313,131,382.5313\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"221\" x2=\"231\" y1=\"366.5313\" y2=\"366.5313\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"231\" x2=\"231\" y1=\"366.5313\" y2=\"388.5313\"/><polygon fill=\"#A80036\" points=\"227,378.5313,231,388.5313,235,378.5313,231,382.5313\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"131\" x2=\"131\" y1=\"422.6641\" y2=\"440.6641\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"131\" x2=\"169\" y1=\"440.6641\" y2=\"440.6641\"/><polygon fill=\"#A80036\" points=\"159,436.6641,169,440.6641,159,444.6641,163,440.6641\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"231\" x2=\"231\" y1=\"422.6641\" y2=\"440.6641\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"231\" x2=\"193\" y1=\"440.6641\" y2=\"440.6641\"/><polygon fill=\"#A80036\" points=\"203,436.6641,193,440.6641,203,444.6641,199,440.6641\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"181\" y1=\"334.5313\" y2=\"354.5313\"/><polygon fill=\"#A80036\" points=\"177,344.5313,181,354.5313,185,344.5313,181,348.5313\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"181\" y1=\"280.3984\" y2=\"300.3984\"/><polygon fill=\"#A80036\" points=\"177,290.3984,181,300.3984,185,290.3984,181,294.3984\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"181\" y1=\"452.6641\" y2=\"462.6641\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"289.5\" y1=\"462.6641\" y2=\"462.6641\"/><polygon fill=\"#A80036\" points=\"285.5,367.0313,289.5,357.0313,293.5,367.0313,289.5,363.0313\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"289.5\" x2=\"289.5\" y1=\"268.3984\" y2=\"462.6641\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"289.5\" x2=\"205\" y1=\"268.3984\" y2=\"268.3984\"/><polygon fill=\"#A80036\" points=\"215,264.3984,205,268.3984,215,272.3984,211,268.3984\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"157\" x2=\"65.5\" y1=\"268.3984\" y2=\"268.3984\"/><polygon fill=\"#A80036\" points=\"61.5,353.0313,65.5,363.0313,69.5,353.0313,65.5,357.0313\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"65.5\" x2=\"65.5\" y1=\"268.3984\" y2=\"474.6641\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"65.5\" x2=\"301.5\" y1=\"474.6641\" y2=\"474.6641\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"301.5\" x2=\"301.5\" y1=\"170.2656\" y2=\"474.6641\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"301.5\" x2=\"205\" y1=\"170.2656\" y2=\"170.2656\"/><polygon fill=\"#A80036\" points=\"215,166.2656,205,170.2656,215,174.2656,211,170.2656\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"181\" y1=\"236.3984\" y2=\"256.3984\"/><polygon fill=\"#A80036\" points=\"177,246.3984,181,256.3984,185,246.3984,181,250.3984\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"181\" y1=\"182.2656\" y2=\"202.2656\"/><polygon fill=\"#A80036\" points=\"177,192.2656,181,202.2656,185,192.2656,181,196.2656\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"157\" x2=\"41.5\" y1=\"170.2656\" y2=\"170.2656\"/><polygon fill=\"#A80036\" points=\"37.5,321.4648,41.5,331.4648,45.5,321.4648,41.5,325.4648\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"41.5\" x2=\"41.5\" y1=\"170.2656\" y2=\"496.6641\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"41.5\" x2=\"181\" y1=\"496.6641\" y2=\"496.6641\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"181\" y1=\"496.6641\" y2=\"541.6641\"/><polygon fill=\"#A80036\" points=\"177,531.6641,181,541.6641,185,531.6641,181,535.6641\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"181\" y1=\"138.2656\" y2=\"158.2656\"/><polygon fill=\"#A80036\" points=\"177,148.2656,181,158.2656,185,148.2656,181,152.2656\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"87\" x2=\"77\" y1=\"739.9297\" y2=\"739.9297\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"77\" x2=\"77\" y1=\"739.9297\" y2=\"761.9297\"/><polygon fill=\"#A80036\" points=\"73,751.9297,77,761.9297,81,751.9297,77,755.9297\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"275\" x2=\"285\" y1=\"739.9297\" y2=\"739.9297\"/><polygon fill=\"#A80036\" points=\"281,766.9961,285,776.9961,289,766.9961,285,770.9961\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"285\" x2=\"285\" y1=\"739.9297\" y2=\"814.0625\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"285\" x2=\"193\" y1=\"814.0625\" y2=\"814.0625\"/><polygon fill=\"#A80036\" points=\"203,810.0625,193,814.0625,203,818.0625,199,814.0625\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"77\" x2=\"77\" y1=\"796.0625\" y2=\"814.0625\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"77\" x2=\"169\" y1=\"814.0625\" y2=\"814.0625\"/><polygon fill=\"#A80036\" points=\"159,810.0625,169,814.0625,159,818.0625,163,814.0625\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"181\" y1=\"692.9297\" y2=\"727.9297\"/><polygon fill=\"#A80036\" points=\"177,717.9297,181,727.9297,185,717.9297,181,721.9297\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"181\" y1=\"634.7969\" y2=\"658.7969\"/><polygon fill=\"#A80036\" points=\"177,648.7969,181,658.7969,185,648.7969,181,652.7969\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"181\" y1=\"826.0625\" y2=\"838.0625\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"322\" y1=\"838.0625\" y2=\"838.0625\"/><polygon fill=\"#A80036\" points=\"318,740.4297,322,730.4297,326,740.4297,322,736.4297\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"322\" x2=\"322\" y1=\"622.7969\" y2=\"838.0625\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"322\" x2=\"205\" y1=\"622.7969\" y2=\"622.7969\"/><polygon fill=\"#A80036\" points=\"215,618.7969,205,622.7969,215,626.7969,211,622.7969\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"157\" x2=\"32\" y1=\"622.7969\" y2=\"622.7969\"/><polygon fill=\"#A80036\" points=\"28,726.4297,32,736.4297,36,726.4297,32,730.4297\" style=\"stroke: #A80036; stroke-width: 1.5;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"32\" x2=\"32\" y1=\"622.7969\" y2=\"850.0625\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"32\" x2=\"181\" y1=\"850.0625\" y2=\"850.0625\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"181\" y1=\"850.0625\" y2=\"890.0625\"/><polygon fill=\"#A80036\" points=\"177,880.0625,181,890.0625,185,880.0625,181,884.0625\" style=\"stroke: #A80036; stroke-width: 1.0;\"/><line style=\"stroke: #A80036; stroke-width: 1.5;\" x1=\"181\" x2=\"181\" y1=\"575.7969\" y2=\"610.7969\"/><polygon fill=\"#A80036\" points=\"177,600.7969,181,610.7969,185,600.7969,181,604.7969\" style=\"stroke: #A80036; stroke-width: 1.0;\"/></g></svg>"
      ],
      "text/plain": [
       "<IPython.core.display.SVG object>"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%plantuml\n",
    "@startuml\n",
    "start\n",
    ":set data;\n",
    ":initialize dictionary d;\n",
    "while(data)\n",
    ":get a line from data;\n",
    "while(line)\n",
    ":split line into words;\n",
    "if (words in d) then(yes)\n",
    ":count += 1;\n",
    "else (no)\n",
    ":count =1;\n",
    "endif\n",
    "endwhile\n",
    "endwhile\n",
    "partition frequency {\n",
    "    :set criteria;\n",
    "    while(d)\n",
    "        :get frequency;\n",
    "        if(frequency greater than criteria)\n",
    "            :save;\n",
    "        endif\n",
    "    endwhile\n",
    "}\n",
    "stop\n",
    "@enduml"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Let it be 가사\n",
    "doc=[\n",
    "    \"When I find myself in times of trouble\",\n",
    "    \"Mother Mary comes to me\",\n",
    "    \"Speaking words of wisdom, let it be\",\n",
    "    \"And in my hour of darkness\",\n",
    "    \"She is standing right in front of me\",\n",
    "    \"Speaking words of wisdom, let it be\",\n",
    "    \"Let it be\",\n",
    "    \"Let it be\",\n",
    "    \"Let it be\",\n",
    "    \"Let it be\",\n",
    "    \"Whisper words of wisdom, let it be\"\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "When I find myself in times of trouble\n",
      "Mother Mary comes to me\n",
      "Speaking words of wisdom, let it be\n",
      "And in my hour of darkness\n",
      "She is standing right in front of me\n",
      "Speaking words of wisdom, let it be\n",
      "Let it be\n",
      "Let it be\n",
      "Let it be\n",
      "Let it be\n",
      "Whisper words of wisdom, let it be\n"
     ]
    }
   ],
   "source": [
    "for sentence in doc:\n",
    "    print sentence"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "When I find myself in times of trouble\n",
      "Mother Mary comes to me\n",
      "Speaking words of wisdom, let it be\n",
      "And in my hour of darkness\n",
      "She is standing right in front of me\n",
      "Speaking words of wisdom, let it be\n",
      "Let it be\n",
      "Let it be\n",
      "Let it be\n",
      "Let it be\n",
      "Whisper words of wisdom, let it be\n"
     ]
    }
   ],
   "source": [
    "for sentence in doc:\n",
    "    words=sentence.split()\n",
    "    for word in words:\n",
    "        print word,\n",
    "    print"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "doc1=[\n",
    "    [\"When I find myself in times of trouble\"],\n",
    "    [\"Mother Mary comes to me\"],\n",
    "    [\"Speaking words of wisdom, let it be\"],\n",
    "    [\"And in my hour of darkness\"],\n",
    "    [\"She is standing right in front of me\"],\n",
    "    [\"Speaking words of wisdom, let it be\"],\n",
    "    [\"Let it be\"],\n",
    "    [\"Let it be\"],\n",
    "    [\"Let it be\"],\n",
    "    [\"Let it be\"],\n",
    "    [\"Whisper words of wisdom, let it be\"]\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "When I find myself in times of trouble\n",
      "Mother Mary comes to me\n",
      "Speaking words of wisdom, let it be\n",
      "And in my hour of darkness\n",
      "She is standing right in front of me\n",
      "Speaking words of wisdom, let it be\n",
      "Let it be\n",
      "Let it be\n",
      "Let it be\n",
      "Let it be\n",
      "Whisper words of wisdom, let it be\n"
     ]
    }
   ],
   "source": [
    "for sentence in doc1:\n",
    "    for word in sentence:\n",
    "        print word"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "d = dict()\n",
    "for sentence in doc:\n",
    "    words=sentence.split()\n",
    "    for word in words:\n",
    "        if word in d:\n",
    "            d[word]+=1\n",
    "        else:\n",
    "            d[word]=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'right': 1, 'be': 7, 'is': 1, 'When': 1, 'it': 7, 'in': 3, 'Mary': 1, 'Speaking': 2, 'standing': 1, 'darkness': 1, 'find': 1, 'wisdom,': 3, 'to': 1, 'Let': 4, 'And': 1, 'I': 1, 'let': 3, 'She': 1, 'words': 3, 'Mother': 1, 'front': 1, 'trouble': 1, 'me': 2, 'myself': 1, 'hour': 1, 'of': 6, 'times': 1, 'Whisper': 1, 'my': 1, 'comes': 1}\n"
     ]
    }
   ],
   "source": [
    "print d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "be\n",
      "it\n",
      "in\n",
      "wisdom,\n",
      "Let\n",
      "let\n",
      "words\n",
      "of\n"
     ]
    }
   ],
   "source": [
    "# 3회 이상 등장한 단어\n",
    "c=2\n",
    "for k in d:\n",
    "    if d[k]>c:\n",
    "        print k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Frequent words:  ['be', 'it', 'in', 'wisdom,', 'Let', 'let', 'words', 'of']\n"
     ]
    }
   ],
   "source": [
    "def countWords(doc):\n",
    "    d = {}\n",
    "    for sentence in doc:\n",
    "        words=sentence.split()\n",
    "        for word in words:\n",
    "            if word in d:\n",
    "                d[word]+=1\n",
    "            else:\n",
    "                d[word]=1\n",
    "    return d\n",
    "\n",
    "def getWordsFreqGreater(c,d):\n",
    "    w=list()\n",
    "    for k in d:\n",
    "        if d[k]>c:\n",
    "            w.append(k)\n",
    "    return w\n",
    "\n",
    "wordDict=countWords(doc)\n",
    "freqWordsList=getWordsFreqGreater(2,wordDict)\n",
    "print \"Frequent words: \",freqWordsList"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### 문장의 인식\n",
    "\n",
    "* 문장을 분리하는 것은 쉽지 않다. (아래는 자습).\n",
    "* 문장 압축."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "string With Punctuation\n",
      "set(['!', '#', '\"', '%', '$', \"'\", '&', ')', '(', '+', '*', '-', ',', '/', '.', ';', ':', '=', '<', '?', '>', '@', '[', ']', '\\\\', '_', '^', '`', '{', '}', '|', '~'])\n",
      "string With Punctuation\n"
     ]
    }
   ],
   "source": [
    "#py4i:113\n",
    "import string\n",
    "s = \"string. With. Punctuation?\" # Sample string \n",
    "out = s.translate(string.maketrans(\"\",\"\"), string.punctuation)\n",
    "print out\n",
    "exclude = set(string.punctuation)\n",
    "print exclude\n",
    "s = ''.join(ch for ch in s if ch not in exclude)\n",
    "print s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x��H���W(�/�IQ� �\r",
      "\u0000�[\u0011�\n",
      "hello world!hello world!hello world!hello world!\n"
     ]
    }
   ],
   "source": [
    "#Please write a program to compress and decompress the string \"hello world!hello world!hello world!hello world!\".\n",
    "#Hints:Use zlib.compress() and zlib.decompress() to compress and decompress a string.\n",
    "\n",
    "import zlib\n",
    "s = 'hello world!hello world!hello world!hello world!'\n",
    "t = zlib.compress(s)\n",
    "print t\n",
    "print zlib.decompress(t)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 데이터구조-13: 시간표를 데이터구조로 저장하기\n",
    "\n",
    "* 자신이 \n",
    "* 리스트 -2 차원\n",
    "* 사전\n",
    "\n",
    "timetable = list()\n",
    "\n",
    "timetable.append('math')\n",
    "timetable.append('english')\n",
    "print timetable\n",
    "\n",
    "timetable = list()\n",
    "\n",
    "timetable=[['math'],['english']]\n",
    "print timetable\n",
    "print timetable[0][0]\n",
    "\n",
    "timetable = dict()\n",
    "\n",
    "timetable['mon'][.append('math')\n",
    "timetable.append('englihs')\n",
    "print timetable"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## 과제\n",
    "\n",
    "* 1. 서울시 통계학교생활 만족도 평균을 구하는 프로그램 작성\n",
    "    * 서울열린데이터광장 data.seoul.go.kr > 검색 '통계학교생활'\n",
    "    * 매우만족+만족 평균, 불만족+매우불만족 평균\n",
    "\n",
    "* 2 . 대통령 연설 2개를 분석해서 빈번한 단어의 차이를 보여주는 프로그램 작성\n",
    "    * 미국대통령 취임연설 (한글처리가능하면 한국대통령 취임연설) 가운데 최근 것과 과거 것 1개씩 선택\n",
    "    * 가장 많이 등장하는 단어 10개씩을 추출하여 비교.\n",
    "    * http://www.infoplease.com/t/hist/inaugural/\n",
    "\n",
    "* 제출기한\n",
    "    * 금요일 오후 5시\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "public class Subject {\n",
    "    private String name;\n",
    "    public void setName(String name)   {     this.name = name;   }\n",
    "    public String getName()   {     return name;   } }\n",
    "public class Student {    private Subject[] studyAreas = new Subject[10];\n",
    "                      //the rest of the Student class }\n"
   ]
  }
 ],
 "metadata": {
  "celltoolbar": "Slideshow",
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
