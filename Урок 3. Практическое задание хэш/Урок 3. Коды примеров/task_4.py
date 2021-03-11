"""Пример с алгоритмом, доступным на вашем ПК"""

import hashlib

hash_obj = hashlib.new('blake2b')
hash_obj.update(b'blake2b example')

print(hash_obj.hexdigest())  # -> 6c81637f462af6927bc2eafcbb04eb02a9df72371c8f10813ccd9c782cdb9861f4078e9c
# 4441eaf1cc364dddfaad6fe9e63436699d0bc0a653e54e2587e409be
