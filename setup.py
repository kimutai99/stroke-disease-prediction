from setuptools import find_packages,setup
from typing import List
HYPHEN_DOT_E='-e .'

def get_requirements(file_path:str)->list[str]:
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        
        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)
            
    return requirements    

HYPHEN_DOT_E='-e .'
setup(
    name='Stroke-Disease-Prediction',
    version='0.0.0.0'
    author='BrianSiele',
    author_email='korosbrian574@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)