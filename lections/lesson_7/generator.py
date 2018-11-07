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


class Profile:
    args = ('first_name', 'last_name')

    def __init__(self, **kwargs):
        for arg in Profile.args:
            setattr(self, arg, kwargs.get(arg))


class Teacher(Profile):

    args = ('subject', )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for arg in self.__class__.args:
            setattr(self, arg, kwargs.get(arg))

    def __str__(self):
        return f"TEACHER: {self.first_name} {self.last_name} teaching {self.subject}"


class Student(Profile):
    args = ('group',)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for arg in self.__class__.args:
            setattr(self, arg, kwargs.get(arg))

    def __str__(self):
        return f"STUDENT: {self.first_name} {self.last_name} from {self.group}"


class Database:
    def __init__(self):
        self._students = []
        self._teachers = []

    def add(self, obj: Profile):
        if isinstance(obj, Student):
            self._students.append(obj)
        elif isinstance(obj, Teacher):
            self._teachers.append(obj)
        else:
            raise TypeError(type(obj))

    @property
    def students(self):
        for s in self._students:
            yield s

    @property
    def teachers(self):
        for t in self._teachers:
            yield t


    @property
    def people(self):
        yield from self.students
        yield from self.teachers


if __name__ == '__main__':
    db = Database()

    count = 5

    for i in range(count):
        s = Student(first_name=f'student_{i+1}_Name',
                    last_name=f'Student_{i+1}_Surname',
                    group='Group_{i+1}')

        t = Teacher(first_name=f'teacher_{i+1}_Name',
                    last_name=f'Teacher_{i+1}_Surname',
                    subject='Subject_{i+1}')

        db.add(s)
        db.add(t)

    print("<< STUDENTS >>")
    for s in db.students:
        print(s)

    print("<< TEACHERS >>")
    for t in db.teachers:
        print(t)

    # for obj in list(db.students) + list(db.teachers):

    print("<< ALL >>")
    for obj in db.people:
        print(obj)


def foo():
    a = (yield 1)
    yield a
    print("A=",a)
    yield 3

f=foo()

print(next(f))
print(f.send(345))
print(next(f))