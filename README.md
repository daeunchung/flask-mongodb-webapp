# flask-mongodb-webapp
영화 정보 및 리뷰 제공 웹 서비스  


## Stacks
Server : Python Flask MongoDB BeautifulSoup  
Client : HTML CSS Bootstrap JavaScript jQuery Ajax  


네이버 영화 페이지에서  
ver1) 크롤링한 영화인 데이터를 이용한  
ver2) naver movie api 를 이용한  
영화인 정보 및 도서 리뷰 제공 웹 서비스  


## TODOs
네이버 영화 페이지를 웹 bs4 패키지 이용해 스크래핑한다.  
스크래핑한 결과를 mongoDB 에 저장한 후에 가져와 화면에 뿌린다.    
도서 리뷰는 플랫폼 내에서 user 끼리 CRUD 가능하도록 flask 로 api 설계한다.  
기능별 사용자 화면과 UI component 도 제작한다.  
+여건이 되면 권한 부여 기능도 찾아보고 추가해준다 


## Database 구조  
Collections(2개)  
  bookreview  
  mystar
