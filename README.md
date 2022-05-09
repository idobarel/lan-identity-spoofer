# Ciosc Hack.

__A simple python code that allows you to break in a network without you having to put your email address or something.__

# Installation:
```bash
$ pip3 install -r requirements.txt
```

# How Does It Work?
Well, usually when someone is puting a page like that, he's storing mac addresses to see to which request he should or should not put a landing page.

With that being said, you can now understand the code.

First, you need to be logged in to the network. 
The app scans the network and saves all the mac address of the clients it found.
Then the program will lunch a DOS attack against the target mac, and then he will get kicked off the network.
Then the program will change your mac address to the targets one.

And BOOM you are in!

# Running:
```bash
python3 main.py
```

__I Don't recommand using this script for something beside pen-testing.__

__Have A Good Day__
