# FileWebApp

1 install dcocker

	sudo yum update -y
	
	sudo yum install -y docker

	sudo service docker start
	
	sudo usermod -a -G docker ec2-user


2 install git and clone code

	sudo yum install -y git

	git clone https://github.com/awslabs/ecs-demo-php-simple-app



3 pull docker image for django (uwsgi) & nginx) from docker hub:

	docker pull mbentley/django-uwsgi-nginx

4 mount code to docker container

	# Example usage:

	docker run -p 80 -d -e MODULE=myapp mbentley/django-uwsgi-nginx

	# You can mount the application volume to run a specific application. 
	# The default volume inside in the container is /opt/django/app. Here is an example:

	docker run -p 80 -d -e MODULE=myapp -v /home/mbentley/myapp:/opt/django/app mbentley/django-uwsgi-nginx

	#By default, this just runs a default 'welcome to django' project.
