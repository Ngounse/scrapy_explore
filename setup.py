# Automatically created by: scrapyd-deploy

from setuptools import find_packages, setup

setup(
    name         = 'scrapy_explore',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = scrapy_explore.settings']},
    package_data = {'projectname': ['/home/ngounse/Desktop/learning/python/scrapy_explore/package.json']}
)
