import  base64

file = open('output.txt', 'rb')
encoded_data = file.read()
file.close()

decoded_data = base64.b64decode((encoded_data))

img_file = open('img.png', 'wb')
img_file.write(decoded_data)
img_file.close()