TempGenie API Documentation
============================

Welcome to the TempGenie API documentation. This document provides details on how to integrate TempGenie's features, including temporary email generation, phone number generation, and password generation, into your applications.

Official Links
--------------
- **ReadTheDocs Documentation**: `TempGenie Documentation <https://tempg.readthedocs.io/en/latest/>`_
- **GitHub Webpage**: `TempGenie GitHub Page <https://daeseob01.github.io/TempGenie/>`_

Overview
--------
The TempGenie API offers developers a programmatic way to utilize its features, such as generating temporary credentials for enhanced user privacy and security. With these endpoints, you can seamlessly integrate TempGenie's functionality into your platforms.

**Base URL**: ``https://api.tempgenie.io/v1``

Authentication
--------------
All API requests require an API key for authentication. This API key should be included in the request header.

**Authentication Header Example**:

.. code-block:: http

    Authorization: Bearer <your_api_key>

Endpoints
---------
Below are the main endpoints available in the TempGenie API:

Temporary Email
^^^^^^^^^^^^^^^

**Generate Temporary Email**

* **Endpoint:** ``/emails/generate``
* **Method:** GET
* **Response Example:**

.. code-block:: json

    {
        "email": "tempuser12345@tempmail.com"
    }

**Description**:
- This endpoint generates a temporary email address for one-time use, perfect for anonymous registration on websites.

Temporary Phone Number
^^^^^^^^^^^^^^^^^^^^^^

**Generate Temporary Phone Number**

* **Endpoint:** ``/phones/generate``
* **Method:** GET
* **Response Example:**

.. code-block:: json

    {
        "phone_number": "+1 201 1234-5678"
    }

**Description**:
- This endpoint provides a disposable phone number to use when verifying accounts or protecting your real phone number.

Temporary Password
^^^^^^^^^^^^^^^^^^^

**Generate Temporary Password**

* **Endpoint:** ``/passwords/generate``
* **Method:** GET
* **Parameters:**
    - ``length`` (optional): The length of the password (default is 12).

* **Response Example:**

.. code-block:: json

    {
        "password": "Ab3!xY9$kLm#"
    }

**Description**:
- This endpoint generates a strong, secure, and random password for account security.

Rate Limiting
-------------
- Maximum 100 requests per minute are allowed for all endpoints.
- Exceeding the rate limit will result in a ``429 Too Many Requests`` response.

Error Handling
--------------
The TempGenie API returns standard HTTP status codes to indicate the success or failure of an API request.

**HTTP Status Codes**:

* ``200``: Success
* ``400``: Bad Request
* ``401``: Unauthorized
* ``404``: Not Found
* ``429``: Too Many Requests
* ``500``: Internal Server Error

**Error Response Example**:

.. code-block:: json

    {
        "error": "invalid_request",
        "message": "The request parameters are invalid.",
        "code": "400"
    }

SDK and Library Support
-----------------------
TempGenie provides an official Python SDK for seamless integration. Community-contributed libraries are available for:

- JavaScript
- Ruby
- Go
- Java

Version History
---------------
* ``v1.0.0``: Initial release
* ``v1.1.0``: Added phone number generation
* ``v1.2.0``: Enhanced password generation with customizable length
* ``v1.3.0``: Added rate limiting and improved error handling

Feedback and Support
--------------------
For questions, issues, or feature requests, please visit our GitHub repository:

`TempGenie GitHub Page <https://daeseob01.github.io/TempGenie/>`_
