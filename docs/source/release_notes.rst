Release Notes
=============

The following is a summary of the changes made in each release of TempGenie. This section provides a detailed history of updates, new features, bug fixes, and improvements.

v1.0.0 (2024-11-28)
-------------------
- **Initial Release**
  - Introduced TempGenie, a tool for generating temporary data for testing and development purposes.
  - Features include:
    - Data generation for emails, phone numbers, and other temporary information.
    - Simple command-line interface (CLI) for generating random data.
    - Easy configuration and extension options for customization.

v1.1.0 (2024-12-05)
-------------------
- **New Features**:
  - Added support for generating random addresses.
  - Included a configuration file for advanced users to customize data formats and types.
  
- **Improvements**:
  - Optimized data generation algorithms for faster processing.
  - Updated the documentation to include detailed usage examples.

- **Bug Fixes**:
  - Fixed an issue with email generation where invalid email addresses were being created under certain conditions.

v1.2.0 (2024-12-12)
-------------------
- **New Features**:
  - Added support for generating temporary credit card numbers.
  - Introduced new randomization options for more flexible data generation.

- **Improvements**:
  - Refined the random data generation algorithms to improve randomness and uniqueness.
  - Enhanced the CLI for better user interaction and error handling.

- **Bug Fixes**:
  - Resolved an issue where the application failed to generate data for specific locales.

v1.3.0 (2024-12-18)
-------------------
- **New Features**:
  - Added a web-based user interface for data generation.
  - Implemented an API for programmatic access to data generation functionalities.
  
- **Improvements**:
  - Improved the performance of the API and CLI, reducing response times and resource consumption.
  
- **Bug Fixes**:
  - Fixed a bug causing the application to crash when generating large datasets.
  - Addressed a minor issue where the application failed to handle special characters in input fields.

How to Upgrade
--------------
To upgrade to the latest version of TempGenie, follow these steps:

1. **Upgrade via pip**:
   
   .. code-block:: bash
       pip install --upgrade tempgenie
