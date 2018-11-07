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

__all__ = []

from mylib import *
print([(k,v) for k, v in locals().items()])
# print([(k,v) for k, v in locals().items() if not k.endswith('__') and not k.startswith('__')])

# from mylib import _b
# from mylib import __c
# from mylib import d
#
# print(a,  _b, __c, d)

# from mylib import foo
#
# foo()


# import pack.mod
#
# print(pack.mod)
#
# from pack import mod2
#
# print(mod2)
# import pack.mod2 as mod2
# print(mod2)
# #print(pack.mod2)

# from pack import mod2
#
# print(mod2)