import environ

# 환경 변수 가져오기
env = environ.Env()

# 현재 파일의 두 단계 위의 디렉토리로 설정
BASE_DIR = environ.Path(__file__) - 2
# 앱들의 파일 경로 설정
APPS_DIR = BASE_DIR.path("apps")
