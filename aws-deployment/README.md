# AWS EC2 Deployment & Cloud Administration

Deployment of the **Web Access Records** Django project to an AWS EC2 instance,
plus the account/IAM setup and secure instance management behind it.

> **Context:** This was a **self-directed learning exercise on a free-tier
> account — not client work.** All resources shown were **terminated** and all
> credentials **revoked** afterward: the EC2 instance was terminated, the SSH
> key pair deleted, IAM access keys revoked, and the account's payment method
> has since changed. Credentials in the CLI screenshots are additionally
> redacted. Nothing here is live.

## Deployment summary

| Item | Value |
|---|---|
| Project | Web Access Records (Django) |
| Instance | `i-082ffb6c3ae4b6bbb` — "Web-access-records" |
| OS / AMI | Ubuntu |
| Public IP | 13.53.86.62 (instance since terminated) |
| App server | Gunicorn |
| IAM user | `django_deployer` (EC2 + S3 access, later scoped down) |
| Access | SSH key pair + EC2 Instance Connect / SSM Session Manager |

## What this demonstrates

- **Account & identity security** — secured root with MFA; created an IAM user
  for deployment instead of using root for daily work.
- **IAM users, roles & policies** — created `django_deployer` with EC2/S3
  policies; created an EC2 instance role (`AmazonSSMManagedInstanceCore`) for
  Systems Manager; worked with policy inheritance.
- **AWS CLI** — installed and configured the CLI (`aws configure`) and drove
  IAM/EC2 from the command line.
- **EC2 provisioning** — launched an Ubuntu EC2 instance, created an RSA key
  pair, attached storage, and configured network/security-group settings.
- **Production app server** — added Gunicorn and prepared the Django project
  (static files, database, settings) for serving on the instance.
- **Secure access** — connected via SSH and via SSM Session Manager, which
  gives an audited shell without exposing SSH to the internet.

## Screenshots

| File | What it shows |
|---|---|
| `screenshots/01-iam-dashboard-root-mfa.png` | IAM dashboard: root MFA, account alias, no long-lived root keys |
| `screenshots/02-root-and-iam-user.png` | Root and IAM user consoles side by side |
| `screenshots/03-mfa-device-registered.png` | Virtual MFA device registered |
| `screenshots/04-aws-cli-configure-redacted.png` | `aws configure` + `aws iam list-users` (keys redacted) |
| `screenshots/05-aws-cli-iam-list-redacted.png` | AWS CLI IAM calls / access-key lifecycle (keys redacted) |

The **running instance** and **live SSM Session Manager terminal** are in the
screenshots at the repository root (Fleet Manager managed node, *Running /
Online*, and an active shell on the instance).

## Notes

Working notes from the deployment (`notes/`):

- `ec2-deployment-steps.txt` — end-to-end steps that were actually run
- `ec2-general-steps.txt` — overall deployment plan
- `ec2-network-settings.txt` — security-group / network configuration
- `ec2-ssh-connection.txt` — connecting to the instance
- `ec2-storage-capacity.txt` — instance storage
- `production-requirements-config.txt` — Gunicorn / production requirements
- `iam-policies.txt`, `policies-inheritance.txt`, `iam-console.txt`,
  `iam-password-policy.txt` — IAM setup notes
- `aws-cli-access-keys-redacted.txt` — AWS CLI access-key workflow (values redacted)
