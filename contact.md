---
layout: default
title: Contact
---

# Contact Us

Get in touch with the TempGenie team.

---

## Contact Form

If you have any questions or need support, please fill out the form below, and we'll get back to you as soon as possible.

<form id="contact-form">
  <label for="name">Your Name:</label>
  <input type="text" id="name" name="name" required>

  <label for="email">Your Email:</label>
  <input type="email" id="email" name="email" required>

  <label for="message">Your Message:</label>
  <textarea id="message" name="message" rows="5" required></textarea>

  <button type="submit" class="btn">Send Message</button>
</form>

<script>
  // Contact form submission handler (for demonstration purposes)
  document.getElementById("contact-form").addEventListener("submit", function(event) {
    event.preventDefault();  // Prevent the form from submitting normally
    alert("Thank you for reaching out! We will get back to you soon.");
  });
</script>

---

## Alternative Communication

If you prefer, you can reach us through the following channels:

- **Email:** support@tempgenie.com
- **Slack:** [TempGenie Slack](https://slack.com)
- **Discord:** [TempGenie Discord](https://discord.com)
- **GitHub Discussions:** [GitHub Discussions](https://github.com/TempGenie/TempGenie/discussions)

---

&copy; 2024 TempGenie. All Rights Reserved.
