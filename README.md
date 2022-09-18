# StoreAllPasswords

This is CLI password manager. I created this project as a way to store your passwords locally on your device in a secure fernet encrytion.
I am still working on adding features to make it better, but what it can do right now is:

1. Read your passwords and usernames from a json
2. List all the sites you have passwords for
3. Delete and add passwords and sites
4. Prompt you for a master password before copying the password to your clipboard


*The json file is not included so if you want to use my code, you can but make sure to change lines #45,50 and 60 to the path of your json file. Also change line # to the path of a file which the first line consists of a fernet key, and the second line the master key
