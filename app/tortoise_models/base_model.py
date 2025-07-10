from tortoise import fields


class BaseModel:
    id = fields.BigIntField(primary_key=True)
    created_at = fields.DatetimeField(auto_now_add=True)


# MYSQL: primary key를 정할 때 주의할 점
# MYSQL version 8 이상부터 라면
# innodb가 defalut engine

# innodb의 특징 중 하나 -> clusting index
# primary key를 기준으로
# primary key 값이 비슷한 row들끼리 disk에서도 실제로 모여있음

# HDD
# 랜덤 IO가 느리고 ,순차 IO가 빠름

# 그냥 int가 아니라, 비즈니스적 의미가 있고
# 계속 증가하는 어떤 값으로 설정하면
# 굉장히 빠르게 읽을 수 있음
