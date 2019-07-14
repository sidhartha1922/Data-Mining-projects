#!/usr/bin/env python
# coding: utf-8

# In[1]:


import face_recognition

image = face_recognition.load_image_file("C:/Users/sidhartha/Desktop/fam.jpg")
face_locations = face_recognition.face_locations(image)


# In[2]:


face_locations[0]


# In[3]:


print("number of faces in this image:{}".format(len(face_locations)))


# In[4]:


len(face_locations)


# In[5]:


from PIL import image


# In[6]:


import PIL


# In[7]:


from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("C:/Users/sidhartha/Desktop/fam.jpg")

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()


# In[ ]:




