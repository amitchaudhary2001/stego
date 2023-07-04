import shutil
import random


image_files = [
    
# 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image1.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image2.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image3.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image4.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image5.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image6.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image7.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image8.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image9.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image10.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image11.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image12.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image13.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image14.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image15.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image16.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image17.jpg',
'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image18.jpg',
# 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image1/image19.jpg',



# 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image2/image1.jpg',
# 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image2/image2.jpg',
# 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image2/image3.jpg',
# 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image2/image4.jpg',
# 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image2/image5.jpg',
# 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image2/image6.jpg',
# 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image2/image7.jpg',
# 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image2/image8.jpg',
# 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/image2/image9.jpg',


]
random_image = random.choice(image_files)
print(random_image)


# source_path = 'path/to/source/image.jpg'
destination_path = 'C:/Users/amit2/OneDrive/Desktop/6th sem project/flask enviroment/static/images/new_image.png'

shutil.copy(random_image, destination_path)



# print(random_image)
