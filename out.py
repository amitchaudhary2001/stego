from LSBSteg import*
# from des import*
from aes import*
from compress import*
#decoding
im = cv2.imread("C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/new_image.png")
steg = LSBSteg(im)

content = steg.decode_text()

# content = decrypt_DES(encryption_key, content)
content = decrypt_AES(encryption_key, content)
decompressed_text = decompress_text(content)
file_path = 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/textfile/new_textfile.txt'  # Specify the file path where you want to save the file
print(decompressed_text)
with open(file_path, 'w', encoding="utf-8") as file:
    file.write(decompressed_text)

