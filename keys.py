import rsa


def gen_keys():
    #private_key_pass = "631252726692175"
    #can be used later for private key encryption :)
    public_key, private_key = rsa.newkeys(1024)

    with open("public.pem", "wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    with open("private.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))


