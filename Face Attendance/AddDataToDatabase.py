import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://face-attendance-system-1b6e8-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "0021":
    {
        "name": "Ayan Ul Haq",
        "course": "B.Tech",
        "starting_year": 2021,
        "total_attendance": 63,
        "branch": "CS",
        "year":4,
        "last_attendance_time": "2022-12-11 10:54:34"
    },
    "0029":
    {
        "name": "Vipin Jaiswal",
        "course": "BCA",
        "starting_year": 2024,
        "total_attendance": 1,
        "branch": "Cyber Security",
        "year":1,
        "last_attendance_time": "2024-12-11 02:55:34"
    },
    "0070":
    {
        "name": "Nitin Jaiswal",
        "course": "B.Tech",
        "starting_year": 2021,
        "total_attendance": 72,
        "branch": "CS",
        "year":4,
        "last_attendance_time": "2024-07-02 00:02:04"
    },
    "0098":
    {
        "name": "Shoaib Khan",
        "course": "B.Tech",
        "starting_year": 2021,
        "total_attendance": 54,
        "branch": "CS",
        "year":2,
        "last_attendance_time": "2022-12-11 02:55:34"
    },
    "0111":
    {
        "name": "Uzair Khan",
        "course": "B.Tech",
        "starting_year": 2024,
        "total_attendance": 44,
        "branch": "CS",
        "year":3,
        "last_attendance_time": "2023-12-11 02:55:34"
    }
}

for key,value in data.items():
    ref.child(key).set(value)