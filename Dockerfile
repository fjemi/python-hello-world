# Initialize a Python image
FROM python:3.8-alpine

# Add file to the image filesystem at a path
ADD helloworld.py /

# Additional commands to execute image
RUN pip install pipenv
RUN pipenv install

# Execute commands when the image loads
CMD ['python', './helloworld.py']
