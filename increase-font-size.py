# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

#FONT = "Times New Roman"

from aqt import mw
from aqt.qt import *

FONT_SIZE = 13

def changeGlobalFontSize():
    font = QApplication.font()
    font.setPixelSize(FONT_SIZE)
    QApplication.setFont(font)

def changeWebFontSize():
    ws = QWebSettings.globalSettings()
    ws.setFontSize(QWebSettings.DefaultFontSize, FONT_SIZE)

def changeFontSize():
    changeGlobalFontSize()
    changeWebFontSize()

changeFontSize()
