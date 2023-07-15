# Using lightweight alpine image
FROM python:3.11-alpine

# Installing system dependencies
RUN apk update && \
    apk add --no-cache build-base

# Installing Pipenv
RUN pip install --no-cache-dir pipenv

# Defining working directory and adding source code
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock ./
COPY nba_stat_track ./nba_stat_track
COPY bootstrap.sh ./

# Set Python version for Pipenv
ENV PIPENV_PYTHON=/usr/local/bin/python

# Install API dependencies
RUN pipenv install --system --deploy

# Start app
EXPOSE 5001
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]
