#!/usr/bin/env python3
"""
    This app was created specifically so we can create our own hash
    that the "Oregon Trail" challenge uses to trick the remote site
    into thinking we entered "good" data.
"""
import hashlib

def hasher(hashstring):
    """
        Hashes a string and returns the hexdigest
    """
    h = hashlib.md5()
    h.update(hashstring)
    return h.hexdigest()

def main():
    """
    Gets the variables needed to hash properly
    """

    print("I will need some values from you. These should be integers only!")

    values = []
    try:
        values.append(int(input("Enter Money value: ")))
        values.append(int(input("Enter Distance value: ")))
        values.append(int(input("Enter Current Day value: ")))
        values.append(int(input("Enter Current Month value: ")))
        values.append(int(input("Enter Current Reindeer value: ")))
        values.append(int(input("Enter Runners value: ")))
        values.append(int(input("Enter Ammo value: ")))
        values.append(int(input("Enter Meds value: ")))
        values.append(int(input("Enter Food value: ")))
    except ValueError:
        print("I need integers only!")
        return "go away"
    hashed = hasher(str(sum(values)).encode())
    print("Hashed value is: {}".format(hashed))

if __name__ == '__main__':
    main()
