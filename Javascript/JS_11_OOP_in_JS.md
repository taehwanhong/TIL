# Javascript ES2015

## OOP in ES2015
> JS의 ES2015기준부터는 클래스가 본격적으로 도입됨.
> 객체의 주요 개념에는 클래스, 상속, 은닉 등이 있는데 이런개념들이 더욱 구체적으로 구현됨
> 사실 잘 모르지만 검색등을 통해 공부한 내용을 정리해보고자 함.
> 특히 이번 TIL에서는, JS의 OOP를 좀더 공부해보겠습니다.

## Class
자 아래 코드를 보자. 미래에 복습할 나에게 우선 사과 한다. 시작부터 코드를 보여줘 미안하다. 너가 원래 이렇다.
```
// 선언방법 1
function MyClass(){

}
// 선언방법 2
var MyClass = function(){

}
```
- 위 구문 둘다 MyClass 라는 '클래스'를 선언한다.
- 사실 근데 공부해보면, 두개의 작동방식은 조금 다르다(생성 시점이 다름)

###그리고 ES2015에서의 Class는 아래와 같이 선언가능함.
```
class Health{
    constructor(name, lastTime){
        this.name = name;
        this.lastTime = lastTime;
    }
    showHealth(){
        console.log("today " + this.lastTime + "training " + this.name);
    }
}

Const myHealth = new Health("running","23:11");
myHealth.showHealrh();
```

> 위에 클래스 선언 한거의 작동을 보면 그냥 함수랑 다를게 없어보인다.
> 맞다. Class는 사실 함수다.(출처 MDN)
> 함수를 함수 표현식과 함수 선언으로 정의할 수 있듯이 class 문법도 class 표현식과 class 선언 두 가지 방법을 제공합니다.

- class 표현식은 아래와 같다.
```
// unnamed
const Polygon = class{
    constructor(height, width){
        this.height = height;
        this.width = width;
    }
} 

// named
const Polygon = class Polygon{
    constructor(height, width){
        this.height = height;
        this.width = width;
    }
} 
```
- class 선언 방법은 아래와 같다.
class Polygon {
    constructor(height, width){
        this.height = height;
        this.width = width;
    }
}

## 메소드 정의

### 생성자
아래 코드를 보자
```
var Polygon = class {
    constructor(height, width){
        this.width = width;
        this.height = height;
    }
    constructor2(height2, width2){
        this.height = height2 * 2;
        this.widht = width2 * 2;
    }
}
```
> 위 코드는 실행하면 당연히 오류가 뜬다.
> 왜냐면 하나의 클래스에서는 하나의 생성자만 가질수 있기 때문임.

```
class Polygon {
    constructor(height, width) {
        this.height = height;
        this.width = width;
    }
}
 
class Square extends Polygon { // 그러하다 extends가 가능하다.
    constructor(length) {
        // length로 다각형의 넓이와 높이를 정의하기 위해 부모클래스의 생성자를 호출합니다.
        super(length, length);
        // Note: 파생 클래스에서, 'this'를 사용하기 전에는 반드시 super()를
        // 호출하여야 합니다. 그렇지 않을 경우 참조에러가 발생합니다.
        this.name = 'Square';
    }
 
    get area() {
        return this.height * this.width;
    }
 
    set area(value) {
        this.area = value;
    }
}
 
var test = new Square(4);
console.log(test.area);
```


### reference
 - [JUI coreJS blog](http://blog.jui.io/?p=13)
 - [정리 잘된 블로그](http://beomy.tistory.com/15)
 