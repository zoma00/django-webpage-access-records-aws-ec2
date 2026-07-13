[![CI](https://github.com/zoma00/django-webpage-access-records-aws-ec2/actions/workflows/ci.yml/badge.svg)](https://github.com/zoma00/django-webpage-access-records-aws-ec2/actions/workflows/ci.yml)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![Faker](https://img.shields.io/badge/Faker-FF6B6B)


# Webpages Database Access Records

A Django 5.2 application for organizing webpages by topic and recording which users accessed
them. The included Faker-based population script creates:

- Topic categories such as Search, Social, Marketplace, News, and Games
- Webpages with generated names and URLs
- Custom users
- Dated access records linking users to webpages

## ☁️ AWS EC2 Deployment
![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?logo=amazonec2&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?logo=gunicorn&logoColor=white)

This project was deployed to **AWS EC2** as a self-directed learning exercise on
a free-tier account — **not client work**. All resources were **terminated** and
all credentials **revoked** afterward (instance terminated, SSH key pair deleted,
IAM access keys revoked, and the account's payment method has since changed).



See **[aws-deployment/](aws-deployment/README.md)** for the full write-up — IAM
users/roles and policies, EC2 provisioning, network/security-group settings,
Gunicorn, and secure SSH / SSM Session Manager access — with redacted
screenshots and deployment notes.


## Prerequisites

- Python 3.11 or newer
- Django 5.2

## Installation

1. Clone or download the repository.
2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv  # or your preferred virtual environment creation method
   source venv/bin/activate  # Activate the virtual environment (Linux/macOS)
   venv\Scripts\activate.bat  # Activate on Windows
   ```
3. Install required dependencies:

   ```bash
   cd first_pro
   pip install -r requirements.txt
   ```
4. Set local environment values and create the database:

   ```bash
   export DJANGO_SECRET_KEY="replace-with-a-local-development-key"
   export DJANGO_DEBUG=True
   export DJANGO_ALLOWED_HOSTS="localhost,127.0.0.1"
   python manage.py migrate
   ```

## Usage

Generate sample data and start the development server:

```bash
python populate.py
python manage.py runserver
```

## Configuration

- The script populates `N=5` topics and webpages by default. Modify `N` in `populate()` to
  create a different number of entries.
- `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, and `DJANGO_ALLOWED_HOSTS` control environment-specific Django settings.

## Further Customization

- You can modify the `topics` list to reflect the specific categories relevant to your website.
- The script can be extended to generate more complex data or integrate with additional Django
  models.

## Testing and CI

From the repository root, run the same checks used by GitHub Actions:

```bash
python -m pip install -r requirements-ci.txt
ruff check first_pro
cd first_pro
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test -v 2
```

The test suite creates a temporary database, applies every migration, and verifies custom-user,
model, relationship, cascade, ordering, view, and empty-state behavior. No AWS resources are
required.

## License

[MIT](LICENSE)

## Contributing to Webpages Database Access Records

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

Thanks for your interest in contributing to Webpages Database Access Records!
