from setuptools import setup

setup(name='v4dark',
      version='0.11',
      description='super fancy discord bot',
      packages=['v4dark'],
      install_requires=['colorlog',
      'discord.py',
      'python-dotenv',
      'beautifulsoup4',
      'lxml',
      'requests'
      ],
      zip_safe=False)
