'''
passwords.py

Kyra Helmbold

This program computes passwords that are hashed in 3 different ways.

Run as you would a normal python file. 


Notes & Credits: 
- Starter Code for computing hashes from Jeff Ondich's conversions.py
- Discussed assignment with Kiri Salij.
- Help on the time command and writing to a file from Geeks for Geeks. 

'''
import hashlib
import binascii
import time

words = [line.strip().lower() for line in open('words.txt')]

# gets all the passwords for phase1. 
def phase1():
    start_time = time.time()
    passwords_cracked = 0
    hashes_computed = 0
    # this chunk takes 0.2s
    word_hashes = {}
    for word in words:
        encoded_word = word.encode('utf-8')
        hasher = hashlib.sha256(encoded_word)
        digest = hasher.digest()
        digest_hex = binascii.hexlify(digest)
        digest_hex_string = digest_hex.decode('utf-8')
        hashes_computed += 1

        word_hashes[word] = digest_hex_string

    
    # make a list of usernames and passwords
    uname_pwd = []

    for line in open("uname_and_hash1.txt", 'r'):
        line = line.split(':')
        uname = line[0]
        hash = line[1]
        for word in word_hashes:
            if word_hashes[word] == hash:
                uname_pwd.append(uname + ':' + word + '\n')
                passwords_cracked += 1

    file = open('cracked1.txt', 'w')
    file.writelines(uname_pwd)
    file.close()

    end_time = time.time()

    print("Phase 1:")
    print("Passwords Cracked:", passwords_cracked) # 2734
    print("Hashes computed:", hashes_computed) # 267516
    print("Time to complete:", end_time - start_time) # 37.604146003723145
    print('\n')

# gets some of the passwords for phase2. 
def phase2():
    start_time = time.time()
    hashes_computed = 0
    passwords_cracked = 0
    uname_hash = {}
    set_hashes = set()

    for line in open("uname_and_hash2.txt", 'r'):
        line = line.split(':')
        uname = line[0]
        hash = line[1]
        uname_hash[uname] = hash

        set_hashes.add(hash)


    # make a list of usernames and passwords
    uname_pwd = []
    # for every combo of 2 words...
    for word1 in words:
        for word2 in words:

            # compute hash
            word = word1 + word2
            encoded_word = (word).encode('utf-8')
            hasher = hashlib.sha256(encoded_word)
            digest = hasher.digest()
            digest_hex = binascii.hexlify(digest)
            digest_hex_string = digest_hex.decode('utf-8')
            hashes_computed += 1

            # see if hash is a password
            if digest_hex_string in set_hashes:
                for uname in uname_hash:
                    if uname_hash[uname] == digest_hex_string:
                        uname_pwd.append(uname + ':' + word + '\n')
                        passwords_cracked += 1
                    
        if passwords_cracked == 51:
            break

    file = open('cracked2.txt', 'w')
    file.writelines(uname_pwd)
    file.close()

    end_time = time.time()

    print("Phase 2:")
    print("Passwords Cracked:", passwords_cracked) # 51
    print("Hashes computed:", hashes_computed) # 1246892076
    print("Time to complete:", end_time - start_time) # 759.8391492366791
    print('\n')


# gets all the passwords for phase3. 
def phase3():
    start_time = time.time()
    hashes_computed = 0
    passwords_cracked = 0
    uname_pwd = []
    for line in open("uname_and_hash3.txt", 'r'):
        line = line.split(':')
        uname = line[0]
        hash = line[1]
        hash = hash.split('$')
        salt = hash[2]
        hash = hash[3]

        # for every word:
        for word in words:
            word_and_salt = salt + word
            encoded_word = (word_and_salt).encode('utf-8')
            hasher = hashlib.sha256(encoded_word)
            digest = hasher.digest()
            digest_hex = binascii.hexlify(digest)
            digest_hex_string = digest_hex.decode('utf-8')
            hashes_computed += 1
            if digest_hex_string == hash:
                uname_pwd.append(uname + ':' + word + '\n')
                passwords_cracked += 1

    file = open('cracked3.txt', 'w')
    file.writelines(uname_pwd)
    file.close()

    end_time = time.time()

    print("Phase 3:")
    print("Passwords Cracked:", passwords_cracked) # 2734
    print("Hashes computed:", hashes_computed) # 731388744
    print("Time to complete:", end_time - start_time) # 419.85552406311035

# phase1()

phase2()

# phase3()