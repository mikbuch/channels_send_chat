# Send message to a logged-in user and to all users

This repository contains example code for a [question at StackOverflow](https://stackoverflow.com/questions/68172488/django-channels-group-send-getting-delayed-while-sending-to-active-window-whe).

![Group send example](channels_group_send.gif)

The question: https://stackoverflow.com/questions/68172488/django-channels-group-send-getting-delayed-while-sending-to-active-window-whe

Related Django documentation: https://channels.readthedocs.io/en/stable/tutorial/part_2.html#write-your-first-consumer

Run the application:

```bash
python manage.py runserver localhost:8000
```

Migration and creating an example user:
```bash
python manage.py migrate
python manage.py createsuperuser --username=channel_user --email=channel@example.com
```

Log in with Django Admin: http://127.0.0.1:8000/admin

Chat URL (logged in session): http://127.0.0.1:8000/chat/632521/

Chat URL (incognito/private session, i.e., user not logged in): http://127.0.0.1:8000/chat/632521/ 

---

Answer:

The working version of the code is avaliable at [my git repository](https://github.com/mikbuch/channels_send_chat).

I tried to recreate your example, but you shared only parts of your code. I had to fill out the missing parts. In all, it was better to just follow the [example from the documentation](https://channels.readthedocs.io/en/stable/tutorial/part_2.html#write-your-first-consumer) exactly. The repository I shared is adapted to your code, to reassemble it as closely as possible.

I don't know exactly why you were getting the delay, but the application example I shared has exactly the same version of Python, and the packages, as you:

 > Python 3.9.5, Django 3.2, Channels 3.0.3
 
and everything works correctly when running it on macOS (i.e., no delays).

If you are still interested in this subject, please try to run my example and let me know if you are still getting the error (the delays).

Anyways, maybe someone else will find my example helpful, when having a similar problem, cheers.