from distutils.core import setup

setup(
  name = 'lru_cache',
  packages = ['lru_cache'],
  version = '0.1',
  license='MIT',
  description = 'A simple implementation of LRU Caching algorithm.',
  author = 'Karan Maheshwari',
  author_email = 'kdmahesh@usc.edu',
  url = 'https://github.com/karan-maheshwari',
  download_url = 'https://github.com/karan-maheshwari/Simple-LRU-Implementation/archive/v_01.tar.gz',
  keywords = ['lru', 'cache', 'caching'],
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
