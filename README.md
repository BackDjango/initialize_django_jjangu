# initialize_django_jjangu

## 📃 프로젝트 개요
 Django REST Framework의 숙달을 위함.

## 🪛 개발 환경
- python == 3.12.2
- django == 5.0.3
- djangorestframework == 3.15.1
- django-environ == 0.11.2

## 🧑🏼‍💻 요구 사항 및 목표
- [ ] 자기한테 맞는 Django 초기 설정
  - [✔️] `config/env.py` 수정
  - [✔️] `config/asgi.py` & `config/wsgi.py` 수정
    - [✔️] `manage.py` 의 DJANGO_SETTINGS_MODULE 환경 변수 조정
  - [ ] `config/urls.py` 수정
  - [ ] `config/settings/celery.py` 수정
  - [ ] `config/settings/cors.py` 수정
  - [ ] `config/settings/sentry.py` 수정
  - [ ] `config/settings/sessions.py` 수정
  - [ ] `config/django/base.py` 수정
    - [✔️] SECRET_KEY 생성 및 분리
    - [✔️] DEBUG 및 ALLOWED_HOST 설정
    - [✔️] Application Definition 설정
    - [✔️] sqlite3를 이용한 DB setting
  - [ ] `config/django/local.py` 수정
  - [ ] `config/django/production.py` 수정
  - [ ] `config/django/test.py` 수정
  - [ ] Mypy 라이브러리 설치
  - [ ] pre-commit 라이브러리 설치
  - [ ] .env 파일 생성
  - [ ] gunicorn - Procfile 생성
  - [ ] pyproject.toml
  - [ ] Swagger `drf-yasg` 세팅
  - [ ] 최종 makemigrations 수행

- [ ] Auth (app) 기능 구현

- [ ] Board 모델 생성 및 비즈니스 로직 구현

- [ ] Pagination

- [ ] Exception

- [ ] Reponse

- [ ] Swagger 라이브러리 적용

- [ ] 맞는 View 생성

## 📂 기본 파일 구조
config
├── __init__.py
├── django
│   ├── __init__.py
│   ├── base.py
│   ├── local.py
│   ├── production.py
│   └── test.py
├── settings
│   ├── __init__.py
│   ├── celery.py
│   ├── cors.py
│   ├── sentry.py
│   └── sessions.py
├── urls.py
├── env.py
└── wsgi.py
├── asgi.py
...