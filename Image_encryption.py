from PIL import Image

def encrypt_image(input_image, key, output_image):
  """Encrypts an image using XOR operation with a key."""
  img = Image.open(input_image)
  pixels = img.load()
  width, height = img.size

  for i in range(width):
    for j in range(height):
      pixel = pixels[i, j]
      # Perform XOR operation with key for each color channel (Red, Green, Blue)
      new_pixel = tuple([p ^ key for p in pixel])
      pixels[i, j] = new_pixel

  img.save(output_image)

def decrypt_image(input_image, key, output_image):
  """Decrypts an image using XOR operation with the same key."""
  img = Image.open(input_image)
  pixels = img.load()
  width, height = img.size

  for i in range(width):
    for j in range(height):
      pixel = pixels[i, j]
      # XOR again with the same key to reverse the encryption
      new_pixel = tuple([p ^ key for p in pixel])
      pixels[i, j] = new_pixel

  img.save(output_image)

# Example usage
if __name__ == "__main__":
  encrypt_image("original.png", 123, "encrypted.png")
  decrypt_image("encrypted.png", 123, "decrypted.png")

  print("Encryption and decryption completed successfully!")
