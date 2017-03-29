## box

div등 tag에는 margin등이 있음

- 테두리 두께 border
- 박스와 내용과의 간격을 padding
- 박스와 외부의 간격을 margin이라고함

```
.wrap{
    width : 100px;
    hegiht : 100px;
    border : 1px solid slategray; //선의 형태 색상 두께 결정
    padding : 10px 10px 10px 10px; //위부터 시계방향
    margin : 10px 10px 10px 10px; //위부터 시계방향
    margin-bottom : 10px//아래만.
    margin : 30px //사방을 
}
```
## margin의 특성
인접한 두개의 block element가 서로 다른 margin을 가지면,
- 큰 값을 가진 margin이 공유되어 사용됨.
- 10px + 20px = 20px

인접한 두개의 inline element 의 margin은...?
- 각각의 margin의 합으로 표시된다.
- 10px + 20px = 30px