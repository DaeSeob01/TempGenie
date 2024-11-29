Configuration Guide
===================

This guide provides an overview of how to configure TempGenie to suit your needs.

1. **Configuration File Overview**

   TempGenie uses a ``config.py`` file to manage settings and customization options. The configuration file controls the following aspects:

   - The types of data to generate (e.g., names, emails, phone numbers).
   - The number of records to generate.
   - Optional custom settings for data formatting.

   You can find the ``config.py`` file in the root directory of the project.

2. **Available Configuration Options**

   Below are the available configuration options you can modify in ``config.py``:

   - **`data_types`**:
     - Controls which types of data are generated.
     - Options include:
       - ``'names'``: Generates random names.
       - ``'emails'``: Generates random email addresses.
       - ``'phones'``: Generates random phone numbers.
       - ``'addresses'``: Generates random addresses.
     - Example:

       .. code-block:: python

           data_types = ['names', 'emails', 'phones']

   - **``num_records``**:
     - Defines the number of records to generate.
     - Example:

       .. code-block:: python

           num_records = 1000

   - **``output_format``**:
     - Defines the output format of the generated data.
     - Options:
       - ``'csv'``: Save data as a CSV file.
       - ``'json'``: Save data as a JSON file.
     - Example:

       .. code-block:: python

           output_format = 'csv'

3. **Customizing Data Generation**

   You can add custom settings for data generation in the configuration file. For example, if you want to customize the random name generation logic, you can modify the ``generate_names()`` function in ``config.py``:

   .. code-block:: python

       def generate_names(num):
           # Custom name generation logic
           return ['Custom Name {}'.format(i) for i in range(num)]
