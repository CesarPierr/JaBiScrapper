from distutils.core import setup

setup(
    name='jabis',
    version='0.1.0',
    author='pedroczr',
    description='Python 3.x module to scrap data from multiples sources and treat it',
    packages=['JaBiScrapper',],
    license='MIT License',
    long_description=open('README.md').read(),
    intall_requires=[
        "pandas", 
        "numpy", 
        "requests", 
        "bs4", 
        "lxml", 
        "html5lib", 
        "urllib3", 
        "selenium", 
        "pyvirtualdisplay", 
        "pyautogui", 
        "pyperclip", 
        "pytesseract", 
        "Pillow", 
        "opencv-python",],
    extras_require={
        'test':['unittest2']
    }
)