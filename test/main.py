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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        a = Account()


class Account(object):
    def __init__(self):
        self.__balance = 0
        self.owner = ""
        self.interest_rate = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(selfSelf, new_bal):
        self.__balance = new_bal

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
