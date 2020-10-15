# SlideCapture
A simple python script to save the slides of an online lecture while it is held for future reference

# Detailed explanation
The script will take a screenshot every [TIMEOUT] seconds, compare this screenshot to the previous one, and save it (at [FILEPATH])if it is not similar to it. Similarity is based on two measurements: the Mean squared Error and the structural similarity of scikit-image. Both It compares the value of each of them to a predefined threshold ([MSE_THRESH] and [SSME_THRESH])  
One could possibly specify a region of the screen to take the screenshot  
If the slides are in a video that shows its controls on mouse movement, one can set the boolean CROP_COMPARISON_IMAGE to true and specify the bounding box. This will only affect the image that will be compared, not the final screenshots

# Word of Warning
If the selected directory already contains files called slide0.png, slide1.png... it will just overwrite them

# Suggested Usage
The tool is made for online lectures, where the lecturer advances to the next slide before one could copz all the relevant information from a slide. For this, zou could have he location of the screenshots open and, when needed, reopen a previous slide.


# How to use
install requirements  
  
specify:   
FILEPATH (where to store the slides screenshots)  
TIMEOUT (how long to wait before capturing new screenshot and compare to previous)  
MSE_THRESH: Threshold for Mean-square error (picture compare: 0 means pictures identical)  
SSIM_THRESH: Threshold for Structural Similarity measure (1.0 means the pictures are identical)  
  
run main.start (or just main.py)  
