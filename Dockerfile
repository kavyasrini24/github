FROM openjdk
WORKDIR /app
COPY . /app
RUN sample.java
CMD ["java","sample"]
