import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-73051-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "RA2211003011544":
    {
        "name": "ARIHANT JAIN",
        "major": "CSE AI-ML",
        "starting_year": 2017,
        "total_Attendance": 7,
        "standing": "G",
        "year": 4,
        "last_attendance_time" : "2022-12-11 00:54:34"

    },
"RA2211003011552":
    {
        "name": "ABHINAV SINGH",
        "major": "CSE BLOCKCHAIN",
        "starting_year": 2021,
        "total_Attendance": 12,
        "standing": "G",
        "year": 1,
        "last_attendance_time" : "2022-12-11 00:54:34"

    },
"RA2211003011559":
    {
        "name": "ACHINTYA GUPTA",
        "major": "CSE CORE",
        "starting_year": 2020,
        "total_Attendance": 7,
        "standing": "G",
        "year": 2,
        "last_attendance_time" : "2022-12-11 00:54:34"

    }
}

for key, value in data.items():
    ref.child(key).set(value)
