from setuptools import setup, find_packages

setup(
    name = "dashbutton_daemon",
    version = "0.3",
    license = "GNU General Public License v3.0, 29 June 2007",
    author = "Dennis Jung, Dipl.-Ing. (FH)",
    author_email = "Dennis.Jung@it-jung.com",
    url = "https://github.com/gasperphoenix/DashbuttonDaemon",
    description = "This package provides a daemon that executes code if a dashbutton is pressed",
    package_dir = {"" : "src"},
    py_modules = ["dashbutton_daemon.DetectDashbutton", "dashbutton_daemon.DashbuttonDaemon"]
    )