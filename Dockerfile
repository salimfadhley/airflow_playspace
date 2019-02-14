FROM salimfadhley/testpython:latest AS base_python
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

FROM base_python AS application
WORKDIR /project/src
RUN SLUGIFY_USES_TEXT_UNIDECODE=yes python -m pip install -e /project/src
USER airflow
WORKDIR /airflow
