from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e'
def get_reuirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='Fault detection',
    version='0.0.1',
    author='Neeraj_Kumar',
    author_email='neerajkumar1092005@gmail.com',
    install_reqirements=get_reuirements('requirements.txt'),#requrements kha se aa rha hai
    packages=find_packages()# packeg ko find krega main foulder se
)