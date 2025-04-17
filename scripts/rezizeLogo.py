from PIL import Image

img = Image.open("../assets/img/favicons/logo.png")
new_size = (img.width + 80, img.height)  # Add 40px only to the right
new_img = Image.new("RGBA", new_size, (0, 0, 0, 0))  # Transparent background
new_img.paste(img, (0, 0))  # Keep the original image on the left
new_img.save("../assets/img/favicons/logoresize.png")
