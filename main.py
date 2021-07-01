import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import PIL


# Inserts texts in the image with specific details
def image_process(data, image_file_name, font_name, font_size, name_x, name_y, id_x, id_y, save_with_name, id_font_color='yellow',
                  name_font_color='red', line_space=150):
    img = PIL.Image.open(image_file_name)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Fonts/' + font_name, font_size)
    for x, d in data:
        draw.text((name_x, name_y), 'Name:' + d['Name'], fill=name_font_color, font=font)
        name_y += line_space
        draw.text((id_x, id_y), 'ID:' + d['Unique Id'], fill=id_font_color, font=font)
        id_y += line_space
    img.save('Processed_Images/' + save_with_name)
    image_file_name = 'Processed_Images/' + save_with_name
    img = PIL.Image.open(image_file_name)
    img.show()


# Inserts texts in the image
def image_process_no_specification(data, image_file_name, font_name="ten.ttf", font_size=50, id_font_color='black',
                                   name_font_color='red', save_with_name="uniqueID.jpg"):
    img = PIL.Image.open(image_file_name)
    id_x, id_y = img.size
    id_x /= 2
    id_y = 30
    name_x = 30;
    name_y = 30;
    print()
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Fonts/' + font_name, font_size)
    for x, d in data:
        draw.text((name_x, name_y), 'Name:' + d['Name'], fill=name_font_color, font=font)
        name_y += 150
        draw.text((id_x, id_y), 'ID:' + d['Unique Id'], fill=id_font_color, font=font)
        id_y += 150
    img.save('Processed_Images/'+save_with_name)
    image_file_name = 'Processed_Images/'+save_with_name
    img = PIL.Image.open(image_file_name)
    img.show()


# return a list all images from a folder
def get_all_images_from(folder_name):
    image_list = []
    valid_images = ["jpg", "png"]
    for filename in os.listdir(folder_name + '/'):
        ext = filename.split('.')[-1]
        if ext.lower() not in valid_images:
            continue
        image_list.append(filename)
    return image_list


def get_all_xlsx_from(folder_name):
    xlsx_files = []
    valid_images = ["xlsx"]
    for filename in os.listdir(folder_name + '/'):
        ext = filename.split('.')[-1]
        if ext.lower() not in valid_images:
            continue
        xlsx_files.append(filename)

    return xlsx_files


# Main function
def main():
    image_folder_name = "Images/"
    xlsx_folder_name = "XLSX Files/"
    xlsx_list = get_all_xlsx_from(xlsx_folder_name)
    images = get_all_images_from(image_folder_name)
    image_empty = False
    xlsx_empty = False
    image_file_name = ""
    xlsx_file_name = ""
    if len(images) == 0:
        image_empty = True
    else:
        image_file_name = image_folder_name + images[0]
    if len(xlsx_list) == 0:
        xlsx_empty = True
    else:
        xlsx_file_name = xlsx_folder_name + xlsx_list[0]
    x = 99
    while True:
        if image_empty:
            print("Images folder is empty.\n[Make sure there is at least one Image to select.]")
        if xlsx_empty:
            print("XLSX Files folder is empty.\n"
                  "[Make sure there is at least one Image to select.]")
        print("Enter 1 to select Image from Images dir:")
        print("Enter 2 to select XLSX from XLSX_Files dir:")
        print("Enter 3 to print the ids and names in the selected Image.")
        print("Enter 0 to Exit.\n")
        print("By Default: First Image  and XLSX is selected. ")
        while True:
            x = int(input("Enter your choice:"))
            if 0 < x > 3:
                print("Wrong input. Please choice carefully.")
            else:
                break
        if x == 0:
            break
        elif x == 1:
            print("Image Files:")
            i = 1;
            for x in images:
                print(str(i) + " " + str(x))
                i += 1
            while True:
                image_no = int(input("Select Image no:")) - 1
                if 0 <= image_no < len(images):
                    image_file_name = image_folder_name + images[image_no]
                    print("Image:" + image_file_name + " was selected.")
                    break
                print("Wrong input")
        elif x == 2:
            print("XLSX Files:")
            i = 1
            for x in xlsx_list:
                print(str(i) + " " + str(x))
                i += 1
            xlsx_no = 0
            while True:
                xlsx_no = int(input("Select XLSX no:")) - 1
                if 0 <= xlsx_no < len(xlsx_list):
                    xlsx_file_name = xlsx_folder_name + xlsx_list[xlsx_no]
                    print("XLSX:" + xlsx_file_name + " was selected.")
                    break
                print("Wrong input")
        elif x == 3:
            if xlsx_empty:
                print("There is no xlsx file in the" + xlsx_folder_name + "dir.")
                break
            elif image_empty:
                print("There is no image file in the" + image_folder_name + "dir.")
                break
            print("Image-" + image_file_name)
            print("XLSX-" + xlsx_file_name)
            print("was selected")
            print("Insert id and name in the image:")
            data = pd.read_excel(xlsx_file_name)
            image_process_no_specification(data.iterrows(), image_file_name)
            print("Print Done")
            continue


# def import_images_with_heading_numbers
if __name__ == "__main__":
    main()
