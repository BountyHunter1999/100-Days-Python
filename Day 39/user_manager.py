import requests


class UserManager:

    def __init__(self, token, username, project, name):
        self.header = {
            "Authorization": f"Bearer {token}"
        }
        self.username = username
        self.project = project
        self.name = name
        self.url = f'https://api.sheety.co/{self.username}/{self.project}/{self.name}'

    def get_user(self):
        res = requests.get(self.url, headers=self.header)
        return res.json()

    def new_user(self):
        user_data = self.get_user()['users']
        print("\tYou're about to subscribe to our Cheap Flight Search Service", end="\n\n")
        f_name = input("Enter Your First Name: ")
        l_name = input("Enter Your Last Name: ")

        user_email = [user['email'] for user in user_data]
        user_num = [user['phoneNumber'] for user in user_data]
        while True:
            email = input("Enter Your Email Address: ")
            if email in user_email:
                print("This email address already exist. Try a new one!")
            else:
                break
        while True:
            phone_num = input("Enter Your Contact Number: ")
            if phone_num in user_num:
                print("This phone number already exists. Try a new one!")
            else:
                break

        params = {
            "user":
                {
                    'firstName': f_name,
                    'lastName': l_name,
                    'email': email,
                    'phoneNumber': phone_num
                }
        }

        res = requests.post(self.url, json=params, headers=self.header)
        print("You're in the club")
        return res.text
