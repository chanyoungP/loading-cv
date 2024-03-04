# loading-cv
이 레포지토리는 Fly Ai 프로젝트 "AI 도슨트 서비스 : Acent"에서 로딩화면에 들어갈 콘텐츠를 생성하는 기능을 구현한 것입니다.

### 기능 목적
- 사용자 로딩 화면에 들어갈 콘텐츠 생성
- 로딩 콘텐츠로 사용자 경험 향상

### 구현 방법
1. input image에 대해서 OpenCV edge 검출 알고리즘(Canny or Sobel) 수행
2. 검출된 edge image frame 저장
3. 검출 알고리즘의 weight 파라미터 변경 ---- 반복
4. 저장된 frame을 gif 파일로 변환

### 결과
![example](./outputs/human0.gif)

### 실제 화면 결과 

https://github.com/chanyoungP/loading-cv/assets/67907678/58ce861b-f7b8-47a7-81b6-494dbfe30e74

