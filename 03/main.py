from ecdsa import SigningKey

def sign_something(signing_key, something):
    return signing_key.sign(something)

def verify_signature(signing_key, signature, something):
    return signing_key.verifying_key.verify(signature, something)


def main():
    signing_key = SigningKey.generate()
    
    contract = b"We all agree that ducks are superior."
    print("Contract:", contract)

    signature = sign_something(signing_key, contract)
    print("Signature:", signature)

    print("Is signature valid: ", verify_signature(signing_key, signature, contract))



if __name__ == "__main__":
    main()
