#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT =jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        try:
            # appends the correct html file to the end of templates/ so you don't have to hard code all files
            template = JINJA_ENVIRONMENT.get_template('templates/%s' % self.request.path)
            self.response.write(template.render())
        except:
            # if it doesn't work automatically goes to home page
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render())
            # outstr = template.render()

app = webapp2.WSGIApplication([
    ('/', MainHandler),            #making an instance: running the code.  
    ('/index.html', MainHandler),
    ('/activities.html', MainHandler),
    ('/cities.html', MainHandler),
    ('/parks.html', MainHandler),
], debug=True)


