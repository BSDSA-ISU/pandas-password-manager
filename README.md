# Password Manager

## what is this?

- its just a simple password manager using python.

## Features

- it provides some basic key based encryption using fernet

## How to set up

- run:

```bash
python -m venv .venv

# activate on linux
source .venv/bin/activate

# activate on pwsh
cd venv\Scripts\; .\activate.ps1 ; cd ..\..

# Finally install the dependencies
pip install -r requirements.txt
```

### Q and A

- what if i lost my keyfile?
  - too bad lol. no really:
- what if someone stole my key? how do i protect it?
  - it can't be installed when no one uses your pc/laptop
  - also to protect your key file. store it on external storage or on protected folders
- is there some recovery methods here?
  - nope.
