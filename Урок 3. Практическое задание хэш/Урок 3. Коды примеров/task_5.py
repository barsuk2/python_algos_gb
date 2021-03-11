"""Хеширование и соль"""

# Модуль uuid применяется для генерации случайного числа
from uuid import uuid4
import hashlib

salt = uuid4().hex  # -> 80740ba2a1584aa7bf96d32bbe774e54
print(type(salt))

passwd = "programmer"
# соль-часть хеша
res = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()  # -> efbb20c297f52672a5211f1358ad8d
# 72907f56e1ff24cd67a6e8b4683a6a18d2
print(res)
