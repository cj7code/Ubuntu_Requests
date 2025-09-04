# Ubuntu Requests - Image Fetcher 🖼️🌍

> *"I am because we are" -- Ubuntu Philosophy*

This project is a Python script inspired by the Ubuntu spirit of
**community, respect, and sharing**.\
It allows you to fetch and organize images from the internet mindfully
and safely.

------------------------------------------------------------------------

## ✨ Features

-   📥 Download **single or multiple images** from URLs\
-   ✅ Handles **errors gracefully** (network, invalid URLs, missing
    filenames)\
-   🛡️ **Safety checks**: verifies file type via HTTP headers\
-   🚫 Prevents **duplicate downloads** by comparing file contents\
-   📂 Saves images neatly in a dedicated `Fetched_Images` folder

------------------------------------------------------------------------

## 📦 Requirements

Make sure you have Python 3 installed.\
Install the required library:

``` bash
pip install requests
```

------------------------------------------------------------------------

## 🚀 Usage

Run the script in your terminal:

``` bash
python ubuntu_image_fetcher.py
```

### Example Run

![Terminal Demo](terminal_demo.png)

------------------------------------------------------------------------

## 🛠️ Implementation Details

-   **requests** → Fetches content from the internet\
-   **os.makedirs()** → Ensures the `Fetched_Images` directory exists\
-   **urllib.parse** → Extracts filenames from URLs\
-   **hashlib** → Generates unique filenames when missing\
-   **Graceful Error Handling** → Respects connections that fail

------------------------------------------------------------------------

## ⚡ Challenge Features Implemented

1.  **Multiple URLs** → Accepts comma-separated URLs\
2.  **Safety Precautions** → Checks `Content-Type`, applies timeouts\
3.  **Duplicate Prevention** → Compares existing files before saving\
4.  **HTTP Headers** → Ensures only valid image files are saved

------------------------------------------------------------------------

## 📂 Repository Structure

    Ubuntu_Requests/
    │── ubuntu_image_fetcher.py   # Main script
    │── README.md                 # Project documentation
    │── terminal_demo.png         # Example terminal screenshot
    └── Fetched_Images/           # Downloaded images (auto-created)

------------------------------------------------------------------------

## 🌍 Ubuntu Principles in Practice

-   **Community**: Connects to the global web to fetch resources\
-   **Respect**: Handles errors without crashing\
-   **Sharing**: Organizes images for reuse and collaboration\
-   **Practicality**: Provides a real, useful tool for daily life

> *"A person is a person through other persons."* -- Ubuntu Philosophy

------------------------------------------------------------------------

## 📜 License

This project is open-source and available under the MIT License.

------------------------------------------------------------------------

## 👨‍💻 Author

Developed with ❤️ and the spirit of **Ubuntu**
# Ubuntu Requests - Image Fetcher
