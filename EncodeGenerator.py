import os
import cv2
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-73051-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-73051.appspot.com"
})

# importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
# print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    # print(path)
    # print(os.path.splitext(path)[0])
    studentIds.append(os.path.splitext(path)[0])

    filename = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)


# print(len(imgList))
# print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print("Encoding Started .....")
encodeListKnow = findEncodings(imgList)
print("Encoding Complete")
# print(encodeListKnow)

encodeListKnowWithIds = [encodeListKnow,studentIds]

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnowWithIds, file)
file.close()
print('file save')

