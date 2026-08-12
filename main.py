from generateur_qr_code import generer_qr_code

def main():
    lien = input("Pour quel lien voulez-vous générer un QR Code ? ")
    nom_fichier = input("Sous quel nom voulez-vous sauvegarder l'image du QR Code ? ")

    generer_qr_code(lien, nom_fichier)

    print(f"QR code créé avec comme nom de fichier : {nom_fichier}")


if __name__ == "__main__":
    main()
