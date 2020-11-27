# ascraper-examples-python
How to parse with aScraper API. Example on Python

## Installation

### Requirements

To work with example you need python v3

``pip3 install -f requirements.txt``


### Preparing requests

To simulate real user you need real ``cookies``.

1. Open Developer Console in Chrome browser
2. Navigate to target site
3. Copy paste ``Cookie`` string
4. Pass this string to ``python script`` using ``--cookie`` flag to convert string row to map

### Ussage

```
usage: ascraper.py [-h] [--file /path] [--selector ul li] [--user API_KEY]
                   [--cookie id=1;] [--url https://www.google.com]
                   [--session 123] [--concurrent 11]

aScraper api example

optional arguments:
  -h, --help            show this help message and exit
  --file /path          path to file with urls
  --selector ul li      css selector to search in html
  --user API_KEY        API_KEY from cabinet
  --cookie id=1;        Cookie string Chrome browser format
  --url https://www.google.com
                        URL to parse, FQDN format
  --session 123         Session Id to persist cookies and headers
  --concurrent 11       Concurrent threads
```

### Multithreading
```
python3 ascraper.py --user "xxxx" --file links.txt --concurrent 5 --selector title --cookie "yandexuid=7194876411567614048; yuidss=7194876411567614048; _ym_uid=1576853108917432489; mda=0; gdpr=0; _ym_d=1598867302; my=YwA=; yp=1599150048.yrts.1567614048#1599150048.yrtsi.1567614048#1601459301.ygu.1#1614635304.szm.2:1920x1200:1920x1041#1601545715.csc.1; i=W2fGtus3JV5gS29Hd1MrGBQXL74Q1vemmMJnhk19CQNA4KVJjsx8MFcUSFanu9R0yKkIxpTD1p0thV8ziZmH6Iomxtg=; ymex=1632553347.yrts.1601017347#1630992553.yrtsi.1599456553; is_gdpr=1; is_gdpr_b=CNnvZBCcBBgB; yabs-sid=382528651606310967; skid=6402682041606340377; sync_cookie_csrf=1707620066fake; _ym_visorc=b; _ym_isad=2"

```

# BEST PRACTICE
* Better maythreads with sleep, but one fast thread
...
* Use real cookies
...
* Simulate real user behavior using session
...
* Retry failed urls later
