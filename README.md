# Project Lab 32: Permissions & Postgresql

Deployed on: [Link](https://github.com/kevinhenry/drf-api-permissions-postres)

PR: [Link](https://github.com/kevinhenry/drf-api-permissions-postgres/pulls)

Collaboration:
  Tony Regalado, Anthony Williams


## Overview

Let’s move our site closer to production grade by adding Permissions and Postgresql Database.


## Feature Tasks and Requirements

- You have been supplied with two demos, each presenting a key new feature.
    - `blogapi-permissions` demonstrates how to restrict access to portions of your APIs data.
    - `blogapi-postgres` demonstrates switching over to using `postgres` vs `sqlite`
- Your job is to merge the functionality of both demos.
- Customize your project to use different application features/models than `Blog` and `Post`


### Features - Django REST Framework

[ ] Make your site a DRF powered API as you did in previous lab.
[ ] Adjust project’s permissions so that only authenticated user’s have access to API.
[ ] Add a custom permission so that only author of blog post can update or delete it.
[ ] Add ability to switch user’s directly from browsable API.


### Features - Docker

* NOTE Refer to demo for built out `Dockerfile` and `docker-compose.yml` examples.
[x] create `Dockerfile` based off `python:3.8-slim`
[x] create `docker-compose.yml` to run Django app as a `web` service.
[x] enter `docker-compose up --build` to start your site.
[ ] add `postgres 11` as a service
    * Note: It is not required to include a volume so that data can persist when container is shut down.
[ ] Go to browsable api and confirm site properly restricts users based on their permissions.


## Implementation Notes

- You should NOT be running Postgres directly on host machine.
    - This means that operations like `createsuperuser` and `migrate` will need to happen inside the container.
    - For example…
        - docker-compose run web python manage.py migrate


### User Acceptance Tests:

[ ] Adjust any tests provided in demo to work with your project.


## Configuration

- Use poetry to create drf-api-permissions-postgres project.

    - poetry init -n

- Use the folder created by Poetry as the root of your project’s git repository.


## Stretch

[ ] Try different permission levels, including custom ones.
[ ] Figure out how to directly access postgres running inside container. Hint: it will take research.
[ ] Add a volume to persist data when container is shut down.


### Getting Started

Clone this repository to your local machine.

$ git clone [Link](https://github.com/kevinhenry/drf-api-permissions-postgres.git)
Once downloaded, activate your virtual environment and run by ____________

`poetry init`
`poetry shell`