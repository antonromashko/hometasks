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


class MyIterator:

    def __init__(self):
        self.arr = [i for i in range(20)]
        #self.count = 0

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count >= len(self.arr):
            raise StopIteration
        self.count += 1
        return self.arr[self.count-1]


if __name__ == '__main__':

    print("<< Test 1 >>")
    i = MyIterator()
    for item in i:
        print(item, end=",")
    print("\nTEST")
    for item in i:
        print(item, end=",")

    print("\n<< Test 2 >>")

    b = [1,2,3,4]

    iter_b = iter(b)

    print(next(iter_b))
    for item in iter_b:
        print(item, end=",")
