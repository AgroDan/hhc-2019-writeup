#!/usr/bin/env python3

"""
    Making sense of things
"""
# From: 1575658800 (Unix time)
# To: 1575666000 (Unix time)
import requests
import os
from Crypto.Cipher import DES
times = [x for x in range(1575658800, 1575666000)]
#times = [x for x in range(1575658821, 1575666000)]


def checker(check_file):
    '''
    Checks if file is recognizable yet
    '''
    if "PDF document" in os.popen(f"file ./{check_file}").read():
        return True
    else:
        return False


def msvcrt_rand(seed):
   def rand():
      nonlocal seed
      seed = (214013*seed + 2531011) & 0x7fffffff
      return seed >> 16
   return rand

def gen_key(seed):
    """
    Generates a key based on the provided seed.
    """
    ms = msvcrt_rand(seed)
    key_ms = []
    for i in range(8):
        key_ms.append('%02x' % ms())
    new_key = []
    for tick in key_ms:
        new_key.append(tick[-2:])

    return ''.join(new_key)

def conv_key(key):
    """
        This function converts a key to bytes
    """
    lkey = [key[i:i+2] for i in range(0, len(key), 2)]
    # Now we have a list of 2 digits
    new_lkey = [int(i, 16) for i in lkey]
    return bytes(new_lkey)

def decrypt_file(enc_file, raw_key):
    """
    Actually decrypts the file
    """
    with open(enc_file, 'rb') as f:
        enc = f.read()

    decryptor = DES.new(raw_key, DES.MODE_CBC, '\x00\x00\x00\x00\x00\x00\x00\x00')
    return decryptor.decrypt(enc)

def write_file(data):
    """
    Writes the file
    """
    with open("./result.pdf", "wb") as f:
        f.write(data)

def rem_file():
    os.remove("./result.pdf")

#myseed = 1576608936
#
#print(f"Seed value: {myseed}")
#
#key = gen_key(myseed)
#print(f"Key: {key}")
#
#
#print(f"Now convert key back to bytes")
#this_key = conv_key(key)
##print(f"Resulting key: {this_key}")

print("Grinding through...")
for i in times:
    print(f"\r{i}")
    key = gen_key(i)
    bkey = conv_key(key)
    data = decrypt_file("./check.pdf.enc", bkey)
    write_file(data)
    if checker("./result.pdf"):
        print("\nWe got one!")
        print(f"This key: {key}")
        print("Obtaining ID to better decrypt...")
        req = requests.post('https://elfscrow.elfu.org/api/store', data=key)
        print(f"ID: {req.text}")
        break
    else:
        rem_file()
