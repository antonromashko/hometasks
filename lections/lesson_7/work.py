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


def number():
    i = 0
    v = None
    while True:
        v = (yield i)

        if v != None:
            break

        i += 1


num = number()
next(num)

for i in range(10):
    print(next(num))

try:
    num.send(1)
except StopIteration:
    print("STOP")

print(next(num))
