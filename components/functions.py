def caesar_code(text, key, encrypt=True):
    result = []
    for char in text:
        if char.isalpha():
            # Gestion des majuscules et des minuscules
            offset = 65 if char.isupper() else 97
            # Calcul du nouveau caractère avec le décalage
            shift = key if encrypt else -key
            result.append(chr((ord(char) - offset + shift) % 26 + offset))
        else:
            # Si ce n'est pas une lettre, on laisse le caractère tel quel
            result.append(char)
    return ''.join(result)

def encrypt_text(text, key):
    return caesar_code(text, key, encrypt=True)

def decrypt_text(text, key):
    return caesar_code(text, key, encrypt=False)

# # Exemple d'utilisation
# text_clair = "Hello, World!"
# key = 3
# texte_chiffre = encrypt_text(text_clair, key)
# print("Texte chiffré:", texte_chiffre)
# texte_dechiffre = decrypt_text(texte_chiffre, key)
# print("Texte déchiffré:", texte_dechiffre)
