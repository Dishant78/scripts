import itertools

def xor_decrypt_multi_byte(ciphertext_hex, known_prefix="THM{", max_key_len=12):
    ciphertext = bytes.fromhex(ciphertext_hex)
    prefix_bytes = known_prefix.encode()

    # XOR ciphertext with known plaintext to recover part of the key
    recovered_key = [c ^ p for c, p in zip(ciphertext, prefix_bytes)]

    for key_len in range(len(recovered_key), max_key_len + 1):
        # Fix the known part of the key
        partial_key = recovered_key[:]

        unknown_len = key_len - len(partial_key)
        # Brute-force the remaining unknown part of the key
        for extra_key_bytes in itertools.product(range(256), repeat=unknown_len):
            full_key = partial_key + list(extra_key_bytes)

            # Try decoding the whole ciphertext
            decoded_bytes = bytes([b ^ full_key[i % key_len] for i, b in enumerate(ciphertext)])
            try:
                decoded_text = decoded_bytes.decode('utf-8')
                if decoded_text.startswith(known_prefix) and decoded_text.endswith('}'):
                    print(f"[+] Key found (len={key_len}): {bytes(full_key)}")
                    print(f"[+] Decoded text: {decoded_text}")
                    return
            except UnicodeDecodeError:
                continue

    print("[-] No valid flag found. Try increasing `max_key_len`.")

# Run the function
ciphertext_hex = "01071e4f06642e3f5a021037277502217b305f15142121071739032a5c23273b2a040327371c460b"
xor_decrypt_multi_byte(ciphertext_hex)




# output
# [+] Key found (len=5): b'UOS4v'
# [+] Decoded text: THM{p1alntExtAtt4ckcAnr3alLyhUrty0urxOr}

# === Code Execution Successful ===
