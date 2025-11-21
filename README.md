# Square Fit Batch

A lightweight Python tool that batch processes images. It resizes them to fit specific dimensions and adds transparent padding to create perfect squares, without cropping or distorting the original image.

This is useful for preparing consistent datasets for e-commerce, portfolios, or machine learning.

## Features

* **Bulk Processing:** Converts entire folders of images at once.
* **No Cropping:** Resizes the image to fit the target size while maintaining the aspect ratio.
* **Transparent Padding:** Centers the image and fills the empty space with transparency.
* **Standard Output:** Saves all files as high-quality PNGs.

## Prerequisites

* Python 3.x
* [Pillow](https://python-pillow.org/) (Python Imaging Library)

## Installation

1.  **Download:**
    * Click the green **<> Code** button at the top of this page.
    * Select **Download ZIP**.
    * Extract the ZIP file to a folder on your computer.

2.  **Install Dependencies:**
    Open your terminal or command prompt in the extracted folder and run:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Setup Folders:**
    Make sure your folder structure looks like this (create the `in` folder if it's missing):
    ```text
    square-fit-batch/
    ├── convert.py
    ├── in/          <-- Place source images here (jpg, png, webp, etc.)
    └── out/         <-- Script creates this for results
    ```

2.  **Run:**
    ```bash
    python convert.py
    ```

3.  **Done:**
    The processed images will appear in the `out` folder.

## Configuration

By default, images are output at **500x500** pixels. To change this:
1.  Open `convert.py` in any text editor.
2.  Edit the `DEFAULT_SIZE` number at the top of the file.
