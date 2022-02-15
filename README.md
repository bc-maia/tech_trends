# TechTreds Web Application

This is a Flask application that lists the latest articles within the cloud-native ecosystem.

## Run

To run this application there are 2 steps required:

1. Initialize the database by using the `python init_db.py` command. This will create or overwrite the `database.db` file that is used by the web application.
2. Run the TechTrends application by using the `python app.py` command. The application is running on port `3111` and you can access it by querying the `http://127.0.0.1:3111/` endpoint.

## _Dockerizing_ The App

- [Dockerfile](./Dockerfile)
- [Docker Commands](./docker_commands.md)

## Github Actions

This project uses [Github Actions](https://docs.github.com/en/actions/publishing-packages/publishing-docker-images) to deploy it's image to dockerhub.

- Check [techtrends-dockerhub.yml](./.github/workflows/techtrends-dockerhub.yml)
