from components.functions import encrypt_text, decrypt_text

text_clair = input("Saisissez le texte à encrypter en code caesar: ")
key = 3
texte_chiffre = encrypt_text(text_clair, key)
print("Texte chiffré: ", texte_chiffre)

texte_dechiffre = decrypt_text(texte_chiffre, key)
print("Texte déchiffré: ", texte_dechiffre)
