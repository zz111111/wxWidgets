## This file reverse renames symbols in the wx package to give
## them their wx prefix again, for backwards compatibility.
##
## Generated by ./distrib/build_renamers.py

# This silly stuff here is so the wxPython.wx module doesn't conflict
# with the wx package.  We need to import modules from the wx package
# here, then we'll put the entry back in sys.modules.
import sys
_wx = None
if sys.modules.has_key('wxPython.wx'):
    _wx = sys.modules['wxPython.wx']
    del sys.modules['wxPython.wx']

import wx.html

sys.modules['wxPython.wx'] = _wx
del sys, _wx


# Now assign all the reverse-renamed names:
wxHTML_ALIGN_LEFT = wx.html.HTML_ALIGN_LEFT
wxHTML_ALIGN_CENTER = wx.html.HTML_ALIGN_CENTER
wxHTML_ALIGN_RIGHT = wx.html.HTML_ALIGN_RIGHT
wxHTML_ALIGN_BOTTOM = wx.html.HTML_ALIGN_BOTTOM
wxHTML_ALIGN_TOP = wx.html.HTML_ALIGN_TOP
wxHTML_CLR_FOREGROUND = wx.html.HTML_CLR_FOREGROUND
wxHTML_CLR_BACKGROUND = wx.html.HTML_CLR_BACKGROUND
wxHTML_UNITS_PIXELS = wx.html.HTML_UNITS_PIXELS
wxHTML_UNITS_PERCENT = wx.html.HTML_UNITS_PERCENT
wxHTML_INDENT_LEFT = wx.html.HTML_INDENT_LEFT
wxHTML_INDENT_RIGHT = wx.html.HTML_INDENT_RIGHT
wxHTML_INDENT_TOP = wx.html.HTML_INDENT_TOP
wxHTML_INDENT_BOTTOM = wx.html.HTML_INDENT_BOTTOM
wxHTML_INDENT_HORIZONTAL = wx.html.HTML_INDENT_HORIZONTAL
wxHTML_INDENT_VERTICAL = wx.html.HTML_INDENT_VERTICAL
wxHTML_INDENT_ALL = wx.html.HTML_INDENT_ALL
wxHTML_COND_ISANCHOR = wx.html.HTML_COND_ISANCHOR
wxHTML_COND_ISIMAGEMAP = wx.html.HTML_COND_ISIMAGEMAP
wxHTML_COND_USER = wx.html.HTML_COND_USER
wxHW_SCROLLBAR_NEVER = wx.html.HW_SCROLLBAR_NEVER
wxHW_SCROLLBAR_AUTO = wx.html.HW_SCROLLBAR_AUTO
wxHW_NO_SELECTION = wx.html.HW_NO_SELECTION
wxHW_DEFAULT_STYLE = wx.html.HW_DEFAULT_STYLE
wxHTML_OPEN = wx.html.HTML_OPEN
wxHTML_BLOCK = wx.html.HTML_BLOCK
wxHTML_REDIRECT = wx.html.HTML_REDIRECT
wxHTML_URL_PAGE = wx.html.HTML_URL_PAGE
wxHTML_URL_IMAGE = wx.html.HTML_URL_IMAGE
wxHTML_URL_OTHER = wx.html.HTML_URL_OTHER
wxHtmlLinkInfo = wx.html.HtmlLinkInfo
wxHtmlTag = wx.html.HtmlTag
wxHtmlParser = wx.html.HtmlParser
wxHtmlWinParser = wx.html.HtmlWinParser
wxHtmlTagHandler = wx.html.HtmlTagHandler
wxHtmlWinTagHandler = wx.html.HtmlWinTagHandler
wxHtmlWinParser_AddTagHandler = wx.html.HtmlWinParser_AddTagHandler
wxHtmlSelection = wx.html.HtmlSelection
wxHTML_SEL_OUT = wx.html.HTML_SEL_OUT
wxHTML_SEL_IN = wx.html.HTML_SEL_IN
wxHTML_SEL_CHANGING = wx.html.HTML_SEL_CHANGING
wxHtmlRenderingState = wx.html.HtmlRenderingState
wxHtmlRenderingStyle = wx.html.HtmlRenderingStyle
wxDefaultHtmlRenderingStyle = wx.html.DefaultHtmlRenderingStyle
wxHtmlRenderingInfo = wx.html.HtmlRenderingInfo
wxHTML_FIND_EXACT = wx.html.HTML_FIND_EXACT
wxHTML_FIND_NEAREST_BEFORE = wx.html.HTML_FIND_NEAREST_BEFORE
wxHTML_FIND_NEAREST_AFTER = wx.html.HTML_FIND_NEAREST_AFTER
wxHtmlCell = wx.html.HtmlCell
wxHtmlWordCell = wx.html.HtmlWordCell
wxHtmlContainerCell = wx.html.HtmlContainerCell
wxHtmlColourCell = wx.html.HtmlColourCell
wxHtmlFontCell = wx.html.HtmlFontCell
wxHtmlWidgetCell = wx.html.HtmlWidgetCell
wxHtmlFilter = wx.html.HtmlFilter
wxPreHtmlWindow = wx.html.PreHtmlWindow
wxHtmlWindow_AddFilter = wx.html.HtmlWindow_AddFilter
wxHtmlWindow = wx.html.HtmlWindow
wxHtmlDCRenderer = wx.html.HtmlDCRenderer
wxPAGE_ODD = wx.html.PAGE_ODD
wxPAGE_EVEN = wx.html.PAGE_EVEN
wxPAGE_ALL = wx.html.PAGE_ALL
wxHtmlPrintout_AddFilter = wx.html.HtmlPrintout_AddFilter
wxHtmlPrintout_CleanUpStatics = wx.html.HtmlPrintout_CleanUpStatics
wxHtmlPrintout = wx.html.HtmlPrintout
wxHtmlEasyPrinting = wx.html.HtmlEasyPrinting
wxHtmlBookRecord = wx.html.HtmlBookRecord
wxHtmlContentsItem = wx.html.HtmlContentsItem
wxHtmlSearchStatus = wx.html.HtmlSearchStatus
wxHtmlHelpData = wx.html.HtmlHelpData
wxHtmlHelpFrame = wx.html.HtmlHelpFrame
wxHF_TOOLBAR = wx.html.HF_TOOLBAR
wxHF_FLATTOOLBAR = wx.html.HF_FLATTOOLBAR
wxHF_CONTENTS = wx.html.HF_CONTENTS
wxHF_INDEX = wx.html.HF_INDEX
wxHF_SEARCH = wx.html.HF_SEARCH
wxHF_BOOKMARKS = wx.html.HF_BOOKMARKS
wxHF_OPENFILES = wx.html.HF_OPENFILES
wxHF_PRINT = wx.html.HF_PRINT
wxHF_DEFAULTSTYLE = wx.html.HF_DEFAULTSTYLE
wxHtmlHelpController = wx.html.HtmlHelpController


