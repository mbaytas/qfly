from setuptools import setup

setup(
    name="qfly",
    description="Qualisys Drone SDK",
    version=0.2,
    url="https://github.com/qualisys/qualisys_drone_sdk",
    license="MIT",
    install_requires=['qtm_rt', 'cflib', 'pynput', 'scipy'],
    packages=["qfly"],
    author="Qualisys AB",
    author_email="support@qualisys.com",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
    ],
    python_requires=">=3.9",
)