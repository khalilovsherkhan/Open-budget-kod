import json

def load_data():
    try:
        with open('user_data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def save_data(data):
    with open('user_data.json', 'w') as file:
        json.dump(data, file)

def get_user_vote(username):
    data = load_data()
    if username in data:
        return data[username]['vote']
    else:
        return None

def cast_vote(username, last_name, phone_numbers):
    vote = input("Qaysi koʼchaga ovoz berasan : ")
    data = load_data()
    data[username] = {'last_name': last_name, 'phone_numbers': phone_numbers, 'vote': vote}
    save_data(data)
    print(" Ovozingiz qabul qilindi !!!! Bor yana bitta ovoz topip kel!")

def main():
    username = input("Ismingni yozee: ")
    last_name = input("Familyangni yozmasang bolmaydi: ")
    phone_numbers = input("Nomer yoz tamom: ").split(',')
    
    previous_vote = get_user_vote(username)
    if previous_vote:
        print(f"Koʻcha  nomini kiriting: {previous_vote}")
    else:
        cast_vote(username, last_name, phone_numbers)

if __name__ == "main":
    main()