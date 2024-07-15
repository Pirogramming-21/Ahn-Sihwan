# 피로그래밍 21기 DB 세션 과제

## 🔥 상품에 대한 정보게시판과 판매게시판이 있는 사이트

기본 기능 구현
[캡처 사진 - 기본](Assignments/week3/SellingCommunity_ERD/ERD_1.png)

챌린지 기능 구현
1. '도, 시, 구' 부분이 애매해서 시•도/시•군•구 행정체계 활용함.
    사용자가 시도, 시군구 부분 Entity 참조하여 해당하는 값만 입력하도록 기능 구현.
    시군구는 시도에 종속적이므로 시도와 일대다관계 설정해둠.
2. 댓글 Entity에 '원댓글ID(parent_comment_id)' NOT NULL로 추가하여 대댓글 기능 구현
3. 해시태그 Entity 생성, 커뮤니티게시판과 1대다 관계 설정 / 유저태그 Entity 생성, 유저식별자 FK로 받아와서 커뮤니티게시판과 1대다 관계 설정하여 기능 구현
4. 팔로우 Entity 생성. 유저에게서 1대다 관계로 FK 받아와서 팔로워식별자, 팔로우식별자 생성하여 구현.

[캡처 사진 - 챌린지 완료](Assignments/week3/SellingCommunity_ERD/ERD_2.png)

[ERD cloud 링크](https://www.erdcloud.com/d/p38CRiW5Qpu8Rcmbr)