### Summary
Django MVT<small>(Only Django)</small>로 구현해 본 인스타그램(K-ingStagram)

### Installation
도커(Docker)가 설치된 환경에서 가상 컨테이너로 실행할 수 있습니다.

```shell
$ docker run --name kingstagram -dp 8000:8000 sh007jeong/kingstagram:0.1.2
```

### Create Superuser
슈퍼 유저를 만드려면 터미널에 다음 커맨드를 입력하십시오.
```shell
$ docker exec -it kingstagram /bin/sh

# python manage.py createsuperuser
Username:
Email address(options):
Password:
Password (again):
```
