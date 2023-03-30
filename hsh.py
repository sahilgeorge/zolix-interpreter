import hashlib
##sha256 encoding
def sha256(console):
    hashed = hashlib.sha256(console.encode('utf-8')).hexdigest()
    return(hashed)

##md5 encoding
def md5(console):
    hashed = hashlib.md5(console.encode('utf-8')).hexdigest()
    return(hashed)

##sha1 encoding
def sha1(console):
    hashed = hashlib.sha1(console.encode('utf-8')).hexdigest()
    return(hashed)

##md4 encoding
def md4(console):
    hashed = hashlib.md4(console.encode('utf-8')).hexdigest()
    return(hashed)

##sha512 encoding
def sha512(console):
    hashed = hashlib.sha512(console.encode('utf-8')).hexdigest()
    return(hashed)

##sha384 encoding
def sha384(console):
    hashed = hashlib.sha384(console.encode('utf-8')).hexdigest()
    return(hashed)