FROM openjdk:11-jdk

MAINTAINER GFG author


LABEL env=prod

ENV app /data/app

RUN mkdir -p $app

ADD https://get.jenkins.io/war/2.397/jenkins.war $app


WORKDIR $app 

EXPOSE 8080


CMD ["java", "-jar", "jenkins.war"]
