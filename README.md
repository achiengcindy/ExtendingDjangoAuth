# ExtendingDjangoAuth
---
extending django authentication is a  practical assesment.
Extended django inbuilt Authentication by abstracicting **User**

### How it works
1. Register.Username is required but email is optional.
+ If you put email during registration, a token is sent to your email and if valid,automatically logs you in.
+ If you didn't put email, you sucessfully log in and is directed to update profile with the  email, a confirmation link sent and if successful,it redirects to the homepage

