# WDMM1405-Flask
Multimedia Programming II - WDMM1405 (Python Programming II) - Flask Examples source code

## Course web page 
https://mksaad.wordpress.com/2019/02/05/python-ii-wdmm1405/

## Github for the first part of the course source code 
https://github.com/motazsaad/WDMM1405

## Installation 
`pip install flask`

---
# Part 1 
## Introduction to Flask

[Flask](http://flask.pocoo.org/) is a micro web framework powered by Python. It's API is fairly small, making it easy to learn and simple to use. But don't let this fool you, as it's powerful enough to support enterprise-level applications handling large amounts of traffic. You can start small with an app contained entirely in one file, then slowly scale up to multiple files and folders in a well-structured manner as your site becomes more and more complex. 

## Contents 
Setting up a basic project structure then developing a static site, styled with Bootstrap. 

## get the bootstrap
https://getbootstrap.com/ 

Take the following files 

* bootstrap.min.css
* bootstrap.min.js   

### advantage 

* Makes your website responsive
* improve the style of your website  

## HTTP messages code

* 200 OK 
* 404 not found 
* 500 server error  

## HTTP Methods 

* GET: get resource from server (html page, jpg image, pdf file, ...etc) 
* POST: send data to server. Usually used with html forms 

---
# Mater template (template inheritance)

design master template and reuse it

---

## Deal with Databases (SQLite) 
SQL: Structured Query Language

Lite == Light ==  

Database: set of related tables 

retrieve date from a single table

### Tool
Sqlite Browser

---

## Build REST API using Python and Flask 

API = Application Program Interface

Developers use API to build applications

Common Example: The weather App

Ordinary Flask app pages return a string or html. There is a need for standard format to extract result from it. It is JSON format

JSON == JAVA Simple Object Notation == Python Dictionary      

### Options 
* Option 1: Basic Flask (Jsonify function) 
* Option 2: Flask-RESTful (pip install Flask-RESTful)


 
## References 

https://github.com/realpython/discover-flask