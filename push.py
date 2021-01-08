import pyrebase
import keyboard

#pip install pyrebase
#pip install keyboard

config = {
  "apiKey": "AAAA6BYFJnA:APA91bESUm5sRscZLxe2ey74U4dGHHkqkGXz04SC4xHvzRbPBEGBGm92EMbk9SWcgTv9D_NCHKtXRxXKwfXhNClWyi9JxB6IhnrukG0Vv3rOvhCl7gm0L_aKoIqR21TV7fKr1eNOnMQd",
  "authDomain": "scooby-a36d6.firebaseapp.com",
  "databaseURL": "https://scooby-a36d6-default-rtdb.firebaseio.com/",
  "storageBucket": "scooby-a36d6.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

data = {"Goal": 0,
	"status": 0}
db.child("move_goal").update(data)
#db.child("cmd_vel").push(data)
i = 0
while(1):
    if keyboard.read_key() == "a":
        print("New Goal: A\n")	
        data = {"Goal": 1,
		"status": 0}
	db.child("move_goal").update(data)

    if keyboard.read_key() == "b":
	print("New Goal: B\n")	
	data = {"Goal": 2,
		"status": 0}
	db.child("move_goal").update(data)

    if keyboard.read_key() == "c":
	print("New Goal: C\n")	
	data = {"Goal": 3,
		"status": 0}
	db.child("move_goal").update(data)

    if keyboard.read_key() == "z":
	print("New Goal: Z\n")	
	data = {"Goal": 0,
		"status": 0}
	db.child("move_goal").update(data)


