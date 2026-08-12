import qrcode

def generer_qr_code(lien, nom_fichier):
    qr = qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )
    qr.add_data(lien)
    qr.make(fit=True)
    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )
    img.save(nom_fichier)

#Executez la fonction generer_qr_code avec le lien et le nom du fichier pour obtenir votre QR Code ! 
#lien et nom_fichier doivent etre du texte (string)
