## RNN레이어
### 언제쓰는가
- Sqeuence 학습
  - 자료간 순서개념이 있는경우
  - 데이터의 연관성이 있는경우
- Input Vector to Sequence
  - 사진주면 설명하는 글쓰기 인공지능
- Sequence to Vector
  - 악플감지 인공지능
- Sequence to Sequence
  - 인공지능 번역

## simple RNN
### 문제점
1. Diminishing Gradient
  - 레이어를 지날수록 상위레이어의 비중이 줄어들어 해결력이 줄어들었음
  - 처음 본 단어가 다른단어를 거칠수록 희미해짐 (결과에 영향이 줄어 예측이 불안정해짐)
### 해결방법
**LSTM** (Long Short Trem Memory/장기기억) 레이어
  - 잃어버릴것과 기억할것을 결정해서 연산
  - 장기기억과 출력값 두개를 다음 레이어에 넘겨줌
![image](https://cdn.discordapp.com/attachments/1111962169567883316/1113690912418172998/image.png)