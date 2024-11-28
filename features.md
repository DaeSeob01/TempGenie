---
layout: default
title: Features
---

# TempGenie Features

Generate temporary credentials: emails, phone numbers, and passwords with ease.

## Features

### Generate Temporary Email
This feature allows you to generate a temporary email address for one-time use, perfect for registering on websites without revealing your personal email.

<button class="btn" onclick="generateTempEmail()">Generate Temporary Email</button>
<div class="output" id="temp-email-output"></div>

### Generate Temporary Phone Number
This feature provides a disposable phone number for temporary use, helping protect your privacy when verifying accounts online.

<button class="btn" onclick="generateTempPhoneNumber()">Generate Temporary Phone Number</button>
<div class="output" id="temp-phone-output"></div>

### Generate Temporary Password
Create strong and secure passwords with the click of a button. This feature suggests a random, complex password for your accounts.

<button class="btn" onclick="generateTempPassword()">Generate Temporary Password</button>
<div class="output" id="temp-password-output"></div>

## Scripts

Add the following JavaScript functions in your `_includes` folder or directly in the layout file to ensure functionality.

```html
<script>
  // Function to generate a temporary email
  function generateTempEmail() {
    const domain = "@tempmail.com";
    const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    let email = "tempuser";
    for (let i = 0; i < 10; i++) {
      email += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    email += domain;
    document.getElementById("temp-email-output").innerText = "Your temporary email: " + email;
  }

  // Function to generate a temporary phone number
  function generateTempPhoneNumber() {
    const countryCodes = ["+1", "+44", "+91", "+49", "+33"];
    const areaCodes = ["201", "305", "415", "646", "323"];
    const randomCountry = countryCodes[Math.floor(Math.random() * countryCodes.length)];
    const randomArea = areaCodes[Math.floor(Math.random() * areaCodes.length)];
    const phoneNumber = `${randomCountry} ${randomArea} ${Math.floor(Math.random() * 10000)}-${Math.floor(Math.random() * 10000)}`;
    document.getElementById("temp-phone-output").innerText = "Your temporary phone number: " + phoneNumber;
  }

  // Function to generate a temporary password
  function generateTempPassword() {
    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()";
    let password = "";
    for (let i = 0; i < 12; i++) {
      password += chars.charAt(Math.floor(Math.random() * characters.length));
    }
    document.getElementById("temp-password-output").innerText = "Your temporary password: " + password;
  }
</script>
