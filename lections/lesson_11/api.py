# Copyright 2018 BEGOSoft Inc.
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


from flask import Flask
from flask import request

app = Flask(__name__)
# import requests
# requests.get()

@app.route('/', methods=['POST', 'PUT', 'DELETE', 'HEAD'])
def index():
    if request.method == 'GET':
        return 'You send me some query params: {}'.format(request.args)
    if request.method in ('PUT', 'DELETE','POST'):
        return "I GOT A {} WITH DATA: {}".format(request.method, request.form), 500
    if request.method == 'HEAD':
        return "Just a HEAD request"


if __name__ == '__main__':
    app.run()