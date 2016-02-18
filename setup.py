import re
import subprocess

from setuptools import setup


def _get_git_description():
    try:
        return subprocess.check_output(["git", "describe"]).decode("utf-8").strip()
    except subprocess.CalledProcessError:
        return None


def get_version():
    description = _get_git_description()

    match = re.match(r'(?P<tag>[\d\.]+)-(?P<offset>[\d]+)-(?P<sha>\w{8})', description)

    if match:
        version = "{tag}.post{offset}".format(**match.groupdict())
    else:
        version = description

    return version


def main():
    setup(
        name="open-repo",
        url="https://github.com/DoWhileGeek/open-repo",
        description="A command line utility for opening a repositories remote homepage.",
        author="Joeseph Rodrigues",
        author_email="dowhilegeek@gmail.com",
        version=get_version(),
        scripts=["open-repo"]
    )


if __name__ == "__main__":
    main()
