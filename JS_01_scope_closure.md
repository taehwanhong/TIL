## Scope 와 Closure

### Variable Scope
 > - 변수범위. 현재 자신의 위치에서 볼 수 있는 변수를 결정하는 방법.
 > - 자신의 Scope안에 있다면 접근 가능.
 > - local scope / global scope 둘중 하나를 가짐
 > - function, with, catch구문이 실행될때, 객체가 생성될때 scope가 생성됨
 > - {}가 있다고 해서 scope가 생성되는것은 아님
 
 아래 코드를 봅시다.(속깊은 참고)
 ```
 for(var i = 0; i<10; i++){
     var total = (total||0) + i;
     var last = i;
     if(total > 16){
         break;
     }
 }
 console.log(total + "," + last);
 ```

for 문 {}안에 있는 total, last에 대하여,
console.log에서 접근이 가능.

이는, for문의 {}가 scope를 생성하지 않는다는것을 의미함.

다시 아래 코드를 보자.(속깊은 참고)
```
function th(){
    var aaa = "hey";
}
console.log(aaa);
```

어떤 결과가 나올까?
이건 100% undefined나온다 이거야.
특히, function은 {} 안에 있는 모든 내용이 local scope에 포함됨.

-------
* 근데 여기서 내가 살짝 궁금했던건, 함수에서 return을 쌔려주면, 그 리터값은 접근 가능한게 아닌가? 했는데 그거 아닌가봄. 아래 코드를 보자. 이건 내가 쓴거다.

```
function doubleSnsd(){
var snsd = "snsd";
    console.log(snsd);
    snsd = snsd + "snsd";
    console.log(snsd);
    return snsd; //snsdsnsd
}
```
여기서 return을 snsd를 하기때문에 snsdsnsd가 나옴.
근데 이건 그냥 리턴일 뿐 이게 어디 변수에 담기지는 않아서 쓸수가 없다.(젠장!)

이런때는, 다시 아래 코드를 보자.
```
var DS = function(){
    var snsd = "snsd";
    console.log(snsd);
    snsd = snsd + "snsd";
    console.log(snsd);
    return snsd;
}
```

사실 이렇게 하면 DS()로 function인 DS를 실행하면,
snsdsnsd를 리턴한다. 여전히. 쓸수가 없다.

그래서 이런짓을 해봤다.
```
DS.snsd //undefined
```
없단다.

전역변수를 새로 선언해서 담아보기로했다.
```
var DS = function(){
    var snsd = "snsd";
    console.log(snsd);
    snsd = snsd + "snsd";
    console.log(snsd);
    return snsd;
}

var aaa = DS(); //snsdsnsd
```

이제 aaa라는 변수에 드디어 snsdsnsd가 담겼다.

근데 사실 이건 클로져는 아님.

---------

try와 with에서의 scope는 function이랑 조금 다르다.

다시 아래 코드를 보자.(속깊은 참고)
```
try{
    throw new exception("fake");
}catch(err){
    var test = "see me";
    console.log(err instanceof ReferenceError===true);
}
console.log(test === "see me");
console.log(typeof(err) === 'undefined');
```

/////////////////////////////////////
to be continued



#### Local scope(지역변수)

아래 코드를 보자.
```
var name = "taehwan";

function tellMe(){
    var name = "david";
    console.log(name); //david
}
console.log(name);//taehwan
```


### Study Reference
 > [속깊은 자바스크립트](http://unikys.tistory.com/295)    
 > [chanlee's blog](http://chanlee.github.io/2013/12/10/understand-javascript-closure/)