#can build entire ml project as a package and do
from setuptools import find_packages,setup
from typing import List#to use list

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Read the requirements file and return the list of requirements
    '''
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        #to start our setup.py directly after reading we use the -e . so that also will come here so shd be removed
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Keerthan Kumar C',
    author_email='ckeerthankumar4@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)