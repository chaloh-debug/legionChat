# legionChat

## What is legionChat
legionChat was a portfolio web app project by Charles. It was built on django framework for the back-end and html, css and js for the web application  front-end. Postgresql was used for the application database. The web application was deployed to heruko.

## What it does
legionChat is a web application that allows for realtime communication. It does this by allowing users to create and/or chatrooms. It uses websockets to send real-time messages by using asynchronous chatConsumer. It also allows user to update their own profile and view other user profiles. On the user profile view one can send friend request to other users. User data is stored inside a posgresql database. A redis database handles caching of data.

## Installation instructions
For users wishing to directly use or customize the application.
1. Clone the project directory.

2. Navigate to the legionChat directory.

3. Open terminal and install required dependencies using following command -

    pip install -r requirements.txt

4. Open terminal in directory where **manage** python file resides. And then execute following command -

    python manage.py runserver
    
5. Go to browser and hit following url -

    localhost:8000
    
## Usage
1. visit the legionChat site.
2. Signup or login to the app.
3. Visit the legionChat chat section to create or join existing rooms.

<p align="center">
  <img src="https://github.com/chaloh-debug/legionChat/blob/main/static/assets/images/rooms.png"
       width="600"
  />
</p>

3. Start Chatting.

<p align="center">
  <img src="https://github.com/chaloh-debug/legionChat/blob/main/static/assets/images/chats.png"
       width="600"
  />
</p>

5. Visit the legionChat request section to view users.

<p align="center">
  <img src="https://github.com/chaloh-debug/legionChat/blob/main/static/assets/images/users.png"
       width="600"
  />
</p>

5. Visit the legionChat request section,select a user to view their profile and send a friend request.

<p align="center">
  <img src="https://github.com/chaloh-debug/legionChat/blob/main/static/assets/images/profile.png"
       width="600"
  />
</p>

7. Visit the legionChat friends section to view received friend requests.

<p align="center">
  <img src="https://github.com/chaloh-debug/legionChat/blob/main/static/assets/images/friends.png"
       width="600"
  />
</p>


## Features
- Chatroom creation.
- Real-time chat messaging.
- View other users' profiles.
- Send friend requests.
- View received friend requests.
- profile page to update user details

## Future of legionChat
- [ ] Accept friend requests.
- [ ] Create private chats.
- [ ] dockerize the app

## Authors

- **Charles Gitahi** <[Chaloh](https://github.com/chaloh-debug)>