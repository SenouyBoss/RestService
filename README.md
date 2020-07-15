# RestService
REST microservice based on github api that gives top 100 trending Repositories with their programming languages count and their list of corresponding repositories.

The app is developped using python 3.6.4 along with the framework flask 1.1.2, docker 19.03.1 latest build and pycharm as IDE.

concept: the app request the data from github API of the trending 100 repos of the last 30 day (the date is manually typed in the source code feel free to change it to see different results). Then the application takes the date and manipulate it to extract the languages that these repos used. 
Creating 2 features: 
  - Display the languages and the number of all repositories that used from that 100 repos.
  - Display the languages and the list of the name of repositories that used it from the top 100 repos.
  
* To test the App:

Clone the git repository in your local machine.
run docker quickstart terminal (install from: https://docs.docker.com/toolbox/toolbox_install_windows/).
create an image based on the dockerfile in the repository.
to create an image run the following commands:
  - $ docker build -t <image_name>:latest <path to cloned project>
  - check if image is created: $ docker images
  - $ docker run -d -p 5000:5000 <image_name>:latest
  - check is image is running: $ docker ps (my image snapshot is in img/output)
 
After creating an image and running the container, it's time to test:
  - open local host in your machine @ '127.0.0.1:5000' to see index page
  - to test the first attribute: the number of repos using each language can be accessed in '127.0.0.1:5000/A1count/
  - the test the second attribute: the list of repos using each language can be accessed in '127.0.0.1:5000/A1list/

the output is in the form of a python dictionnary diplayed in a json format using python/flask libraries.

Image of the output: (see img/output folder)

- Index Page:
127.0.0.1 - - [15/Jul/2020 16:57:54] "←[37mGET / HTTP/1.1←[0m" 200 -

- First Attribute:
127.0.0.1 - - [15/Jul/2020 16:58:14] "←[37mGET /A1count HTTP/1.1←[0m" 200 -

- Second Attribute:
127.0.0.1 - - [15/Jul/2020 16:58:19] "←[37mGET /A1list HTTP/1.1←[0m" 200 -

