## 부동산 어플리케이션

DJANGO와 REACT를 사용한 풀스택 개발 / postman으로 test  
 어드민 아이디: shin92@admin.com  

#### 파이썬 가상머신
이썬에서는 한 라이브러리에 대해 하나의 버전만 설치가 가능합니다.  
여러개의 프로젝트를 진행하게 되면 이는 문제가 됩니다. 작업을 바꿀때마다 다른 버전의 라이브러리를 설치해야합니다.  
이를 방지하기 위한 격리된 독립적인 가상환경을 제공합니다.  
일반적으로 프로젝트마다 다른 하나의 가상환경을 생성한 후 작업을 시작하게 됩니다.  
가상환경의 대표적인 모듈은 3가지가 있습니다.  
venv : Python 3.3 버전 이후 부터 기본모듈에 포함됨  
virtualenv : Python 2 버전부터 사용해오던 가상환경 라이브러리, Python 3에서도 사용가능  
conda : Anaconda Python을 설치했을 시 사용할 수있는 모듈  
pyenv : pyenv의 경우 Python Version Manger임과 동시에 가상환경 기능을 플러그인 형태로 제공  


## Backend

-accounts = 회원에 대한 모델  
-realtors = 부동산 중개업자에 대한 모델
-listings = 부동산 매물에 대한 모델


## 패키지

*djangorestframework = REST API를 위한 장고 패키지  
*django-cors-headers 장고와 리액트 소통을 위한 패키지  
*djangorestframework-simplejwt -JSON을 위한 패키지  
*pillow - 이미지 업로드를 위한 패키지  
*psycopg2 , psycopg2-binary -post된 데이터베이스를 다루기위한 패키지?  
