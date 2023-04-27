from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(filepath:str)->List[str]:
    requirements =[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(
name="House_rent",
version='0.0.1',
author="kaushal shukla",
author_email='kvushvl@gmail.com',
packages= find_packages(),
install_packeges=get_requirements("requirements.txt")

)