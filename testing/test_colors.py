#!/usr/bin/python3




import jk_terminal_essentials as te







def printBar(color:str, text:str):
	s = color + "  " + text + "  " + te.STYLE_RESET
	print(s)
#



for color, text in [
		(	te.FGCOLOR_BLACK,			"FGCOLOR_BLACK"		),
		(	te.FGCOLOR_RED,				"FGCOLOR_RED"		),
		(	te.FGCOLOR_GREEN,			"FGCOLOR_GREEN"		),
		(	te.FGCOLOR_YELLOW,			"FGCOLOR_YELLOW"		),
		(	te.FGCOLOR_BLUE,			"FGCOLOR_BLUE"		),
		(	te.FGCOLOR_MAGENTA,			"FGCOLOR_MAGENTA"		),
		(	te.FGCOLOR_CYAN,			"FGCOLOR_CYAN"		),
		(	te.FGCOLOR_LIGHT_GRAY,		"GREEN"		),
		(	te.FGCOLOR_DARK_GRAY,		"GREEN"		),
		(	te.FGCOLOR_LIGHT_RED,		"FGCOLOR_LIGHT_RED"		),
		(	te.FGCOLOR_LIGHT_GREEN,		"FGCOLOR_LIGHT_GREEN"		),
		(	te.FGCOLOR_LIGHT_YELLOW,	"FGCOLOR_LIGHT_YELLOW"		),
		(	te.FGCOLOR_LIGHT_BLUE,		"FGCOLOR_LIGHT_BLUE"		),
		(	te.FGCOLOR_LIGHT_MAGENTA,	"FGCOLOR_LIGHT_MAGENTA"		),
		(	te.FGCOLOR_LIGHT_CYAN,		"FGCOLOR_LIGHT_CYAN"		),
		(	te.FGCOLOR_WHITE,			"FGCOLOR_WHITE"		),
	]:
	printBar(color, text)





