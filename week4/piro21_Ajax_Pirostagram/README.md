# 기능 목록

1. 좋아요
2. 댓글 작성
3. 댓글 삭제


## 챌린지 과제

1. ajax를 이용한 검색(미완성일때도 관련 게시글 보이게)
2. 실제 인스타 ui에 맞춰서 구현하기
3. 사진 스토리처럼 넘어가도록 구현
4. 유저 검색기능 추가( 게시글 유저 ) ( 유저모델 생성해야함 )
5. 정렬기능
6. 대댓글

---
## 작업 순서
django-admin startproject config .
django-admin startapp pirostagram
    앱은 하나만 있어도 충분할 것 같았음. -> 일단 확장성 좋게 수정
settings 에서 installed apps, static, templates 정의
    => 기본세팅 commit
pirostagram 앱 models 정의
    필요한 기능: 게시글 좋아요, 댓글, 댓글삭제, (챌린지: 게시글 검색 - 기준이 뭐지?, 유저 검색, 정렬, 대댓글, 사진 여러장 넘어가게)
    1. post
        - post id (PK)
        - user (FK)
        - image
        - text
        - likes
        - created_at
    2. comment
        - text
        - user (FK)
        - post id (FK)
        - created_at
    - User모델은 새로 앱 파기
    apps.user
    
