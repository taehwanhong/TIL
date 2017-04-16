

# NPM
 node package manager라는게 있다.

# 동기 비동기 프로그래밍
 이 주제는 상당히 복잡함
- 빨래 설거지 청소 3가지 일을 해야한다,
 동기적 일처리는, 일단 빨래하고, 그다음에 설거지하고 청소하고 이런 방식이 동기적 일처리임

- 비동기적 일처리는, 외주 주는거구나.
- 끝나는 시점이 중요하지 않다면 비동기적으로 일처리는거임.

이메일 발송 시스템....

동기적으로는 이메일을 받을사람들이 만명정도 된다고 하면, 서버에서 한명한명에게 이메일을 보내는거임. 

비동기적으로 일처리는 이메일을 보내는 별도의 시스템에게 만명에게 보내라고 하고 나는 내 할일 하는거임.
뒤에서 사람들에게 메일 보내는....

# Node js에서의 동기/비동기

file read 를 기준으로,
```
var fs = require('fs');

//sync
console.log(1);
var data = fs.readFileSync('data.txt', {encoding:'utf8'});
console.log(data);


//async
console.log(2); //------1번실행
fs.readFile('data.txt',{encoding:'utf8'}, function (err, dt) {
    console.log(3); // ---------3번 실행 // callback!
    console.log(dt);
});
console.log(4); // ------2번실행
```

## express
node에서 서버 만들려고 하면 귀찮은 일을 해야함....

```
const http = require('http');
const o = require('os');
const express = require('express');
const app = express()

console.log(o.platform());

app.get('/', function(req, res) {
    res.send('Hello World!')
})

app.listen(3000, function() {
    console.log('Example app listening on port 3000!')
})
```

이런걸 대체하려면 express package를 사용하면 좋음.

설치는 




# ref and using package
 - [JS 함수지향 프로그래밍](https://opentutorials.org/module/532/6495)
 - [JS 객체지향 프로그래밍](https://opentutorials.org/module/532/6584)
 - [JS 웹앱 개발](https://opentutorials.org/module/1514)
 - [node JS 개발](https://opentutorials.org/course/2136/11884)
 - [underscore](http://underscorejs.org)