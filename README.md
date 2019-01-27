# Crawling, spiders, Scrapy?

## Practice

### Virtualenv

- Make a virtualenv

		mkvirtualenv --python=/usr/bin/python3 scrapy_test

- Install Scrapy and requirements

		pip install scrapy
		pip install requirements

- Create a new project and see what you get

		scrapy startproject techtalk

		.
		├── requirements.txt
		└── techtalk
		    ├── scrapy.cfg
		    └── techtalk
		        ├── __init__.py
		        ├── items.py
		        ├── middlewares.py
		        ├── pipelines.py
		        ├── __pycache__
		        ├── settings.py
		        └── spiders
		            ├── __init__.py
		            └── __pycache__



- Webs

	- https://www.knowyourinstrument.com/
	- https://www.ticketmaster.es (//div[contains(@class,"sc-2mfaq8-0")]//a[contains(text(),"Metal")])