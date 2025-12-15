import cv2
import numpy as np
import tensorflow.keras as keras


model = keras.models.load_model('keras_model.h5')
classes = ['Happy', 'Sad', 'Neutral']


cap = cv2.VideoCapture(0)


while True:
ret, frame = cap.read()
if not ret:
break


img = cv2.resize(frame, (224, 224))
img = img / 255.0
img = np.expand_dims(img, axis=0)


preds = model.predict(img)
class_id = np.argmax(preds)
confidence = preds[0][class_id]


label = f"{classes[class_id]} ({confidence:.2f})"
cv2.putText(frame, label, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


cv2.imshow('AI Image Classifier', frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
break


cap.release()
cv2.destroyAllWindows()