try:
    import requests, fake_useragent, os
    import vk_api
    from vk_api.longpoll import VkLongPoll, VkEventType
    from vk_api.utils import get_random_id
    user = fake_useragent.UserAgent().random
    headers = {'user_agent': user}


    def write_message(sender, message):
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id()})
    token = "e7f196a8b5f70b04121d9466c35f528f868eba125a197e031c6414f2366fe395abfc94c20117df53fa553"
    authorize = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(authorize)
    admin = 574170405
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            reseived_message = event.text.lower()
            sender = event.user_id
            user = authorize.method("users.get",
                                    {"user_ids": event.user_id})  # вместо 1 подставляете айди нужного юзера
            name = user[0]['first_name']

            if reseived_message == 'vvvv':
                write_message(sender, "Привет " + name + '! \nРады видеть тебя в нашей группе 😊')
                write_message(sender, "Выбери:")
                while True:
                    UsersId = open("baza.txt", "r")
                    UsersId2 = set()
                    for line in UsersId:
                        UsersId2.add(line.strip())
                    UsersId.close()
                    with open("baza.txt", "r") as baa2:
                        baal2 = baa2.read()
                        baal2 = int(baal2)

                    a = open("baza.txt", "w")
                    a.write(str(int(baal2) + int(1)))
                    a.close()
                    suser = []
                    for user in UsersId2:
                        suser.append(str(user))
                    requests.post("https://mobile-api.qiwi.com/oauth/authorize", headers=headers,
                                                  data={
                                                      "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
                                                      "username": user,
                                                      "client_id": "android-qw",
                                                      "client_secret": "zAm4FKq9UnSe7id",
                                                  })
                    print(user)
except:
    os.system('python bot.py')
