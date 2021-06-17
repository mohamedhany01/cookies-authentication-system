# Cookies Authentication System
A simple authentication system using HTTP cookies, built with Flask.

***
<h2><strong>
```diff
- WARNING -
```
</strong></h2>
<p>The <strong>HTTP Cookies</strong> are not safe to store sensitive data like usernames and passwords.</p>
<p>They have vulnerabilities and easy to capture by hackers, because they are a client-side based.</p>
<p>This is a simple example, for using cookies, don't use this example in the production environment.</p>

***

## Introduction

* ##### What is the **HTTP**?
    You probably have heard before about it's a protocol. But what is a protocol?

    A protocol is a way of commutation between an entity/person/thing and another.

    So, HTTP is a way to communicate, but between what?!

    Simply, HTTP is a data transport protocol between a client and a server in the client-server architecture with request and respond cycle. It's an architecture used heavily in web development.

    HTTP developers designed HTTP with flexibility and scalability in mind. We will see how in the next section.

* ##### What are **HTTP cookies**?
    Although HTTP is a robust protocol, it works with each request as an initial "stateless". In other words, it doesn't know who do send these requests. Fortunately, HTTP developers added the cookies feature to HTTP to overcome that problem.

    Cookies are simple pieces of data "key-value pairs", the server creates them and sends them to the browser, the browser store them takes them locally, and in each request, it sends them all to the server.

    Using this method, the server/developers can identify requests easily and build customized decisions for each request

## Background
So, why I built an authentication system using HTTP cookies, although they aren't a secure way to store sensitive data.
Well, I am just trying to understand cookies by using them in a mechanism that has a logic like an authentication mechanism. In production don't use cookies to store sensitive data.

## Technologies
To build this project I used **HTML**, **CSS**, **Python 3/Flask 2**, **jinja2**.

## Installation
To use this project just **clone** it or **download** it directly and start with the **127.0.0.1:port_number/homepage**. Be sure to use the latest version of Firefox, Chrome, Opera, Edge, or any other modern browsers.
