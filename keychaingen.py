#generate keychain file 
import binascii 
import nacl.utils
import nacl.secret
import nacl.utils


from nacl.public import PrivateKey, Box

prkey1 = PrivateKey.generate()

prkey2 = PrivateKey.generate()

skey1Hex = prkey1.encode(encoder=nacl.encoding.HexEncoder)
print ("Bobs secret key 1 is: %s" % (skey1Hex))

skey2Hex = prkey2.encode(encoder=nacl.encoding.HexEncoder)
print ("Bobs secret key 2 is: %s" % (skey2Hex))

plkey1 = prkey1.public_key

plkey2 = prkey2.public_key

pkey1Hex = plkey1.encode(encoder=nacl.encoding.HexEncoder)
print ("Bobs public key 1 is: %s" % (pkey1Hex))

pkey2Hex = plkey2.encode(encoder=nacl.encoding.HexEncoder)
print ("Bobs public key 2 is: %s" % (pkey2Hex))
