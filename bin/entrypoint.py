#! /usr/ocal/bin/python
import os
import subprocess
import sys

import click

AIRFLOW_COMMAND = "/usr/local/bin/airflow"

@click.command()
@click.argument("mode")
@click.option("--port", type=int, default=8080)
def main(mode:str, port:int):
    if mode=="webserver":
        command = f"{AIRFLOW_COMMAND} webserver -p {port}"
    elif mode in {"scheduler", "worker"}:
        command = f"{AIRFLOW_COMMAND} {mode} --help"
    else:
        raise RuntimeError(f"Invalid mode: {repr(mode)}")

    airflow_home_dir = os.environ.get("AIRFLOW_HOME")
    airflow_config_file = os.path.join(airflow_home_dir, "airflow.cfg")

    if not os.path.exists(airflow_config_file):
        print(f"Installing Airflow to {airflow_home_dir}.")
        subprocess.call(f"{AIRFLOW_COMMAND} initdb", shell=True)
    else:
        print(os.listdir(airflow_home_dir))
        print("Airflow is already installed, skipping initialization.")



    sys.exit(subprocess.call(command, shell=True))


if __name__ == "__main__":
    main()