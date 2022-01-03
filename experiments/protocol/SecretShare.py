import os

#This function takes a secret, a modulos P, and bytes size.
#randomly generates two secret shares and computes
#the third secret share

def genSecretShares(secret, P, byteSize):
    print(byteSize)
    share1 = os.urandom(byteSize).hex()
    share2 = os.urandom(byteSize).hex()
    share3 = pow(secret - (int(share1,16) + int(share2,16)),1,P)
    shares = [share1, share2, hex(share3)[2:]]
    return shares

