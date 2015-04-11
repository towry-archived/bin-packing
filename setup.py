"""
    Bin packing algorithm

    :copyright: (c) 2015 by Towry Wang
    :license: MIT, http://towry.me/mit-license/
"""

import sys
from cx_Freeze import setup, Executable

__author__ = "Towry Wang"
__version__ = "0.1.0"
__contact__ = "towry@foxmail.com"
__url__ = "http://github.com/towry/bin-packing"
__license__ = "MIT"

base = None
if sys.platform == 'win32':
    base = "Win32GUI"

setup(name= "binpacking",
    version= __version__,
    description= "bin packing algorithm",
    long_description= __doc__,
    author= __author__,
    author_email= __contact__,
    url= __url__,
    license= __license__,
    packages= ['binpacking'],
    zip_safe= False,
    include_package_data= True,
    platforms= 'any',
    setup_requires= [
        "Pillow >= 2.7.0"
    ],
    executables= [Executable("binpacking/__main__.py", 
        base= base, 
        compress= True,
        targetName= "bp.exe")
    ]
    )
