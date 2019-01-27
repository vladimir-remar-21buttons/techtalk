# Crawling, spiders, Scrapy?

## Practice

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

	- https://www.eventbrite.com/d/spain--barcelona/events/
	- https://www.knowyourinstrument.com/