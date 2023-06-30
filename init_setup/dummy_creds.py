import hashlib

# Credentials
passphrase = "XXXXXXXXXX"
# OBTAIN NEW PASSPHRASE FOR YOUR ACCOUNT ON https://grjcodes.com/newssnacks
md5_hash = hashlib.md5()
md5_hash.update(passphrase.encode("utf-8"))
key = md5_hash.hexdigest()

# API links
# OBTAIN CONFIGURATION FOR THIS SECTION AFTER MAKING ACCOUNT ON https://grjcodes.com/newssnacks
