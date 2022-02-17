# Send message to a logged-in user and to all users

This repository contains example code for a [question at StackOverflow](https://stackoverflow.com/questions/68172488/django-channels-group-send-getting-delayed-while-sending-to-active-window-whe).

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

The working version of the code is available at [my git repository](https://github.com/mikbuch/channels_send_chat).

I tried to recreate your example, but you shared only parts of your code. I had to fill out the missing parts. In all, it was better to just follow the [example from the documentation](https://channels.readthedocs.io/en/stable/tutorial/part_2.html#write-your-first-consumer) exactly. The repository I shared is adapted to your code, to reassemble it as closely as possible.

**User logged-in in a single place**

On one browser (Safari) the user is logged-in, on the other (Chrome) use is not logged in.

![Group send example](channels_group_send.gif)

The application example I shared has exactly the same version of Python, and the packages, as you:

 > Python 3.9.5, Django 3.2, Channels 3.0.3
 
When the user is logged in one browser/window, verything works correctly when running it on macOS (i.e., no delays).

**User logged-in in several different places**

(Different browsers)

I also tried the following scenario:

 * Safari -- user logged in
 * Fifefox -- user logged in
 * Chrome -- user **not** logged in

and now I was getting the same delays as you!

Link to the video showcasing the delays: https://www.youtube.com/watch?v=b-1kT--Qx0w

Now I will try updating to Django 4.0 and channels 3.0.4 and I will see if this problem is still the case.