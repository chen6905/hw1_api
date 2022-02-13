# Bookshelf API created with Python and Flask

## What is this?
This is a simple Python/Flask that imitates a bookshelf created for Homework 1 of CSCI3081W. 'Books' can be added to the bookshelf and can be removed at any time. The application will keep track of the action history and the current number of books in the Bookshelf. You can also view all books that is currently in the Bookshelf. 

## Pre-requisites
Note: This is only necessary if you are going to build the image yourself. Using it through docker pull will not need pre-requisites.
  * [Python](https://www.python.org/)
  * Install flask:

    ```bash
    pip install --no-cache-dir -r requirements.txt
    ```

## Running the web server

To run the server (if you somehow had the source files), use the following command in the command line:

  ```bash
  python server.py
  ```

The following is a list of available API commands:
  * GET - [http://127.0.0.1:1235/bookshelf/getBookshelf](http://127.0.0.1:8081/bookshelf/getBookshelf)
  * GET - [http://127.0.0.1:1235/bookshelf/getHistory](http://127.0.0.1:8081/bookshelf/getHistory)
  * GET - [http://127.0.0.1:1235/bookshelf/getBookNum](http://127.0.0.1:8081/bookshelf/getBookNum)
  * POST - [http://127.0.0.1:1235/bookshelf/add](http://127.0.0.1:8081/bookshelf/add)
  * POST - [http://127.0.0.1:1235/bookshelf/remove](http://127.0.0.1:8081/bookshelf/remove)

In order to invoke them, please use POSTMAN, CURL, or any other program that you like. The GET commands can be called through the URL in a browser directly, but the POST commands will require some program to send JSON formatted data.

The **add** command takes in the two following input:
* *title* 
* *author* 

Here is an example call for POSTMAN (should be applicable for other programs):
* The API command - http://127.0.0.1:1235/bookshelf/add
* Body - {"title": "test3", "author": "aaron"}

The **remove** command will be similar to the add function, but it will only require the *title* as data.

## How to use this via Docker?
1. Pull the Bookshelf image using the following command
    ```bash
    docker pull jkl2953/hw1_api
    ```
2. Run the image using the following command:
    ```bash
    docker run -p 127.0.0.1:1235:8081 -it jkl2953/hw1_api
