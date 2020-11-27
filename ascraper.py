import argparse
import random
import time
import uuid
from multiprocessing import Process

import numpy as np
import requests as re

api_url = 'http://api.ascraper.com/crawl'
parser = argparse.ArgumentParser(description='aScraper api example')
parser.add_argument('--file', metavar='/path', type=str,
                    help='path to file with urls')
parser.add_argument('--selector', metavar='ul li', type=str,
                    help='css selector to search in html')
parser.add_argument('--user', metavar='API_KEY', type=str,
                    help='API_KEY from cabinet')
parser.add_argument('--cookie', metavar='id=1;', type=str,
                    help='Cookie string Chrome browser format')
parser.add_argument('--url', metavar='https://www.google.com', type=str,
                    help='URL to parse, FQDN format')
parser.add_argument('--session', metavar='123', type=str,
                    help='Session Id to persist cookies and headers')
parser.add_argument('--concurrent', metavar='11', type=str,
                    help='Concurrent threads')
args = parser.parse_args()


def cookies_from_string(cookie_string):
  cookie = []
  for c in cookie_string.split(" "):
    cookie.append(
        {'name': c.split("=")[0], 'value': c.split("=")[1].replace(";", "")})
  return cookie


def chunk_request(urls, user_id, selector, cookie_string):
  session = str(uuid.uuid4())
  for u in urls:
    try:
      single_request(user_id, selector, u.strip(), cookie_string, session)
    except:
      print("Exception with url: " + u)
    time.sleep(random.randint(2, 7))


def single_request(user_id, selector, url, cookie_string, session):
  headers = {
    'content-type': 'application/json'
  }
  request = {
    'userId': user_id,
    'render': 'false',
    'format': 'json',
    'url': url
  }
  if selector is not None:
    request['selector'] = selector

  if session is not None:
    request['session'] = session

  if cookie_string is not None:
    request['cookies'] = cookies_from_string(cookie_string)

  resp = re.post(api_url, json=request, headers=headers)
  code = resp.json()["status"]["codeNumber"]
  if code == 200:
    print("API call was successfully completed")
  else:
    print("API call error: " + str(code))
    exit()
  if selector is None:
    print(resp.json()["html_source"])
  else:
    print(resp.json()["source"])


if __name__ == "__main__":
  if args.user is None:
    print("user is not defined, see docs")
    parser.print_help()
    exit()

  if args.url is None and args.file is None:
    print("url of file with urls are not defined, see docs")
    parser.print_help()
    exit()

  if args.url:
    single_request(args.user, args.selector, args.url, args.cookie,
                   args.session)
  elif args.concurrent is not None and args.file is not None:
    with open(args.file) as urls:
      concurrent = int(args.concurrent)
      lines = urls.readlines()
      line_chunks = np.array_split(lines, concurrent)
      for chunk in line_chunks:
        Process(target=chunk_request, args=(chunk, args.user,
                                            args.selector,
                                            args.cookie)).start()
