from builtins import *
#!/usr/bin/env python

#Copyright (c) 2013, Eduard Broecker
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without modification, are permitted provided that
# the following conditions are met:
#
#    Redistributions of source code must retain the above copyright notice, this list of conditions and the
#    following disclaimer.
#    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
#    following disclaimer in the documentation and/or other materials provided with the distribution.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
#WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
#PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
#DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
#OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
#DAMAGE.

#
# this script imports json-files from a canmatrix-object
# json-files are the can-matrix-definitions of the CANard-project (https://github.com/ericevenchick/CANard)

from .canmatrix import *
import codecs
import json
import sys

def importJson(filename, **options):
    db = CanMatrix()

    f = open(filename, "r")
    jsonData = json.load(f)

    if "messages" in jsonData:
        for frame in jsonData["messages"]:
            newframe = Frame(frame["id"],frame["name"],8,None)

            for signal in frame["signals"]:
                if signal["is_big_endian"]:
                    byteorder = 0
                else:
                    byteorder = 1
                if signal["is_signed"]:
                    valuetype = '-'
                else:
                    valuetype = '+'
                newsignal = Signal(signal["name"], signal["start_bit"], signal["bit_length"], 
                            byteorder, valuetype, signal["factor"], signal["offset"],0,0,"",[])
                newframe.addSignal(newsignal)
            db._fl.addFrame(newframe)
    f.close()
    return db
