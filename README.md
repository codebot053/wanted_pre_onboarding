# wanted_pre_onboarding
백엔드 코스 - 5차 선발과제 


- 과제 개요 -

wanted 백엔드 코스 5차 선발과제로 아래 요구사항을 만족하는 API 서버구현을 목적으로 합니다.

📝 요구사항 

  1. 채용공고 등록(POST)

  2. 채용공고 수정(PUT/PATCH)

  3. 채용공고 삭제(DELETE)

  4. 채용공고 목록(GET)
    4-1. 사용자는 채용공고 목록을 확인.
    4-2. 채용공고 검색기능 구현(선택사항)

  5. 채용 상세 페이지(GET)

  6. 사용자는 채용공고에 지원(PATCH)

  7. 기술 요건
    7-1. ORM 사용하여 구현.
    7-2. RDBMS 사용
    
🚧 사용기술

Django(DRF), SQLite

🔨 구현 계획

  API 개요

  |Index|Method|URI|Description|
  |---|---|---|---|
  |1|GET|/post/|채용공고 목록 조회|
  |2|POST|/post/|채용공고 등록(기업)|
  |3|GET|/post/{post_id}/|채용공고 상세 조회|
  |4|PATCH|/post/{post_id}/|채용공고 수정|
  |5|DELETE|/post/{post_id}/|채용공고 삭제|
  |6|GET|/post/?search={}/|채용공고 검색|
  |7|PATCH|/post/{post_id}/apply/{user_id)|채용공고지원|
  
📁 커밋 컨벤션

본 선행 과제의 커밋 컨벤션을 위해 gitmoji 를 도입하여 관리해 보았습니다.

  |Gitmoji|Description|
  |---|---|
  |🎉|프로젝트 시작|
  |✨|기능 추가|
  |⚡|기능 개선/수정|
  |🚧|코드 수정|
  |📝|문서 추가/수정|
  |💡|주석 추가/작성|
  |🐛|버그 수정|
  |✅|테스트 추가/수정|
