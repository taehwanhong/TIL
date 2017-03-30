
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


### 함수
```
//   public static returntype functionName(arg1, arg2){
//	 }
```

자바는 모든지 다 클래스임.... 
```
public class Main {

	
	public static void sayHello(int n){
		for(int i=0; i<n; i++){
			System.out.println(i + "hello");
			
		}
	}
	
	public static void main(String[] args){
		sayHello(5);
	}

}
```

### 클래스와 오브젝트

오브젝트
 - state와 behavior가 있는 SW 꾸러미
 - state : 변수
 - behavior : 메소드
 - 인스턴스와 같은 내용.
 - 값이 바뀌지 않는것은 immutable

 클래스
 - 오브젝트를 만들기 위한 틀, 템플릿이 클래스임
 - 자바에서는 항상new라는 키워드를 이용해야.
 - String은 new없이 만들수 있는 유일한 클래스
 - user defined data type with behavior

한 파일에 class하나씩!!!! 그래서 프로그램이 커지면 파일이 엄청 많아짐.

같은 폴더(패키지)에 있는 클래스들끼리는 참조 안달아줘도 괜찮음.

Main.java
```
public class Main {

	
	public static void sayHello(int n){
		for(int i=0; i<n; i++){
			System.out.println(i + "hello");
			
		}
	}
	
	public static void main(String[] args){
		Car c1 = new Car(); // 인스턴스 c1이 생성
        Car c2 = new Car();
        c1.name = "mirai";
        c2.name = "bmw";
        c1.color = "red";//color가 static이라서 모든 곳에 적용됨.
        
        c1.accel(10);
        c2.accel(100);
        c1.print();  
        c2.print();
        
	}

}
```
Car.java
```
package ex1;

public class Car {
    //state와 behavior
    //STATE define
	//instance variable :인스턴스마다 각각 따로 값을 가지는것.
	public static String color;
    public int speed;
    public String name;
    
    //class variable : 클래스 전체에서 이건 공유하는 변수(static변수)
    public static int numberWheel = 4;
//    
//  @param x 만큼 가속  
//    
    //method
    public void accel(int speed){
//    	speed += x;
    	this.speed += speed;
    }
    public void print(){
    	System.out.println(this.name + " " + car.color + " " + this.speed);
    }
}
```


### 객체지향 Class

하는 애를 super class, 당하는애를 sub class

class는 분류라는 뜻임. 사람은 분류하면 포유류 class임.

People을 상속 받아서 Student를 만든다던지

People에는 eat, walk, name, age, money가 있다고하면,
Student는 People을 상속받았으니 eat walk는 기본빵.

### 추상 클래스
추상메소드를 가지고 있으면, 추상 클래스가 됌
이런애들은 객체를 생성할수 없음.
대신에 상속받은 애한테서 추상 메소드를 정의해서 사용가능함.



```
public abstract class People {
	public int age;
	public String name;
	public float weight;
	public abstract void walk();
	//abstract...
	//추상 메소드는 행동이 없음. 
	//메소드에 본문이 없음.
	//구현 안한거는 상속받은 애. sub가 구현해야함. 그래서 이렇게 써놓으면 student에서 에러뜸.
	//추상클래스는 객체를 만들어낼수 없음. 정의가 안되어 있으니깐.	
}
```

```
public class Student extends People {
    public int score;
    public void study(int hour){
    	super.weight += 1 * hour;//super는 부모를 지칭,
    	score++;
    }


	@Override
	public void walk() {
		// TODO Auto-generated method stub
		super.weight -= 1;
	}
	
}
```

### 인터페이스

다중상속을 위해 자바에만 있는 특이한 클래스.
인터페이스는 능력에 대한게 많음 serializable 이런거.

이게 왜 있냐면, 자바에서는 상속이 하나밖에 안됨

구현된게 아무것도 없고, 몸통이 없음.

이걸 쓰는 이유는 강제하는것임. 최대한 견고하게!
유지보수를 잘하기 위해서, 대용량 프로그램을 하기위해서 객체지향으로!




### 배열 Array

int[] a = new int [10];
int[][]b = new int [5][10];

Car[] c = new Car[5];
c[0].name = "subway"; // error
이렇게 하면, 참조에 new가 안되서 참조만 있어서 작동하지 않음

Car[] c = new Car[5];
c[0] = new Car();
c[0].name = "subway"; // error
//위처럼 c[0]에 new해줘서 참조가 가르치도록 해야함.


for (i = 0; i < 10 ; i++){
    a[i] = i *2;
    System.out.println(a[i]);
}


new로 만든다는건 이건 객체라는거임.
new로 만들면 힙 이라는곳에 쌓임.

### 리스트와 해시맵

**java에서 가장 많이 쓰는 자료형**

````
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args){

        List <Car> carList = new ArrayList<car>();
        Car c = new Car();
        c.name = "sm3";
        carList.add(c);
        Car x = carList.get(0);

        System.out.println(x.name);
        System.out.println(c == x);

    }
}
````


[제네릭 : 아무거나 담을수 있는 그릇.](https://opentutorials.org/course/1223/6237)

