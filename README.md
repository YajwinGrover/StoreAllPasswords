# StoreAllPasswords

This is CLI password manager. I created this project as a way to store your passwords locally on your device in a secure fernet encrytion.
I am still working on adding features to make it better. Feel free to create an issue for a feature you want, and I'll try adding it.

# Installation

## Download code
Click the Green Code button and click download zipped file. Unzip the file and navigate to the folder in terminal

## Download dependancies
Navigate to the unzipped folder in terminal by running
```bash
cd Downloads/StoreAllPasswords-main
```
Check if you have python3 by running 
```bash
python3 -V
```
If you python version is not atleast 3.9.0, please update your python version

Check your pip version
```bash
pip -V
```
If this returns an error, or you pip version is below 22.3, please upgrade your pip version


Next download the Fernet library by running
```bash
pip install cryptography
```

## Setting up the CLI

Run the following steps to move storeAllPasswords.py to ~/bin. MAKE SURE YOUR TERMINAL IS IN THE DIRECTORY WITH THE PYTHON FILE

```bash
mkdir ~/bin
mv storeAllPasswords.py ~/bin
```
If ~/bin already exists, you can skip the first command

Next navigate to the ~/bin folder

```bash
cd ~/bin
```

Make an alias so you dont have to type storeAllPasswords.py everytime you want to run it. Make the alias be called sap

```bash
cp storeAllPasswords.py sap
```
Finally, to make the command accesible from anywhere run
```bash
export PATH=$PATH":$HOME/bin
```
Run 
```bash
sap
```
