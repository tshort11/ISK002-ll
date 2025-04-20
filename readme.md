#  Welcome to *interlude!*

**interlude!** is a command-line music discovery and management application that lets users explore and rate their favorite songs, albums, and artists using the **Spotify API**.

---

##  Table of Contents

- [Installation Instructions](#installation-instructions)
- [Dependencies](#dependencies)
- [System/Hardware Requirements](#systemhardware-requirements)
- [How to Use](#how-to-use)
- [Features](#features)
- [License Information & Ethics](#license-information--ethics)

---

## Installation Instructions

Follow these steps to install the application:

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/tshort11/ISK002-ll.git
   cd interlude
   ```

2. **Install Required Dependencies**  
   Ensure you are in a virtual environment (optional but recommended), then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**  
   ```bash
   python main.py
   ```

---

##  Dependencies

The following libraries are required for the application to function correctly:

- **`requests`**: Handles HTTP communication with the Spotify API.
- **`rich`**: Enhances console UI with colors, tables, and formatting.
- **`colorama`**: Enables colored text on the command line (cross-platform).
- **`prettytable`**: Displays clean, readable tables for user data.
- **`json`**: Handles storage and retrieval of user data (built-in).
- **`os`**: Interacts with the file system (built-in).
- **Your custom modules** (e.g., `user.py`, `album.py`, etc.)

All external libraries can be installed via `pip`.

---

## System/Hardware Requirements

| Component         | Requirement                         |
|------------------|-------------------------------------|
| Operating System | Windows, macOS, or Linux            |
| Python Version   | Python 3.7 or higher                |
| Disk Space       | At least 50MB free for local files  |
| Internet         | Required for accessing Spotify API  |

---

##  How to Use

### 1. Launch and Authenticate
- Run `main.py` and select from:
  - **1**: Create a new user account
  - **2**: Log in to an existing account

### 2. Favorite Management
- **Add Favorite Album**: Search by name and rate it (0-5)
- **Add Favorite Song**: Search and rate songs similarly
- **Add Favorite Artist**: Add an artist by name

### 3. Discover New Music
- View trending or new Spotify releases:
  - Albums are shown with title, artist, release date, and links

### 4. View and Manage Your Profile
- See your saved:
  - Favorite albums with ratings
  - Favorite songs
  - Favorite artists

### 5. Exit and Save
- Select **6** from the menu
- Saves all user data locally in `.json` format

### Tips for Best Experience
- Use stable internet during usage for API responses
- Avoid duplicate usernames
- Periodically update dependencies with:
  ```bash
  pip install --upgrade -r requirements.txt
  ```

---

## Features

| Feature                   | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| User Account Management   | Create, log in, and manage user profiles                                    |
| Favorite Albums & Songs   | Add and rate music you enjoy                                                |
| Favorite Artists          | Save your favorite music creators                                           |
| Discover Music            | View new releases and explore suggestions                                  |
| Saved Profiles            | Data is saved locally for future sessions                                  |
| CLI Interface             | Simple, readable interface for quick access                                |

---

##  License Information & Ethics

### 🔍 Third-Party Libraries and Licenses

| Library     | License Type       | Ethical Notes |
|-------------|--------------------|----------------|
| `requests`  | Apache License 2.0 | Open and permissive; promotes contribution and proper attribution. |
| `rich`      | MIT License        | Encourages reuse and sharing; ideal for open-source tools. |
| `colorama`  | MIT License        | Easy redistribution and modification make it open and ethical. |
| `prettytable`| MIT License       | Lightweight and reusable for both personal and commercial use. |
| `json` (builtin) | Public Domain | No restrictions on use; encourages free and open development. |

### Ethical Use of Software

This project follows ethical guidelines for software development:

- **Transparency**: All libraries and their licenses are clearly documented.
- **Compliance**: Licensing terms are respected in distribution and use.
- **Attribution**: Credit is given to authors where required.
- **Open Source Support**: Use of libraries under MIT and Apache 2.0 licenses supports open-source collaboration.

**We do not use any third-party software with restrictive, unethical, or non-compliant licenses.**

---

By using **interlude!**, you join a community that values transparency, openness, and creativity in tech. 



