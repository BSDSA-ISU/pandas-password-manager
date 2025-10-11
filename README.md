# 🔒 Password Manager

## what is this?

- its just a simple password manager using python.

## 🫰 Features

- it provides some basic key based encryption using fernet with strong 2^256 key

---

## How to set up

1. ### **Install python(if it isn't installed):**

   - windows:
     - [python download](https://www.python.org/downloads/windows/)

   - for linux:

    ```bash
    # debian/ubuntu or other debian based linux apt
    sudo apt install python3

    # arch and other arch based distros
    sudo pacman -Sy python

    # gentoo portage
    sudo emerge -v python
    ```

2. ### **run for linux:**

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

3. **run for windows 11/10:**

    ```ps1
    # creates a virtual environment
    python -m venv .venv

    # activate on pwsh/windows
    cd .venv\Scripts\; .\activate.ps1 ; cd ..\..

    # Finally install the required dependencies
    pip install -r requirements.txt
    ```

4. ### 💡 Note: On windows if you get an error like “cannot be loaded because running scripts is disabled on this system”, you need to enable execution with

```ps1
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

```mermaid
gitGraph
  checkout main-rc
  commit
  commit
  commit
  commit
  commit
  commit
  checkout main
  commit
  commit
  commit
  commit
  commit
```

---

### Q and A 💬

1. **what if i lost my keyfile?**
    - too bad lol. no really:
2. **what if someone stole my key? how do i protect it?**
     - it can't be stolen when no one uses your pc/laptop, unless it is hacked.
     - also to protect your key file. store it on external storage or on protected folders
3. **is there some recovery methods here?**
     - nope.
4. **where's the keyfile?**
    - its on the same working dir and it is named **key.key**
