# SlideCapture
A simple python script to save the slides of an online lecture while it is held for future reference

# How to use
install requirements

specify: 
FILEPATH (where to store the slides screenshots)
TIMEOUT (how long to wait before capturing new screenshot and compare to previous)
MSE_THRESH: Threshold for Mean-square error (picture compare: 0 means pictures identical)
SSIM_THRESH: Threshold for Structural Similarity measure (1.0 means the pictures are identical)

run main.start (or just main.py)
