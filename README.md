# GFP fluorescence detector

This program is designed for detection of GFP fluorescence in 96-well plates.

## Requirements

- Python 3.x
- NumPy Python library
- OpenCV Python library

## Usage

usage: python Image processing.py [-h] -i INPUT [-t TYPES] [-pt PIXEL_THRESHOLD]
                           [-it IMAGE_THRESHOLD] [-f FILTER_SIZE] [-a ALPHA] [-b BETA] \\
1. **Required arguments:**
    -  -i INPUT, --input INPUT
                        Full input path for your experiment with scanned plates inside.
      
      ```bash
        "./Folder_with_experiment/Folders_with_plates( inside the plate folder images should be named as [A-D][01-12]_*.png
      ```
2. **Optional arguments:**
    * -h, --help            show this help message and exit

    *  -t TYPES, --types TYPES
                        Image types you are going to analyse.
    *  -pt PIXEL_THRESHOLD, --pixel_threshold PIXEL_THRESHOLD
                        Pixel threshold applied to your images.
    *  -it IMAGE_THRESHOLD, --image_threshold IMAGE_THRESHOLD
                        Image score threshold applied to your images.
    *  -f FILTER_SIZE, --filter_size FILTER_SIZE
                        Median filter radius applied to your images for
                        smoothing.
    * -a ALPHA, --alpha ALPHA
                        Contrast enhansement.
    * -b BETA, --beta BETA  Brightness enhansement.

