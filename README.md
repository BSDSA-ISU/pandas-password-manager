# Password Manager

## what is this?

- its just a simple password manager using python.

## Features

- it provides some basic key based encryption using fernet with strong 2^256 key

## How to set up

- run:

```bash
# creates a virtual environment
python -m venv .venv

# activate on linux
source .venv/bin/activate

# activate on pwsh/windows
cd .venv\Scripts\; .\activate.ps1 ; cd ..\..

# Finally install the required dependencies
pip install -r requirements.txt
```

## 💡 Note: On windows if you get an error like “cannot be loaded because running scripts is disabled on this system”, you need to enable execution with

```ps1
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### Q and A

- what if i lost my keyfile?
  - too bad lol. no really:
- what if someone stole my key? how do i protect it?
  - it can't be stolen when no one uses your pc/laptop
  - also to protect your key file. store it on external storage or on protected folders
- is there some recovery methods here?
  - nope.
