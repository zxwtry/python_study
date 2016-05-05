#!/usr/bin/python
# -*- coding:utf-8 -*-

import os,sys,urllib,urllib2,urlparse
from sgmllib import SGMLParser 

img = []
class URLLister(SGMLParser):
  def reset(self):
    SGMLParser.reset(self)
    self.urls=[]
    self.imgs=[]
  def start_a(self, attrs):
    href = [ v for k,v in attrs if k=="href" and v.startswith("http")]
    if href:
      self.urls.extend(href)
  def start_img(self, attrs):
    src = [ v for k,v in attrs if k=="src" and v.startswith("http") ]
    if src:
      self.imgs.extend(src)


def get_url_of_page(url, if_img = False):
  urls = []
  try:
    f = urllib2.urlopen(url, timeout=1).read()
    url_listen = URLLister()
    url_listen.feed(f)
    if if_img:
      urls.extend(url_listen.imgs)
    else:
      urls.extend(url_listen.urls)
  except urllib2.URLError, e:
    print e.reason
  return urls

#recursion
def get_page_html(begin_url, depth, ignore_outer, main_site_domain):
  #other sites
  if ignore_outer:
    if not main_site_domain in begin_url:
      return

  if depth == 1:
    urls = get_url_of_page(begin_url, True)
    img.extend(urls)
  else:
    urls = get_url_of_page(begin_url)
    if urls:
      for url in urls:
        get_page_html(url, depth-1)

def download_img(save_path, min_size):
  print "download begin..."
  for im in img:
    filename = im.split("/")[-1]
    dist = os.path.join(save_path, filename)
    connection = urllib2.build_opener().open(urllib2.Request(im))
    if int(connection.headers.dict['content-length']) < min_size:
      continue
    urllib.urlretrieve(im, dist,None)
    print "Done: ", filename
  print "download end..."

if __name__ == "__main__":
  #sites to crawl
  url = "http://www.lkong.net/thread-1464340-1-1.html"
  #path for img
  save_path = os.path.abspath("./download")
  if not os.path.exists(save_path):
    os.mkdir(save_path)
  #min size of img; ignore too small img
  min_size = 92
  #recursion depth
  max_depth = 1
  #outer sites ignore
  ignore_outer = True
  main_site_domain = urlparse.urlsplit(url).netloc

  get_page_html(url, max_depth, ignore_outer, main_site_domain)

  download_img(save_path, min_size)
