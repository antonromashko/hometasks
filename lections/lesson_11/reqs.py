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


import requests


def show_data(url: str, data: dict) -> None:
    for method in ('get', 'post', 'put', 'delete', 'head', 'options'):
        res =  getattr(requests, method)(url, data=data)
        print("{} -> {} {}".format(method.upper(),
                                res.text, res.status_code))


if __name__ == '__main__':
    show_data("http://localhost:5000?data=124",
              {'user': 'me', 'password': 'gusta'})