## Jquery 맛보기

```
"Write less, do more"
```

### 특징
> - HTML/DOM manipulation : DOM조작 짱짱맨!!!!!
> - STYLE maniqulation : .css조작도 짱짱맨!!!!!
> - event handling : event도 짱짱맨!!!!!
> - effect, animation!!! : 이펙트도 짱짱맨!!!! 마법같은 코드!!! 근데 Css로 짜면 더 빠름. 
> - Ajax
> - Utilities : each 이런거...
> - plugins : 막강한 기능

**근데 최근엔 ES가 표준화 되고, Jquery 장점이 점점 줄어듬.**



### get -> act
```
$('div').hide()  // element를 얻고 실행!
$('div').click()
```

### method chaining
```
$('div').addClass.show("slow");  // 
```
위와같이 method를 연결해서 할수 있음.

```
var obj = {
    append : function(name){
        this.name += name;
        return this;
    },
    removeSpecial : function(){
        this.name = this.name.replace(/[^a-z]/ig,"");
        return this;
    },
    getName : function(){
        return this.name;
    }
}

var code = Object.create(obj);
code.name = "^^crong$$";

var cleanName = code.append(")))))))").removeSpecial().getName()
console.log(cleanName);
```


### Ajax
$.ajax({
    method: "GET",
    url: "https://api.github.com/repos/octocat/Hello-World"
}).done(function( msg ) { 
    $show.slideDown("fast", function(){
    $(this).text(msg.languages_url); 
    });
});


### Study Ref
>[jquery, wikipedia](https://en.wikipedia.org/wiki/JQuery#Chaining)


### NEXT
> [lodash](https://lodash.com/) : data parsing 등 유용.
> [underscore](http://underscorejs.org/)
> [underscore 나무위키](https://namu.wiki/w/%EC%96%B8%EB%8D%94%EC%8A%A4%EC%BD%94%EC%96%B4)