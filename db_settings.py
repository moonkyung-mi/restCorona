DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",  # 엔진
        "NAME": "etlmysql",  # 데이터베이스 이름
        "USER": "root",  # 사용자
        "PASSWORD": "root",  # 비밀번호
        "HOST": "localhost",  # 호스트
        "PORT": "3306",  # 포트번호
    }
}

# SECRET_KEY
# settings.py에서 복사하고 SECRET_KEY 주석 처리
# DATABASES 주석 처리
SECRET_KEY = "django-insecure-mdsw^*ysl26)%dj0y9e!53qxt##xu@@0b7!*w!k)*ry%7)^79z"


