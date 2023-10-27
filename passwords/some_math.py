# oops i forgot to do this in the other python file and didn't want to run again 

def doit(time, hashes, passwords):
    print("seconds per hash:", time/hashes)
    print("seconds per password cracked:", time/passwords)
    print("passwords per hash:",  passwords/hashes)
    print("-----------------")


#     Time per hash computed: [seconds per hash]
# Time per password cracked: [seconds per password]
# Passwords cracked per number of hashes computed: [passwords per hash]

print("Phase1")
doit(37.604146003723145, 267516, 2734)

print("Phase 2")
doit(759.8391492366791, 1246892076, 51)

print("Phase 3")
doit(419.85552406311035, 731388744, 2734)