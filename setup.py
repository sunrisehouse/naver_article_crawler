from setuptools import setup, find_packages

with open('requirements.txt', "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = 'naver_article_crawler',
    version = '0.0.1',
    description = 'naver article crawler',
    author = 'sunrisehouse',
    url="https://github.com/sunrisehouse/naver_article_crawler",
    packages=find_packages(),
    install_requires=requirements,
)
