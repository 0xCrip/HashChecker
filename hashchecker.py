import hashlib
import sys
filepath = "hash.txt"
i = 0
counter = 0

# input_hash = input("Enter the hash you would like to check: \n")
input_hash = sys.argv[1]

with open(filepath, 'rb') as my_file:
    for line in my_file:
        hash_pass = hashlib.sha256(line.rstrip()).hexdigest()
        if hash_pass == input_hash:
            print('------------------------------\n' + str(i))
            print("Password: " + str(line))
            print(hash_pass)
            counter += 1
        i += 1
    if counter > 0:
        print("\nAble to return " + str(counter) + " entries.\n")