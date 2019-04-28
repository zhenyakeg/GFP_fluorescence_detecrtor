# GFP fluorescence detector

This program is designed for detection of GFP fluorescence in 96-well plates.

## Contacts

Eugene Kegeles kegeles.ea@phystech.edu
## Requirements

- Python 3.x
- NumPy Python library
- OpenCV Python library

## Usage

usage: python Image processing.py [-h] -i INPUT [-t TYPES] [-pt PIXEL_THRESHOLD]
                           [-it IMAGE_THRESHOLD] [-f FILTER_SIZE] [-a ALPHA] [-b BETA] 
1. **Required arguments:**
    -  -i INPUT, --input INPUT
                        Full input path for your experiment with scanned plates inside.
      
      ```bash
        ./Folder_with_experiment/Folders_with_plates
        # inside the plate folder images should be named as [A-D][01-12]_*.file_type
      ```
2. **Optional arguments:**
    * -h, --help            show this help message and exit

    *  -t TYPES, --types TYPES
                        Image types you are going to analyse separated with a space.  
                        *Defaults: png, tif*
                        
    *  -pt PIXEL_THRESHOLD, --pixel_threshold PIXEL_THRESHOLD
                        Pixel threshold applied to your images.  
                        Type: int.  
                        *Default: 9*
    *  -it IMAGE_THRESHOLD, --image_threshold IMAGE_THRESHOLD
                        Image score threshold applied to your images.  
                        Type: int.  
                        *Default: 589*
    *  -f FILTER_SIZE, --filter_size FILTER_SIZE
                        Median filter radius applied to your images for
                        smoothing.  
                        Type: odd int.  
                        *Default: 3*
    * -a ALPHA, --alpha ALPHA
                        Contrast enhansement.  
                        Type: float.  
                        *Default: 1.4*
    * -b BETA, --beta BETA  Brightness enhansement.  
                          Type: int.  
                        *Default: 10*
        
## Output

All the Output files will be stored in each plate's directory.

- Makes a new directory "Changed" with modified images showing GFP-positive areas in all wells of this plate.
- File "log.txt" contains the information about all selected wells from this plate: score, background, etc.
- File "layout.txt" shows where in a plate selected wells were located.

## Algorithm overview

1. RGB image is converted to monochrome.
2. Contrast enhansment is performed.  
``` python
image = ALPHA * image + BETA
```
3. Background is calculated as an average intensity on a rectangle with the center in the middle of the image and with linear sizes corresponding to 80% of an image dimentions.

4. Background substraction is performed.

5. Image is being thresholded with the IMAGE_THRESHOLD.

6. Median filter is applied to the thresholded image of FILTER_SIZE.

7. Number of 255 - valued pixels is calculated in the thresholded and filtered image. This score represents GFP - positive area in the well.

8. Wells with the score higher then IMAGE_THRESHOLD are selected.

