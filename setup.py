from setuptools import find_packages,setup
from typing import List

DOT_E = "-e ."
def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements]

        if DOT_E in requirements:
            requirements.remove(DOT_E)

    return requirements



setup(
    name="Bitcoin_Prediction",
    version="0.0.1",
    author="Shreyash",
    author_email="shreyashchawda12@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()
)