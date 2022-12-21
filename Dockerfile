FROM python:3.7
EXPOSE 8080
MAINTAINER /Dockerfile
copy sample_email ./
CMD ["python","./sample_email.py"]
