import hashlib
import bcrypt
from argon2 import PasswordHasher
from argon2.low_level import hash_secret, Type
from Crypto.Hash import MD4
from impacket.ntlm import compute_lmhash

ph = PasswordHasher()


def generate_hashes(text):

    h = MD4.new()
    h.update(text.encode("utf-16le"))
    ntlm_hash = h.hexdigest().upper()

    hashes = {
        "md5": hashlib.md5(text.encode()).hexdigest(),
        "sha1": hashlib.sha1(text.encode()).hexdigest(),
        "sha224": hashlib.sha224(text.encode()).hexdigest(),
        "sha256": hashlib.sha256(text.encode()).hexdigest(),
        "sha384": hashlib.sha384(text.encode()).hexdigest(),
        "sha512": hashlib.sha512(text.encode()).hexdigest(),

        "sha3_224": hashlib.sha3_224(text.encode()).hexdigest(),
        "sha3_256": hashlib.sha3_256(text.encode()).hexdigest(),
        "sha3_384": hashlib.sha3_384(text.encode()).hexdigest(),
        "sha3_512": hashlib.sha3_512(text.encode()).hexdigest(),

        "blake2s": hashlib.blake2s(text.encode()).hexdigest(),
        "blake2b": hashlib.blake2b(text.encode()).hexdigest(),

        "bcrypt": bcrypt.hashpw(
            text.encode(),
            bcrypt.gensalt()
        ).decode(),

        "argon2": ph.hash(text),

        "argon2i": hash_secret(
            secret=text.encode(),
            salt=b"mysalt1234567890",
            time_cost=3,
            memory_cost=65536,
            parallelism=4,
            hash_len=32,
            type=Type.I
        ).decode(),

        "argon2d": hash_secret(
            secret=text.encode(),
            salt=b"mysalt1234567890",
            time_cost=3,
            memory_cost=65536,
            parallelism=4,
            hash_len=32,
            type=Type.D
        ).decode(),

        "argon2id": hash_secret(
            secret=text.encode(),
            salt=b"mysalt1234567890",
            time_cost=3,
            memory_cost=65536,
            parallelism=4,
            hash_len=32,
            type=Type.ID
        ).decode(),

        "scrypt": hashlib.scrypt(
            text.encode(),
            salt=b"mysalt",
            n=16384,
            r=8,
            p=1
        ).hex(),

        "pbkdf2": hashlib.pbkdf2_hmac(
            "sha256",
            text.encode(),
            b"mysalt",
            100000
        ).hex(),

        "ntlm": ntlm_hash,
        "lm": compute_lmhash(text).hex().upper(),
    }

    return hashes