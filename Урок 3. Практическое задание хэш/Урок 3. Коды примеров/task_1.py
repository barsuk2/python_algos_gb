import hashlib

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

"""
Результат:
{'sha3_384', 'shake_128', 'sha224', 'blake2s', 'sha512', 'shake_256', 
'sha3_512', 'sha256', 'md5', 'sha3_256', 'blake2b', 'sha384', 'sha3_224', 'sha1'}

{'sha3_384', 'shake_128', 'sha224', 'blake2s', 'sha512', 'shake_256',
'sha3_512', 'sha256', 'md5', 'sha3_256', 'blake2b', 'sha384', 'sha3_224', 'sha1'}
"""