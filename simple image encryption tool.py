from PIL import Image
import numpy as np
import random
def encrypt_image(input_image, key):
    
    #Encrypts the input image using a given key.
    # Open the input image
    img = Image.open(input_image)
    
    # Convert the image to a NumPy array
    img_arr = np.array(img)
    
    # Encrypt the image by swapping pixel values
    height, width, channels = img_arr.shape
    for i in range(height):
        for j in range(width):
             # Swap the pixel values based on the key
            img_arr[i, j, 0] = img_arr[i, j, 0] ^ key[0]
            img_arr[i, j, 1] = img_arr[i, j, 1] ^ key[1]
            img_arr[i, j, 2] = img_arr[i, j, 2] ^ key[2]
    
    # Convert the encrypted array back to an image and save it
    encrypted_img = Image.fromarray(img_arr.astype(np.uint8))
    encrypted_img.save("encrypted_image.jpg")
    print("Image encrypted successfully!")
    Image._show(encrypted_img)


def decrypt_image(encrypted_image, key):
    
    #Decrypts the encrypted image using the same key.
    
    # Open the encrypted image
    img = Image.open(encrypted_image)
    
    # Convert the image to a NumPy array
    img_arr = np.array(img)
    
    # Decrypt the image by swapping pixel values again
    height, width, channels = img_arr.shape
    for i in range(height):
        for j in range(width):
            # Swap the pixel values based on the key
            img_arr[i, j, 0] = img_arr[i, j, 0] ^ key[0]
            img_arr[i, j, 1] = img_arr[i, j, 1] ^ key[1]
            img_arr[i, j, 2] = img_arr[i, j, 2] ^ key[2]
    
    # Convert the decrypted array back to an image and save it
    decrypted_img = Image.fromarray(img_arr.astype(np.uint8))
    decrypted_img.save("decrypted_image.jpg")

    print("Image decrypted successfully!")
    Image._show(decrypted_img)


input_image = input("input_image.jpg:")
key = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
encrypt_image(input_image, key)
decrypt_image("encrypted_image.jpg", key)
