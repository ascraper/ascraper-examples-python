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

Prepare the list of URL's. One row - one URL.
To run the code concurrently pass ``--concurrent`` flag with numbers of "threads" and the ``--file`` with path to the file with urls.

Code will devide the file to chunks based on ``--concurrent`` flag.

"Threads" will run simultaneously. *Be aware,* code has a random sleep from 2 to 7 in each thread. That was done to improve successful rate of crawling.

See details in *Best Practice* section.

```
python3 ascraper.py --user "xxxx" --file links.txt --concurrent 5 --selector title --cookie "yandexuid=7194876411567614048; yuidss=7194876411567614048; _ym_uid=1576853108917432489; mda=0; gdpr=0; _ym_d=1598867302; my=YwA=; yp=1599150048.yrts.1567614048#1599150048.yrtsi.1567614048#1601459301.ygu.1#1614635304.szm.2:1920x1200:1920x1041#1601545715.csc.1; i=W2fGtus3JV5gS29Hd1MrGBQXL74Q1vemmMJnhk19CQNA4KVJjsx8MFcUSFanu9R0yKkIxpTD1p0thV8ziZmH6Iomxtg=; ymex=1632553347.yrts.1601017347#1630992553.yrtsi.1599456553; is_gdpr=1; is_gdpr_b=CNnvZBCcBBgB; yabs-sid=382528651606310967; skid=6402682041606340377; sync_cookie_csrf=1707620066fake; _ym_visorc=b; _ym_isad=2"

```

# BEST PRACTICE
* Better few threads with sleep, but one fast thread

Try to simulate regular user if targed site is sensitive to crawling. Imagine that your code should moke a real user. So, make more slow users, but one fast.

* Use real cookies

Cookies will help you to simulate real user. Considering that crurl/wget and simple bots doesn’t have cookies on start - pass cookies from real browser.
It could help to skip some validations.
You can pass cookies and use the ``session``, API will persist cookies for 15 minutes. ``Set-Cookie`` header will be persisted to session too.

* Simulate real user behavior using session

To achieve more queality on scraping, try no to speedup crawling. Carefully calculate rates of crawler. 
Its a good decision to do requests before crawling target site, e.g. crawl google.com to obtain cookies in session mode and that crawl target site.

* Retry failed urls later
Better to cralw with non stopping behavior and than, later, re-crawl failed links
