FROM python:3.6.6-alpine 
# Create app directory
RUN mkdir /app
WORKDIR /app
# Bundle app source
# Install app dependencies
COPY src/requirements.txt ./
COPY src /app
RUN pip3 install -r requirements.txt
EXPOSE 5080 
CMD ["python3", "/app/billBoard.py"]