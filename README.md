# GFP fluorescence detector

This program is designed for detection of GFP fluorescence in 96-well plates.

## Requirements

- Python 3.x
- NumPy Python library
- OpenCV Python library

## Usage

usage: python Image processing.py [-h] -i INPUT [-t TYPES] [-pt PIXEL_THRESHOLD]
                           [-it IMAGE_THRESHOLD] [-f FILTER_SIZE]
                           [-r ROLLING_BALL] [-a ALPHA] [-b BETA]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Full input path for your experiment with scanned
                        plates inside.
  -t TYPES, --types TYPES
                        Image types you are going to analyse.
  -pt PIXEL_THRESHOLD, --pixel_threshold PIXEL_THRESHOLD
                        Pixel threshold applied to your images.
  -it IMAGE_THRESHOLD, --image_threshold IMAGE_THRESHOLD
                        Image score threshold applied to your images.
  -f FILTER_SIZE, --filter_size FILTER_SIZE
                        Median filter radius applied to your images for
                        smoothing.
  -r ROLLING_BALL, --rolling_ball ROLLING_BALL
                        If >0 radius for rolling ball background subtraction
                        applied to your images.
  -a ALPHA, --alpha ALPHA
                        Contrast enhansement.
  -b BETA, --beta BETA  Brightness enhansement.

