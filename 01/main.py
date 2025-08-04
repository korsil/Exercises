from argon2 import PasswordHasher

def main():
    ph = PasswordHasher()
    password = "ducksAreSupreme"
    hash = ph.hash(password)
    print(hash)


if __name__ == "__main__":
    main()
