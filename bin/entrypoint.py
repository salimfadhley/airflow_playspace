#! /usr/ocal/bin/python
import os
import subprocess

def main():
    airflow_home_dir = os.environ.get("AIRFLOW_HOME")
    airflow_config_file = os.path.join(airflow_home_dir, "airflow.cfg")

    if os.path.exists(airflow_config_file):
        print(f"Installing Airflow to {airflow_home_dir}.")
    else:
        print(os.listdir(airflow_home_dir))
        print("Airflow is already installed, skipping initialization.")

    # airflow initdb
    #
    # aiflow webserver -p 8080
    #
    # ls -l ${airflow_home_dir}
    #
    # airflow scheduler



if __name__ == "__main__":
    main()