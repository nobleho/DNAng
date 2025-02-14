#!/usr/bin/env python3

class dnagen:
    def readfile(fnm):
        f = open(fnm, "r")
        fdata = f.read()
        print(fdata) 
        # for x in f:
        #     print(x)
        f.close()

    def save(fnm, data):
        f = open(fnm, "w")
        f.write(data)
        f.close()

    def decode():
        pass   

    def encode():
        pass

    def gendnagent():
        pass

    def dnagenConvert():
        pass

    def helper():
        print("Helper ...")