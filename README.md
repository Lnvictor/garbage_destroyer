# garbage_destroyer

[![Garbage destroyer](https://github.com/Lnvictor/garbage_destroyer/actions/workflows/python-app.yml/badge.svg)](https://github.com/Lnvictor/garbage_destroyer/actions/workflows/python-app.yml)


Garbage destroyer is a project made for cleaning old files in a specif directory, that is specified by the user.
The app is a scheduled job, the job recurrency is also parametrized.

---

## Setup

I used poetry as a dependency management tool, so you can the project dependencies with:
```shell
    poetry update
```

Or, if your want just use pip, you can run:
```
    pip install -r requirements.txt
```

## Running as a Scheduled job
You need create a config file called **config.ini** in project root, in order to add some required settings to run the application:

- Config sections:
    -  Scheduler: Config for scheduling the applcation running times, for example:

        ```ini
            [Scheduler]
            day=*
            hour=*
            minute=0
        ```
    With this configuration, the application will be scheduled to run every day and every hour at the minute 0.

    - Cleaning: This one is for cleaning parameters:

        ```ini
        [Cleaning]
            dir=/Users/victorpereira/Downloads
            time_diff_in_days=1
            file_extension=jpg
        ```
---

## How to run
```python
    python app.py
```

## How to run as cli application
run the following commands
```python
chmod +x setup.sh
./setup.sh
```
Then, you can run
```sh
./gds --help
```

Have fun :octopus:

---

## References

- [Apsscheduler Official docs](https://apscheduler.readthedocs.io/en/3.x/)
- [Python official docs for configparser](https://docs.python.org/3/library/configparser.html)