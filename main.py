import os

import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import PIL


# Inserts texts in the image with specific details
def image_process(data, image_file_name, font_size, name_x, name_y, id_x, id_y, id_font_color='yellow',
                  name_font_color='red', line_space=150):
    img = PIL.Image.open(image_file_name)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Fonts/Arial.ttf', font_size)
    for x, d in data:
        draw.text((name_x, name_y), 'Name:' + d['Name'], fill=name_font_color, font=font)
        name_y += line_space
        draw.text((id_x, id_y), 'ID:' + d['Unique Id'], fill=id_font_color, font=font)
        id_y += line_space
    img.save('Processed_Images/uniqueID.jpg')
    image_file_name = 'Processed_Images/uniqueID.jpg'
    img = PIL.Image.open(image_file_name)
    img.show()


# Inserts texts in the image
def image_process(data, image_file_name, font_size=50, id_font_color='yellow', name_font_color='red'):
    img = PIL.Image.open(image_file_name)
    id_x, id_y = img.size
    id_x /= 2
    id_y = 30
    name_x = 30;
    name_y = 30;
    print()
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Fonts/Arial.ttf', font_size)
    for x, d in data:
        draw.text((name_x, name_y), 'Name:' + d['Name'], fill=name_font_color, font=font)
        name_y += 150
        draw.text((id_x, id_y), 'ID:' + d['Unique Id'], fill=id_font_color, font=font)
        id_y += 150
    img.save('Processed_Images/uniqueID.png')
    image_file_name = 'Processed_Images/uniqueID.png'
    img = PIL.Image.open(image_file_name)
    img.show()


# return a list all images from a folder
def get_all_images_from(folder_name):
    image_list = []
    valid_images = ["jpg", "png"]
    for filename in os.listdir(str + '/'):
        ext = filename.split('.')[-1]
        if ext.lower() not in valid_images:
            continue
        image_list.append(filename)
    return image_list


# Main function
def main():
    images = get_all_images_from('Images')
    print("Image Files:")
    print(images)
    xlsx_name = "MidNightHackathon212.1.xlsx"
    # data = pd.read_excel(xlsx_name)
    # print(data)
    # # for x, y in data.iterrows():
    # #     print(y['Name'], '   ', y['Unique Id'])
    # # print(image_list)
    # image_file_name = 'Images/white.jpg'
    # image_process(data.iterrows(), image_file_name)


# def import_images_with_heading_numbers
if __name__ == "__main__":
    main()
