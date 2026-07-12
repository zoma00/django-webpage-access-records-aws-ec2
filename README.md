![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![Faker](https://img.shields.io/badge/Faker-FF6B6B)


Project Name: (Webpages Database Access Records)

Description:

This Python script populates a Django database with sample data for a website that might categorize web pages under various topics. It creates:

- Topics: 

Categories for webpages (e.g., Search, Social, Marketplace, News, Games)
- Webpages:

 Sample webpages with randomly generated URLs, names, and associated topics

- Access Records:
 Simulates user interactions with the webpages (date and user who accessed the webpage)

- Custom Users:
A set of fake users (optional, depending on your Django model setup)


## ☁️ AWS EC2 Deployment

This project was deployed to **AWS EC2** as a self-directed learning exercise on
a free-tier account — **not client work**. All resources were **terminated** and
all credentials **revoked** afterward (instance terminated, SSH key pair deleted,
IAM access keys revoked, and the account's payment method has since changed).

![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?logo=amazonec2&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?logo=gunicorn&logoColor=white)

See **[aws-deployment/](aws-deployment/README.md)** for the full write-up — IAM
users/roles and policies, EC2 provisioning, network/security-group settings,
Gunicorn, and secure SSH / SSM Session Manager access — with redacted
screenshots and deployment notes.


Prerequisites:

- Python 3 (tested with 3. x versions)
- Django framework (installation instructions: [https://docs.djangoproject.com/en/4.2/intro/install/](https://docs.djangoproject.com/en/4.2/intro/install/))
- `faker` library (`pip install faker`)

Installation:

1. Clone or download the repository.
2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv  # or your preferred virtual environment creation method
   source venv/bin/activate  # Activate the virtual environment (Linux/macOS)
   venv\Scripts\activate.bat  # Activate on Windows
   ```
3. Install required dependencies:

   ```bash
   pip install -r requirements.txt 
   ```
4. Copy your Django project's `settings.py` file to the root of this script's directory (modify `DJANGO_SETTINGS_MODULE` accordingly).

Usage:

1. Open a terminal or command prompt and navigate to the script's directory.
2. Run the script:
   ```bash
   python populate.py
   ```
   This will generate and populate the sample data.

Configuration (Optional):

- The script populates `N=5` topics and webpages by default. You can modify the value of `N` in the `populate` function to create a different number of entries.
- To include fake user generation and association with Access Records, uncomment the `create_fake_users` and user-related lines within the `populate` function.

- Consider adding a `requirements.txt` file to list dependencies for easier installation using `pip install -r requirements.txt`.

Further Customization:

- You can modify the `topics` list to reflect the specific categories relevant to your website.
- The script can be extended to generate more complex data or integrate with your Django models  if needed.

Testing:

- Ensure Django is running with your project's settings.
- Run the script and verify the generated data in your Django admin interface or database.

License:

(MIT License).

Contributing:

(Provide instructions on how others can contribute to your project, if applicable).

Readme.md:

Project Name**

**Introduction:**

A Python script for populating a Django database with sample data for a website  categorizes web pages.

Features:

- Generates topics (categories)
- Creates webpages with random URLs, names, and associations with topics
- Simulates user interactions with webpages (Access Records)
- Optionally generates fake users (if your Django model setup includes users)

Installation:

(Refer to the Installation section in the documentation)

Usage:

(Refer to the Usage section in the documentation)

Configuration:

(Refer to the Configuration section in the documentation)

Further Customization:

(Refer to the Further Customization section in the documentation)

Testing:

(Refer to the Testing section in the documentation)

License:

(Specify your preferred license)

Contributing:

## Contributing to (Webpages Database Access Records)

We welcome contributions from the community! Here's how you can get involved:

Bug Reports and Issues:

- If you encounter a bug or have an issue with the script, feel free to create a new issue on the project's GitHub repository. 
- Clearly describe the problem you're facing, including any error messages or unexpected behavior. 
- If possible, provide steps to reproduce the issue.

Feature Requests:

- If you have a suggestion for a new feature or enhancement, create a new issue on the repository. 
- Describe the proposed feature in detail, explaining its potential benefits and how it could be implemented.

Pull Requests:

- If you'd like to directly contribute code changes, consider creating a pull request. 
  - Fork the repository on GitHub.
  - Clone your forked repository to your local machine.
  - Make your changes to the code.
  - Test your changes thoroughly to ensure they don't introduce new issues.
  - Commit your changes with informative commit messages.
  - Create a pull request on the original repository, describing the changes you made and how they address an issue or add value.

General Guidelines:

- When submitting issues or pull requests, follow the issue template or pull request template provided on the repository (if available).
- Adhere to the project's coding style and conventions (if any). These might be documented in a style guide or evident from existing code.
- Write clear and concise code with comments explaining complex logic.
- Ensure your code is well-tested and doesn't break existing functionality.

Additional Notes:

- We appreciate contributions that are respectful and professional.
- We reserve the right to review and approve all contributions before merging them into the main codebase.

Thanks for your interest in contributing to (Webpages Database Access Records)!
