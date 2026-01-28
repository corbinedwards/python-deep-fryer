# Python Deep Fryer
> [!WARNING]
> This script can create multiple images and override a directory with a certain naming convention.
> There is a prompt that asks if you want to replace the directory.

This script takes an image and applies a "deep fry" effect to it. This is done by applying harsh effects, saving a low quality JPG, then repeating multiple times.
Five different images are created for the user to choose from. 

## Examples
![1](https://github.com/user-attachments/assets/2ad10e2c-b2bf-4e31-8385-987f4468a92b)
![2](https://github.com/user-attachments/assets/b8531265-a394-48c2-a5b6-5111f4ca1c4d)
![3](https://github.com/user-attachments/assets/c817df2e-aec5-4d61-b2a3-46f4e8d01e5a)
![4](https://github.com/user-attachments/assets/c479dce2-289d-4a7b-b75a-8ebc2345a825)
![5](https://github.com/user-attachments/assets/24f7a7b7-5a65-48d3-9ccf-889a3a428823)

## Install/Running
This app requires Pillow, so once the repo is cloned you'll need to install the package in a local environment. There are a couple of ways:

Through [poetry](https://python-poetry.org/)
```
cd [repo path]
poetry install
poetry run python fry.py
```

Alternatively, you can set up a virtual environment and install Pillow through `requirements.txt`
```
cd [repo path]
python -m venv ./
./bin/pip install -r requirements.txt
./bin/python fry.py
```
