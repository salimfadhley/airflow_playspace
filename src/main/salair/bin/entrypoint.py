#! /usr/local/bin/python
import os

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME")

SETUP_FLAG_PATH = os.path.join(AIRFLOW_HOME, "setup_complete")


def run_airflow_setup():
    print("Running Airflow setup")


def touch(SETUP_FLAG_PATH:str):
    pass


def main():
    if not os.path.exists(SETUP_FLAG_PATH):
        run_airflow_setup()
        touch(SETUP_FLAG_PATH)


if __name__ == "__main__":
    main()