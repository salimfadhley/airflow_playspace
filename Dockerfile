FROM python:3.6 AS base_python
ENV AIRFLOW_HOME=/airflow
RUN pip install --upgrade pip setuptools
RUN useradd -u 1000 airflow
RUN usermod -g sudo airflow
COPY . /project
WORKDIR /project/src
COPY ./home /airflow
RUN chown --recursive airflow:airflow /airflow
RUN mkdir /home/airflow
RUN chown --recursive airflow:airflow /home/airflow
VOLUME /airflow

FROM base_python AS airflow
WORKDIR /project/src
RUN SLUGIFY_USES_TEXT_UNIDECODE=yes python -m pip install -e /project/src
USER airflow
WORKDIR /airflow
EXPOSE 8080
