#!/usr/bin/env python
# coding: utf-8

# In[16]:


import tensorflow as tf


# In[17]:


import matplotlib.pyplot as plt


# In[18]:


from tensorflow import keras 


# In[19]:


import numpy as np 


(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data() 

plt.imshow(x_train[1]) 
plt.imshow(x_train[0]) 

x_train = x_train.astype('float32') / 255.0 
x_test = x_test.astype('float32') / 255.0 


# In[24]:


x_train = x_train.reshape(-1, 28, 28, 1) 
x_test = x_test.reshape(-1, 28, 28, 1) 


# In[25]:


x_train.shape


x_test.shape



y_train.shape

y_test.shape


# In[29]:


model = keras.Sequential([
keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),

keras.layers.MaxPooling2D((2,2)),
keras.layers.Dropout(0.25),

keras.layers.Conv2D(64, (3,3), activation='relu'),
keras.layers.MaxPooling2D((2,2)),

keras.layers.Dropout(0.25),

keras.layers.Conv2D(128, (3,3), activation='relu'),

keras.layers.Flatten(),
keras.layers.Dense(128, activation='relu'),

keras.layers.Dropout(0.25),
keras.layers.Dense(10, activation='softmax')

])
model.summary()


# In[30]:


model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))


# In[31]:


test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:',test_acc)


# In[ ]:




