# Automatically created by: scrapyd-deploy

from setuptools import find_packages, setup

setup(
    name         = 'scrapyproject',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = scrapy_explore.settings']},
)
