[![Publish to Docker](https://github.com/ruben69695/personalweb/actions/workflows/deploy.yml/badge.svg)](https://github.com/ruben69695/personalweb/actions/workflows/deploy.yml)
![GitHub](https://img.shields.io/github/license/ruben69695/personalweb?color=purple)
![GitHub last commit](https://img.shields.io/github/last-commit/ruben69695/personalweb)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/ruben69695/personalweb?color=purple)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ruben69695/personalweb?color=purple)

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%203.svg)](https://www.digitalocean.com/?refcode=e212aaa8b0c3&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge) 

# Personal Web
My personal and professional web made with Python, Django, PostgreSQL and deployed on Digital Ocean cloud platform in a PaaS.
Take a look at my page on [rubenarrebola.pro](https://www.rubenarrebola.pro) 😎

## Requirements
1. Docker and Docker Compose installed on your machine
2. Python, Django and PostgreSQL knowledge

## Getting started
1. Clone the repository
```bash
git clone https://github.com/ruben69695/personalweb.git
```
2. Open the root of the project in your terminal
```bash
cd personalweb
```
3. Export in your system environment a new secret key necessary for docker compose, you can [generate a new one](https://djecrety.ir/)
```bash
export DJANGO_SECRET_KEY="Your new secret key goes here"
```
3. Build and stand up the services using docker compose
```bash
docker compose up --build -d
```
4. Now [open your browser](http://127.0.0.1:8000/)
5. Easy and enjoy 🍻

## Languages and versions
- Python 3.9.13
- Django 4.0.4
- pip 20.3.4
- Postgresql 14.3

## Development environment
- Debian Bullseye 11
- VSCodium v1.86.0
- NVIM v0.4.4

## Architecture
- Server - Client

## Production Deployment
- Heroku Platform
- Digital Ocean

## Runs on
- Linux
- MacOS
- Windows
- Docker
