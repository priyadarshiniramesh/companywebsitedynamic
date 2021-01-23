# Dynamic Website Design for a Manufacturing Company
## AIM:
To design a dynamic website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAM:

### base.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>PRIYA PRIVATE LIMITED</title>
    <link rel="stylesheet" href="{% static 'css/company.css' %}">
   
    <link rel = "icon" href ="{% static 'image/titleicon.jpg' %}" type = "image/x-icon"> 
              
</head>

<body>
    <div class="container">
    <div class="banner">
       <b>SILICON PRIVATE LIMITED</b>
    </div>
    <div class="menu">
        <b><div class="menuitem"><a href="/home">Home</a></div></b>
        <b><div class="menuitem"><a href="/product">Products</a></div></b> 
        <b><div class="menuitem"><a href="/people">People</a></div></b>
        <b><div class="menuitem"><a href="/contactus">Contact Us</a></div></b>
    </div><div class="content">
    {% block content %}    
    {% endblock  %}
    </div>
    <div class="footer">
        <b>Copyright © 2020 Silicon Private Limited, Developed by PRIYADARSHINI</b>
    </div>
    </div>
</body>

```

### home.html 
```

{% extends "companywebsite/base.html" %}

{% block content %}
    <div class="homecontent">    
    <h1><b>ABOUT US </b></h1>
    <img src="/static/image/company.jpg">
    <div class="contenttext">
    <b>Silicon Pvt Ltd, provides a broad range of semiconductor and infrastructure software applications that serve the data center, networking, software, broadband, wireless, and storage and industrial markets. Common applications for its products include: data center networking, home connectivity, broadband access, telecommunications equipment, smartphones, base stations, data center servers and storage, factory automation, power generation and alternative energy systems, displays, and mainframe operations and management, and application software development. Some of Silicon's core technologies and products include:</b>
    <ul>
        <b><li>Memory Chips</li></b>
        <b><li>SATA HDD</li></b>
        <b><li>SATA SSD </li></b>
        <b><li>Broadband Modems</li></b>
        <b><li>Wifi Devices</li></b>
        <b><li>Switching Devices</li></b>
        <b><li>Optical Sensors</li></b>
    </ul> 
    </div>
    </div>
{% endblock  %}
```

### product.html
```
{% extends "companywebsite/base.html" %}

{% block content %}
    <div class="productcontent">    
    <h1>Our Premium Products</h1>
    <div class="productitems">
        {% for product in products %}
        <div class="productitem"> 
            <div class="itemimage">
            <img src="{{ product.photos.url }}" alt="product image">
            </div>
            <div class="itemname">{{product.Name}}</div> 
            <div class="itemprice">Price : {{product.Price}}</div>
        </div>
        {% endfor %}
        
         
    </div>
    </div>
{% endblock  %}

```
### people.html
```
{% extends "companywebsite/base.html" %}

{% block content %}


<div class="productcontent">    
    <h1>PEOPLES</h1>
    <div class="productitems">
    {% for people in peoples %}
        <div class="productitem"> 
            <div class="itemimage">
            <img src="{{ people.photo.url }}" alt=" product image">
            </div>
            <div class="itemname">{{ people.Name }}</div>
            <div class="itemprice">{{ people.Designation }}</div>
        </div>
    {% endfor %}
    </div>
</div>

{% endblock  %}

```
### contactus.html
```
{% extends "website/base.html" %}

{% block content %}

    <div class="contactcontent">    
    <h1>CONTACT US</h1>
    <div class="contactlists">
        <div class="contactlist"> 
            <h1> GEMMA (SALES MANAGER)</h1>
            <h2>ADDRESS : KG Campus, 365, Thudiyalur Rd, Saravanampatti, Keeranatham, Tamil Nadu, India - 641035</h2>
            <h3>PHONE :0422 - 441 9999</h3>
            <h4>EMAIL : siliconlimited@gmail.com</h4>
        </div>
    </div>
    </div>

{% endblock  %}

```
## OUTPUT:

![output](./static/image/out 1.jpg)
![output](./static/image/out 2.jpg)
![output](./static/image/out 3.jpg)
![output](./static/image/out 4.jpg)

## VALIDATION REPORT 

![output](./static/image/home.jpg)
![output](./static/image/product.jpg)
![output](./static/image/people.jpg)
![output](./static/image/contact.jpg)



## RESULT:

         Thus a website is designed for the chip manufacturing company and is hosted in thr URL http://priyadarshini.student.saveetha.in:8000/ .HTML code is validate.