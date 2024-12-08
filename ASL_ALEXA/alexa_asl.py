import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os

for dirname, _, filenames in os.walk('/Users/anaceciliaguerra/Desktop/VueJs/ASL_ALEXA'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import keras
from keras.models import Sequential
from keras.layers import Dense,Flatten,Conv2D,MaxPool2D,Dropout
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_df=pd.read_csv('/Users/anaceciliaguerra/Downloads/sign_mnist_train.csv')
test_df=pd.read_csv('/Users/anaceciliaguerra/Downloads/sign_mnist_test.csv')

train_label=train_df['label']
trainset=train_df.drop(['label'],axis=1)

X_train = trainset.values
X_train = trainset.values.reshape(-1,28,28,1)

test_label=test_df['label']
X_test=test_df.drop(['label'],axis=1)

from sklearn.preprocessing import LabelBinarizer
lb=LabelBinarizer()
y_train=lb.fit_transform(train_label)
y_test=lb.fit_transform(test_label)

X_test=X_test.values.reshape(-1,28,28,1)

train_datagen = ImageDataGenerator(rescale = 1./255,
                                  rotation_range = 0,
                                  height_shift_range=0.2,
                                  width_shift_range=0.2,
                                  shear_range=0,
                                  zoom_range=0.2,
                                  horizontal_flip=True,
                                  fill_mode='nearest')

X_test=X_test/255

from tensorflow.keras.layers import Input

model=Sequential()

model.add(Input(shape=(28,28,1)))

model.add(Conv2D(128,kernel_size=(5,5), strides=1,padding='same',activation='relu'))
model.add(MaxPool2D(pool_size=(3,3),strides=2,padding='same'))

model.add(Conv2D(64,kernel_size=(2,2), strides=1,activation='relu',padding='same'))
model.add(MaxPool2D((2,2),2,padding='same'))

model.add(Conv2D(32,kernel_size=(2,2), strides=1,activation='relu',padding='same'))
model.add(MaxPool2D((2,2),2,padding='same'))
          
model.add(Flatten())

model.add(Dense(units=512,activation='relu'))
model.add(Dropout(rate=0.25))
model.add(Dense(units=24,activation='softmax'))

model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(train_datagen.flow(X_train,y_train,batch_size=200),
         epochs = 20,
          validation_data=(X_test,y_test),
          shuffle=1
         )
(ls,acc)=model.evaluate(x=X_test,y=y_test)

# Make predictions on the test data
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)

# Plot some test images along with predicted and actual labels
fig, axes = plt.subplots(4, 3, figsize=(10, 10))
axes = axes.flatten()

label_mapping = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H',
    8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P',
    16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X',
    24:'Y',25:'Z'
}

#print result
'''
for i, ax in enumerate(axes):
    ax.imshow(X_test[i].reshape(28, 28), cmap='gray')
    ax.set_title(f"Pred: {label_mapping[y_pred_classes[i]]}, Real: {label_mapping[y_true[i]]}")
    ax.axis('off')

plt.tight_layout()
plt.show()
'''

#print(f"Pred: {label_mapping[y_pred_classes[0]]}, Real: {label_mapping[y_true[0]]}")

#print("only pred: "+label_mapping[y_pred_classes[9]])

ledTurnOn = 0
if label_mapping[y_pred_classes[0]] == 'G':
    ledTurnOn = 1

#arduino 
import serial
import time

if ledTurnOn == 1 :
    # Use the correct port for your Arduino
    ser = serial.Serial('/dev/cu.usbmodem14301', 9600)  # Open serial port at 9600 baud
    time.sleep(2)  # Wait for Arduino to reset

    ser.write(b'1')  # Send '1' to turn the LED on
    time.sleep(2)    # Wait for 2 seconds

    ser.write(b'0')  # Send '0' to turn the LED off

    ser.close()  # Close the serial port

print(print("only pred: "+label_mapping[y_pred_classes[0]]))
