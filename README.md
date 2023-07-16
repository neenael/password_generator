# Password service
Service for password generating
## Endpoints
- [Get started](#get-started)
  - [Docker](#docker)
  - [Common installation](#common-installation)
## Get started
### Docker
This project contains a template Dockerfile for running Django applications in a Docker container.\
To use Docker in a Django project, you need to have Docker installed on your machine. You can download Docker Desktop on the official website\
Docker: https://www.docker.com/products/docker-desktop
1. Сopy the project from the repository:
```
git clone https://github.com/neenael/password_generator.git
```
2. Follow the project directory
```commandline
cd password_generator
```
3. Run the command below to pull Image from DockerHub
```commandline
docker pull neenael/password_project_image
```
4. Run the command below to run sercive
```commandline
docker run -p 8000:8000 --name passwords neenael/password_project_image
```
5. [Follow the localhost (127.0.0.1:8000)](http://127.0.0.1:8000)

### Common installation
1. Сopy the project from the repository:
```
git clone https://github.com/neenael/password_generator.git
```
2. Set up a virtual environment
```commandline
python -m venv venv
```
(Skip if alreadt exists)
```commandline
source venv/bin/activate
```
3. Install the requirements
```commandline
pip install django
```
4. Follow the project directory
```commandline
cd password_generator
```
5. Run migrations compilation
```commandline
python manage.py migrate
```
6. Execute the command to run local server
```commandline
python manage.py runserver
```
7. [Follow the localhost (127.0.0.1:8000)](http://127.0.0.1:8000)
