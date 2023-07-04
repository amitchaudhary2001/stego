from LSBSteg import*
# from des import*
from aes import*
from compress import*
#encoding
steg = LSBSteg(cv2.imread("C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/new_image.png"))
# img_encoded = steg.encode_text("my message to ayush")
f = open("C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/textfile/new_textfile.txt", "r")
# print(f.read())


data=f.read()
compressed_data = compress_text(data)
# decompressed_text = decompress_text(compressed_data)

# encrypted_text = encrypt_DES(encryption_key, compressed_data)
encrypted_text = encrypt_AES(encryption_key, compressed_data)
img_encoded = steg.encode_text(encrypted_text)
cv2.imwrite("C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/new_image.png", img_encoded)





# print(compressed_data)
# print("Decompressed text:")
# print((decompressed_text))
# print(encrypted_text)