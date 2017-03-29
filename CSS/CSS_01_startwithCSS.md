## CSS

### Basic Usage
아래와 같은 형태로 생겨먹음.
```
선택자 {속성 : 값;}
span { color : red; }
```

### style을 HTML에 적용하는 3가지 방법
> * inline
> * internal
> * external
> * 우선순위 inline,> internal,> external 임
1. inline
```
<span style="color:red;">
```

2. internal
```
<style>
span{color : red;}
</style>
```

2. external
* main.css
```
span{color :red;}
```

* main.html
```
<link rel="stylesheet" type="text/css" href="main.css" />
```

### 예제를 보자
main.html
```
<head>
    <link rel="stylesheet" type="text/css" href="main.css" />
    <style>
        div > p {  //div 밑의 p를 의미한다.
            font-size : 20px;
        }
    </style>
</head>
<body>
    <div>
        <p style="color:blue;">
        texttexttexttexttexttexttexttexttexttexttexttexttext
        </p>
    </div>
</body>
```


### 망할. 상속이 있다.

- 아래 코드를 보라.
```
<html>

<head>
    <style>
        body>div {
            color: green;
            font-size: 30px;
            border: 2px solid slategray;
            padding: 30px;
        }
    </style>
</head>

<body>
    <div>
        <ul>
            <li>
                <span> dummy </span>
                <div>
                    <p> testtesttest </p>
                </div>
            </li>
            <li>
                <div>
                </div>
            </li>
        </ul>
    </div>
</body>

</html>
```

### Cascading (적용 우선 순위)
> - 동등한 레벨이라면 나중에 선언된게 우선
> - 같은 대상이라도 구체적으로 선언한게 우선 li 보다는 div > li가 우선
> - class와 id가 같은 노드를 가르치면, id값이 우선
> - id > class > element 임.

> 궁금하면, css specificity(명시도)를 찾아보시라!
> * ref : [MDN](https://developer.mozilla.org/ko/docs/Web/CSS/Specificity)


### Selector
3가지 기본 선택자.
1. TAG선택
```
span{
    color : red;
}
```
SPAN tag에 모두 적용된당.

2. ID선택
```
#idname {
    color : red;
}
```
JS에서는 맨 위에꺼부터 선택됨. 근데 CSS에서는 id모두 찾아옴.
근데 HTML에 id는 하나만쓰는게 좋음

- 그리고 id선택은 element랑 같이 쓸수 있다.
```
div.idname {
    color : red;
}
```

3. Class선택
```
.classname{
    color : red;
}
```

4. 그리고 복합적으로(그룹으로) 선택도 가능하다.
h1, div, li {
    color : red;
}

5. 게다가, 하위요소를 지정도 가능하다.

- 자식요소 선택은 > 를 사용.
```
div > li {
    color : red;
}
```
요런거라든가
- 하위 요소 선택은 공백을 사용
```
#idname li {
    color : red;
}
```
- nth child선택도 가능.
```
#idname > li:nth-child(2){
    color :red;
}
```

### font&color 
```
.myspan {
    color : rgba(255,0,0,0,5); //red
    color : #ff000; //red
    color : #f00; //red
    font-size : 16px;
    font-size : 1em;//상대적인 크기 기본값 16px임
    background-color : red; //element의 색을 바꿈
    font-family : "monospace";//폰트!
}
```
다만 em의 기본값은 상속을 받음. 부모 node가 32px로 결정되면 이것을 기본 값으로 사용함.

폰트 패미리가 여러개로 쓰는건 브라우저가 지원하지 않을경우 다음꺼를 사용하도록 하기 위한것임.

