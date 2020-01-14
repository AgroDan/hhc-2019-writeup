# Capteha Bypass with Machine Learning

Not "Captcha," but rather Capteha, which stands for "Completely Automated
Public Turing Test to tell Elves and Humans Apart. This challenge provided
you with 100 items to click on and tells you to select only gifts,
ornaments and stockings (for example). The choices were randomly generated.
Using the python requests library and the TensorFlow library I was able to
download and write the images directly from the API to disk and use
TensorFlow to correctly identify the images and submit them to the Capteha
API before the timer expires, and then submit the contest entry over and
over again until I win. Upon doing so, they email me the confirmation code.

The code I wrote for this challenge is a lot bigger than I would like to
copy-paste, so here is some of the code. The remainder can be found on my
github profile:

[My Capteha Code](capteha_api.py)
