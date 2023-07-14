#!/usr/bin/env python3

import cgi
import cgitb
import os
import boto3
import webbrowser

# Enable CGI error reporting
cgitb.enable()

# Create CGI form instance
form = cgi.FieldStorage()

# Print HTTP headers
print("Content-Type: text/html")
print()

# Print HTML response
print("<html>")
print("<head>")
print("<title>Automation Menu</title>")
print("</head>")
print("<body>")
print("<h1>Automation Menu</h1>")
print("<form method='POST' action=''>")
print("<label for='choice'>Select an option:</label>")
print("<select name='choice' id='choice'>")
print("<option value='1'>Running Basic Linux Commands</option>")
print("<option value='2'>Automating AWS Cloud using AWS-CLI</option>")

print("</select>")
print("<input type='submit' value='Submit'>")
print("</form>")

# Check user choice
if 'choice' in form:
    choice = form.getvalue('choice')

    if choice == '1':
        print("<h2>Running Basic Linux Commands</h2>")
        print("<form method='POST' action=''>")
        print("<label for='system'>Which system do you want to run the Linux commands on?</label>")
        print("<input type='radio' id='local' name='system' value='local'>")
        print("<label for='local'>Local</label>")
        print("<input type='radio' id='remote' name='system' value='remote'>")
        print("<label for='remote'>Remote</label>")
        print("<br>")
        print("<input type='text' id='ip' name='ip' placeholder='Enter remote system IP' style='margin-top: 5px;'>")
        print("<br>")
        print("<input type='text' id='command' name='command' placeholder='Enter command name' style='margin-top: 5px;'>")
        print("<br>")
        print("<input type='submit' value='Run Command'>")
        print("</form>")

    elif choice == '2':
        print("<h2>Automating AWS Cloud using AWS-CLI</h2>")
        print("<form method='POST' action=''>")
        print("<label for='aws_choice'>Select an AWS operation:</label>")
        print("<select name='aws_choice' id='aws_choice'>")
        print("<option value='1'>Creating a new key pair</option>")
        print("<option value='2'>Creating a security group</option>")
        print("<option value='3'>Launching a new EC2 instance in Mumbai region</option>")
        print("<option value='4'>Launching an EBS volume</option>")
        print("<option value='5'>Attaching an EBS volume to a launched instance</option>")
        print("<option value='6'>Creating an S3 bucket</option>")
        print("</select>")
        print("<br>")
        print("<input type='submit' value='Submit'>")
        print("</form>")

print("</body>")
print("</html>")
