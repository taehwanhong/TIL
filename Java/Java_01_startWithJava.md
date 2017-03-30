
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

