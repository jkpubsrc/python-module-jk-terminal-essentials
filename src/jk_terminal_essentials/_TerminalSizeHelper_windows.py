

import os
import typing
import struct
import subprocess
import ctypes
import ctypes.wintypes

from .terminal_cursor_position import terminal_cursor_position






# Windows API structures

class COORD(ctypes.Structure):
	_fields_ = [
		("X", ctypes.wintypes.SHORT),
		("Y", ctypes.wintypes.SHORT),
	]
#

class SMALL_RECT(ctypes.Structure):
	_fields_ = [
		("Left", ctypes.wintypes.SHORT),
		("Top", ctypes.wintypes.SHORT),
		("Right", ctypes.wintypes.SHORT),
		("Bottom", ctypes.wintypes.SHORT),
	]
#

class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
	_fields_ = [
		("dwSize", COORD),
		("dwCursorPosition", COORD),
		("wAttributes", ctypes.wintypes.WORD),
		("srWindow", SMALL_RECT),
		("dwMaximumWindowSize", COORD),
	]
#

# Get handle to stdout

try:
	_handle = ctypes.windll.kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
except:
	_handle = None





#
# Static helper class to provide terminal width and height
#
class _TerminalSizeHelper_windows(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	@staticmethod
	def ____tryGetTerminalSize_tput() -> typing.Union[os.terminal_size,None]:
		try:
			_data = subprocess.check_output([ "tput", "cols", "lines" ]).decode("UTF-8")
			_items = _data.split("\n")
			cols = int(_items[0])
			rows = int(_items[1])
			return os.terminal_size((cols, rows))
		except:
			pass

		return None
	#

	@staticmethod
	def ____tryGetTerminalSize_windll() -> typing.Union[os.terminal_size,None]:
		try:
			from ctypes import windll, create_string_buffer
			h = windll.kernel32.GetStdHandle(-12)
			csbi = create_string_buffer(22)
			res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
			if res:
				(_bufx, _bufy, _curx, _cury, _wattr, _left, _top, _right, _bottom, _maxx, _maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
				cols = _right - _left + 1
				rows = _bottom - _top + 1
				return os.terminal_size((cols, rows))
		except:
			pass

		return None
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	#
	# Main entry point for determining Windows terminal size
	#
	@staticmethod
	def __windows_getTerminalSize() -> typing.Union[os.terminal_size,None]:
		try:
			return os.get_terminal_size()
		except:
			pass

		# ----

		ret = _TerminalSizeHelper_windows.____tryGetTerminalSize_windll()
		if ret:
			return ret

		ret = _TerminalSizeHelper_windows.____tryGetTerminalSize_tput()
		if ret:
			return ret

		return None
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	################################################################################################################################
	## Public Static Methods
	################################################################################################################################

	@staticmethod
	def getTerminalSize() -> os.terminal_size:
		ret = _TerminalSizeHelper_windows.__windows_getTerminalSize()
		if ret is None:
			return os.terminal_size((80, 24))
		return ret
	#

	@staticmethod
	def getCusorPosition() -> terminal_cursor_position:
		if _handle is None:
			raise Exception()

		csbi = CONSOLE_SCREEN_BUFFER_INFO()
		success = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(
			_handle,
			ctypes.byref(csbi)
		)

		if success:
			x = csbi.dwCursorPosition.X
			y = csbi.dwCursorPosition.Y
			return terminal_cursor_position(x, y)
		else:
			return terminal_cursor_position(-1, -1)
	#

#

















