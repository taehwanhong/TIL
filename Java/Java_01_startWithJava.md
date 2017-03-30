
* 볼책: 코딩 인터뷰 완전 분석
* 

## 환경 구축

### java 설치
  > 생활코딩 참고     
  > oracle에서 mac osx 로 설치하면 됨.

### 버전 확인.
  > javac -version      
  > STS spring에 맞게 만든 tool도 있음.

### 시작하기 hello

Hello.java
```
  public class Hello{
   public static void main(String[] args){
        System.out.println("hello world");
     }
}
```

그리고 터미널에서, 

``` bash
David-Mac-pro15:jinnycast davidhong$ javac hello.java
David-Mac-pro15:jinnycast davidhong$ java hello
hello world
```
javac는 자바 컴파일러임.
자바는 컴파일 언어라서 컴파일을 꼭 한번씩 해줘야함


>1. class명은 무조건 대문자로 시작합니다. 컨벤션이니깐 따르도록
>2. 파일 이름은 class이름 그중에서도 public class와 같아야함.
>3. main 함수가 있어야함. 반드시! 여기가 시작점임 이게 없으면 실행이 안됌
>4. **모든 자바 프로그램은 public class의 main method로부터 시작함.**


위 코드를 간단히 Review하면,
```
  public class Hello{
  //entry point
   public static void main(String[] args){ //main함수가 있음.
        System.out.println("hello world"); //System Class의 out이라는 객체가 가지고 있는 println이라는 method를 실행하겠다.
     }
}
```

> 자바는 C언어에 객체지향을 넣고 쉽게 만든것임  
> C언어도 main함수부터 시작함. 함수는 항상 return이 있었음.

#### 항상 main부터 짜겠음.

* Main.java
```
public class Main {
    public static void main(String[] args){
        // your code here
        System.out.println("i am main");
    }
}
```

* terminal에서...
```bash
David-Mac-pro15:jinnycast davidhong$ vi Main.java
David-Mac-pro15:jinnycast davidhong$ javac Main.java
David-Mac-pro15:jinnycast davidhong$ java Main
```

## Why java

면접때 가장 많이 봄.
코드를 이해하면 됌. 굳이 자바로 안짜도 됌


### Data type

1. class
    클래스는...
2. primitive
    - 숫자 타입 : 
        * byte(0~255, signed일때, -255~255, 00~FF),
        * short : 
        * int : 4byte 2^32 = 40억까지 됌 -20억~+20억 사이.
        * long, : 8byte 
        * float : 부동소수점(근사치,)
        * double : float에 비해 두배 정확
    - boolean : true, false임
    - char : 1글짜 문자열, 사실 이런 타입은 없고 이거도 숫자로 저장함.ㅋ

3. String
    - class이지만, primitive와 유사.
    - **immutable : 한번 만들어진 객체의 값을 바꿀수 없다.**

4. 기본값
    - 초기화를 하지 않은값.
    - 숫자 타입의 기본값은 0
    - string은 null

5. 리터럴...?코드 안에서 값을 표현하기 위한 모든 방식.
    - 1, true, 'a', "A"
    - 숫자 타입의 리터럴 1
    - boolean type의 리터럴 true
    - [리터럴에 대한 위키피디아](https://ko.wikipedia.org/wiki/리터럴)

### 조건문
```
// IF문
    if(a!=5){
        System.out.println("ok");
    }
    else if(a!=10){
        System.out.println("ok3");
        System.out.println("ok4");
    } else {
        System.out.println("ok5");
    }
//For문
    int i = 0
    int j = 0;
    for (i=0 j=1 ; i<10; i++, j--){
        System.out.println(i + "" +j);
    }
    System.out.println(i);
```



### eclipse에서 해보자.

New Class로 만듬
Main.java
```
package ex1;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Hello Ecl");
	}

}
```

Run as Java application

result
```
Hello Ecl
```

### Memory (String의 immutable을 이해하기 위하여.)

4G = 2^16

int a = 4 // 어딘가에 4를 할당. 0000 0000 ~ 0000 0003
double b = 3.5 // 어딘가에 8byte임 0000 0004 ~ 000???

memory는 stack이라서 쌓아감.

근데 string c =  "hello";
이건 hip이라는 곳에 잡음...(어딘가....)

그래놓고 string class가 저장된 주소값을 저장하는것을 참조, reference라고함.

primitive type이 아닌 경우는 대부분 refercence값을 저장함.

a=4
b=3.5
c=[] -> hello //참조 타입은 이렇게표시함.

String은 immutable이기때문에. 만약에 c = c + world하면,
어딘가에 hello world를 새로 만들고, 참조를 바꿈.

c=[] -> hello world를 가르킴.

이후 사용되지 않는 hello는 가비지 콜렉터가 치움.


