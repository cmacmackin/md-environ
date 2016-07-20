#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  include.py
#
#  Copyright 2015 Christopher MacMackin <cmacmackin@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from __future__ import print_function
from __future__ import unicode_literals
from os import getenv

from markdown import Extension
from markdown.inlinepatterns import Pattern

ENVIRON_RE = r'\$\{(\w+)\}'


class EnvironPattern(Pattern):
    """
    Pattern to pick out environment variables and insert their value.
    """
    def handleMatch(self, m):
        var = m.group(2)
        return getenv(var,'')
        

def makeExtension(*args, **kwargs):
    """Inform Markdown of the existence of the extension."""
    return EnvironExtension(*args, **kwargs)


class EnvironExtension(Extension):
    """
    Extension: ${VARNAME} will be replaced by contents of environment
    variable VARNAME, it it is defined, or by an empty string otherwise.
    """

    def extendMarkdown(self, md, md_globals):
        """Insert 'environ' pattern before 'not_strong' pattern."""
        md.inlinePatterns.add('environ',
                              EnvironPattern(ENVIRON_RE),
                              '<not_strong')
            
