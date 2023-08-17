# start by pulling the python image
FROM public.ecr.aws/docker/library/python:slim-buster

# switch working directory
WORKDIR /app

# copy the requirements file into the image
COPY requirements.txt ./

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . .

# configure the container to run in an executed manner
EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
