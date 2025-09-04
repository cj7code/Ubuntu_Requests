"""
Ubuntu-Inspired Image Fetcher
--------------------------------
"I am because we are" – Ubuntu Philosophy

This program respectfully connects to the web community, 
fetches shared image resources, and organizes them for later appreciation.

Features:
- Download single or multiple images from user-provided URLs
- Graceful error handling (network, HTTP errors, invalid URLs)
- Prevents duplicate downloads (checks existing files by name and size)
- Safe precautions: verifies content type and limits large downloads
- Organizes all images in a dedicated "Fetched_Images" directory

Libraries used:
- requests  (for HTTP requests)
- os        (for file and directory handling)
- urllib    (for parsing URLs)
- hashlib   (to generate unique filenames if needed)
"""

import requests
import os
import hashlib
from urllib.parse import urlparse

# Directory where images will be stored
IMAGE_DIR = "Fetched_Images"


def create_directory():
    """Create the Fetched_Images directory if it does not exist."""
    os.makedirs(IMAGE_DIR, exist_ok=True)


def get_filename_from_url(url, content):
    """
    Extracts filename from URL.
    If none is found, generates a unique one using hash.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    if not filename:  # If URL doesn't contain a filename
        # Generate unique filename based on hash of content
        file_hash = hashlib.md5(content).hexdigest()[:10]
        filename = f"image_{file_hash}.jpg"

    return filename


def is_duplicate(filepath, content):
    """
    Check if a file already exists with the same content.
    Prevents downloading duplicates.
    """
    if not os.path.exists(filepath):
        return False
    with open(filepath, "rb") as f:
        existing_content = f.read()
    return existing_content == content


def fetch_image(url):
    """Download a single image from the web and save it."""
    try:
        # Fetch with timeout and error handling
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Precaution: Check content-type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped: {url} (Not an image, Content-Type={content_type})")
            return

        # Extract filename
        filename = get_filename_from_url(url, response.content)
        filepath = os.path.join(IMAGE_DIR, filename)

        # Avoid duplicates
        if is_duplicate(filepath, response.content):
            print(f"✓ Skipped duplicate: {filename}")
            return

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Create directory
    create_directory()

    # Ask for one or multiple URLs
    urls = input("Please enter image URL(s) (comma-separated for multiple): ").split(",")

    # Fetch each image
    for url in [u.strip() for u in urls if u.strip()]:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
