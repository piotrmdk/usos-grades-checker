#!/usr/bin/env python
# -*- coding: utf-8 -*-

import oauth2 as oauth
from datetime import datetime
import urlparse
import json
import sys
import pprint


def grades():
  # USOS API Base URL, trailing slash included.
  usosapi_base_url = 'https://usosapps.uw.edu.pl/'

  # Consumer Key to use.
  from secure import ck
  from secure import cs
  consumer_key = ck
  consumer_secret = cs

  # Access Token to use.
  from secure import atk
  from secure import ats
  access_token_key = atk
  access_token_secret = ats

  # Client ini
  usosapi_base_url_secure = usosapi_base_url.replace("http://", "https://")
  consumer = oauth.Consumer(consumer_key, consumer_secret)
  access_token = oauth.Token(access_token_key, access_token_secret)
  client = oauth.Client(consumer, access_token)


  resp, content = (client.request(usosapi_base_url + "services/courses/user", "GET"))
  items = json.loads(content)
  grades_tab = []

  for semester in items['course_editions'].keys():
    for course in items['course_editions'][semester]:
      rc = {'id': '', 'term': '', 'name': '', 'unit':{}, 'grade': ''}
      rc['id'] = course.get('course_id')
      rc['term'] = course.get('term_id')
      rc['name'] = course['course_name']['pl']
      resp, content = (client.request(usosapi_base_url + "services/grades/course_edition?course_id=" + rc['id'] + "&term_id=" + rc['term'], "GET"))
      result = json.loads(content)

      if len(result.get('course_units_grades')) != 0:
        for unit in result.get('course_units_grades'):
          for part in result.get('course_units_grades').get(unit):
            exam = result.get('course_units_grades').get(unit).get(part).get('exam_id')
            rc['unit'][exam] = result.get('course_units_grades').get(unit).get(part).get('value_symbol')


      if result.get('course_grades') is not None:
        for part in result.get('course_grades'):
          if result.get('course_grades').get(part) is not None:
            rc['grade'] = result.get('course_grades').get(part).get('value_symbol')

      grades_tab.append(rc)
  return grades_tab


