import base64
image = open('img.png', 'rb')
image_read = image.read()
image_encode = base64.b64encode(image_read)

write_file = open('output.txt', 'wb')
write_file.write(image_encode)
write_file.close()