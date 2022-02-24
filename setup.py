from distutils.core import setup


with open('README.md', 'r') as readmefile:
    readme = readmefile.read()


setup(
    name = 'backintime',
    version = '0.6.1.2',
    description = 'Trading strategies backtesting',
    author='Akim Mukhtarov',
    author_email = 'akim.int80h@gmail.com',
    url = 'https://github.com/akim-mukhtarov/backintime',
    packages = [
        'backintime',
        'backintime/backtester',
        'backintime/broker',
        'backintime/candles_providers',
        'backintime/candles_providers/binance_api_candles',
        'backintime/candles_providers/timeframe_dump',
        'backintime/market_data_analyzer',
        'backintime/market_data_storage',
        'backintime/oscillators',
        'backintime/timeframes_candle'
        ],
    install_requires = [
        'certifi==2021.10.8',
        'charset-normalizer==2.0.12',
        'idna==3.3',
        'numpy==1.22.2',
        'pandas==1.4.1',
        'python-dateutil==2.8.2',
        'pytz==2021.3',
        'requests==2.27.1',
        'six==1.16.0',
        'ta==0.9.0',
        'urllib3==1.26.8'
        ],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description_content_type='text/markdown',
    long_description=readme,
)
