# mypasswordpackage/hasher.py

import nacl.pwhash
import nacl.exceptions

def hash_password(password: str) -> bytes:
    """Hashes the given password using PyNaCl's Argon2i."""
    password_bytes = password.encode('utf-8')
    hashed_password = nacl.pwhash.str(password_bytes)
    return hashed_password

def verify_password(stored_hash: bytes, entered_password: str) -> bool:
    """Verifies if the entered password matches the stored hash."""
    entered_password_bytes = entered_password.encode('utf-8')
    try:
        return nacl.pwhash.verify(stored_hash, entered_password_bytes)
    except nacl.exceptions.InvalidkeyError:
        return False
