# ExtendingDjangoAuth
---
extending django authentication is a  practical assesment.
Extended django inbuilt Authentication by abstracting **User**

### How it works
1. Register.Username and password is required but email and other fields are optional.
+ If you enter email during registration, a token is sent to your email and if valid,automatically logs you in.
+ If you didn't enter email during registration, upon  sucessful log in , user is re-directed to update profile with the  email, a confirmation link sent and if successful,it redirects to the homepage

