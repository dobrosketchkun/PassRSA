from Crypto.Protocol.KDF import PBKDF2
from Crypto.PublicKey import RSA
import getpass

kbits = raw_input('How big exactly? ( must be a multiple of 256 and >= 1024 )\n')
knumber = raw_input('Number of keys\n')


password = getpass.getpass('Enter password part one.\n')
salt = getpass.getpass('Enter password part two.\n')


master_key = PBKDF2(password, salt, count=10000)
#print('master_key',master_key)

def my_rand(n):
    # kluge: use PBKDF2 with count=1 and incrementing salt as deterministic PRNG
    my_rand.counter += 1
    return PBKDF2(master_key, "my_rand:%d" % my_rand.counter, dkLen=n, count=1)

my_rand.counter = 0

for i in range(int(knumber)):
    RSA_key = RSA.generate(int(kbits), randfunc=my_rand)
    public_key = RSA_key.publickey().exportKey("PEM") 
    private_key = RSA_key.exportKey("PEM") 
    print(private_key)
    print(public_key)