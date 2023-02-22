import os
from .__version__ import __version__, __author__

JABIS_BANNER = """
   .-,  .--.  ,---.   ,-.   .---. 
   | | / /\ \ | .-.\  |(|  ( .-._)
   | |/ /__\ \| |-' \ (_) (_) \   
   | ||  __  || |--. \| | _  \ \  
(`-' || |  |)|| |`-' /| |( `-'  ) 
 \_ )||_|  (_)/( `--' `-' `----'  
   (_)       (__)                           
"""

if not 'JABIS_BANNER' in os.environ or os.environ['JABIS_BANNER'] != 'disable':
    print(JABIS_BANNER)