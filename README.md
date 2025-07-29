# RepositoryCount

```
 ____                   ____                  _            
|  _ \ ___ _ __   ___  / ___|___  _   _ _ __ | |_ ___ _ __ 
| |_) / _ \ '_ \ / _ \| |   / _ \| | | | '_ \| __/ _ \ '__|
|  _ <  __/ |_) | (_) | |__| (_) | |_| | | | | ||  __/ |   
|_| \_\___| .__/ \___/ \____\___/ \__,_|_| |_|\__\___|_|   
          |_|                                       
```
# 📦 RepositoryCount

A fun Python script that fetches your public GitHub repository count and generates a graphical counter image using custom digit images!  
Perfect for adding a visual repo badge to your README, website, or just for learning web scraping and image processing.



## ✨ Features

- 🔍 **Scrapes your GitHub profile** for the current public repository count
- 🖼️ **Renders the count as an image** using custom digit PNGs
- 💾 **Saves the result as `Counter.png`** in your project folder
- 🧩 **Easy to customize** with your own digit images



## 🛠️ Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) (`pip install pillow`)
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

## 🚀 How to Use

1. **Install dependencies:**
   ```sh
   pip install pillow requests beautifulsoup4
   ```

2. **Run the script with your GitHub username as an argument:**
   ```sh
   python GitRepoImg.py YOUR_GITHUB_USERNAME
   ```

3. **Check the output:**  
   The script will generate a `Counter.png` file showing your current repo count using the digit images from the `Imgs/` folder.

## 🖼️ Customization

- Replace the PNGs in the `Imgs/` folder (`0.png` to `9.png`) with your own digit designs for a personalized look!


## 📂 Project Structure

```
RepositoryCount/
├── GitRepoImg.py
├── Counter.png         # Output image (created after running the script)
├── README.md
└── Imgs/
    ├── 0.png
    ├── 1.png
    ├── 2.png
    ├── 3.png
    ├── 4.png
    ├── 5.png
    ├── 6.png
    ├── 7.png
    ├── 8.png
    └── 9.png
```


## 🤔 Why?

This project is a playful way to combine **web scraping** and **image processing** in Python.  
Use it to show off your repo count, learn about BeautifulSoup and Pillow, or just have fun!

