from setuptools import find_packages
from setuptools import setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirments(file_path:str)-> List[str]:
    """
    this functon will return list of requirments
    """
    requirments =[]
    with open(file_path) as f:
        requirments = f.readlines()
        requirments =[reqs.replace("\n", "")for reqs in requirments]
        
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT) 
    return requirments

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Nitin kalra',
    author_email = 'nitin.kalra70@gmail.com',
    packages=find_packages(),
    install_requires = get_requirments('requirments.txt'))