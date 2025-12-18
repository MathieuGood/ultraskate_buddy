from __future__ import annotations

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


class AuthService:
    """
    Service responsable de la sécurité des mots de passe.
    Basé sur Argon2 (OWASP recommended).
    """

    _hasher: PasswordHasher = PasswordHasher()

    @classmethod
    def hash_password(cls, password: str) -> str:
        """
        Hash un mot de passe en clair avec Argon2.

        :param password: mot de passe utilisateur
        :return: hash sécurisé
        """
        return cls._hasher.hash(password)

    @classmethod
    def verify_password(cls, password: str, password_hash: str) -> bool:
        """
        Vérifie un mot de passe contre son hash Argon2.

        :param password: mot de passe fourni
        :param password_hash: hash stocké
        :return: True si valide
        """
        try:
            return cls._hasher.verify(password_hash, password)
        except VerifyMismatchError:
            return False
