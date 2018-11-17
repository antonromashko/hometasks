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

from tkinter import *
from tkinter import filedialog as tkFileDialog


def Quit(ev):
    global root
    root.destroy()


def LoadFile(ev):
    fn = tkFileDialog.Open(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', open(fn, 'rt').read())


def SaveFile(ev):
    fn = tkFileDialog.SaveAs(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn += ".txt"
    open(fn, 'wt').write(textbox.get('1.0', 'end'))


root = Tk()

panelFrame = Frame(root, height=60, bg='gray')
textFrame = Frame(root, height=340, width=600)

panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)

textbox = Text(textFrame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')

loadBtn = Button(panelFrame, text='Load')
saveBtn = Button(panelFrame, text='Save')
quitBtn = Button(panelFrame, text='Quit')

loadBtn.bind("<Button-1>", LoadFile)
saveBtn.bind("<Button-1>", SaveFile)
quitBtn.bind("<Button-1>", Quit)

loadBtn.place(x=10, y=10, width=40, height=40)
saveBtn.place(x=60, y=10, width=40, height=40)
quitBtn.place(x=110, y=10, width=40, height=40)

root.mainloop()