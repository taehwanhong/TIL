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


### reference
 - [JUI coreJS blog](http://blog.jui.io/?p=13)
