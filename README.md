# flask-mongodb-webapp
영화 정보 및 리뷰 제공 웹 서비스  


## Stacks
Server : Python Flask MongoDB BeautifulSoup  
Client : HTML CSS Bootstrap JavaScript jQuery Ajax  


네이버 영화 페이지에서  
ver1) 크롤링한 정보를 이용한  
ver2) naver movie api 를 이용한  
영화 정보 및 리뷰 제공 웹 서비스  
영화 정보는 받아온 DB ,  
리뷰는 플랫폼 내에서 user 끼리 CRUD  
+여건이 되면 권한 부여 기능도 찾아보고 추가해준다 

## TODOs
네이버 영화 페이지를 웹 bs4 패키지 이용해 스크래핑한다.  
스크래핑한 결과를 mongoDB 에 저장한다.  
DB에 저장된 데이터를 사용자에게 제공하고, 사용자가 입력한 데이터를 DB에 추가, 수정 및 삭제가 가능하도롤 flask 로 api 설계한다.
기능별 사용자 화면과 UI component 도 제작한다.  
