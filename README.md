# DIS/PIS course example project

## Description
A basic example project for a DIS/PIS course.

## Installation
Create virtual environment:
```bash
python -m venv venv
```

Activate virtual environment:
```bash
# Windows
venv\Scripts\activate 
```
```bash
# Linux
source venv/bin/activate 
```

To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage

To run the project, run:
```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload 
```

or start venv and run:

```bash
python main.py
```

After that you can go to http://localhost:8000/docs to see the API documentation.


## Docker

To build the image, run:
```bash
docker build -t example-app-api .
```

Then run the image as container:
```bash 
docker run -p 8000:8000 dexample-app-api
```
