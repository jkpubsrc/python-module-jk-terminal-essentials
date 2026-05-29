

import os
import typing
import struct
import sys
import termios
import tty

from .terminal_cursor_position import terminal_cursor_position






#
# Static helper class to provide terminal width and height
#
class _TerminalSizeHelper_posix_ioctl(object):

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
	def ____ioctl_GWINSZ(fd) -> os.terminal_size|None:
		try:
			import fcntl
			import termios
			cr = struct.unpack("hh", fcntl.ioctl(fd, termios.TIOCGWINSZ, "1234"))
			return os.terminal_size((cr[0], cr[1]))
		except:
			pass

		return None
	#

	#
	# Main entry point for determining POSIX terminal size
	#
	@staticmethod
	def __posix_getTerminalSize() -> os.terminal_size|None:
		ret = _TerminalSizeHelper_posix_ioctl.____ioctl_GWINSZ(0)
		if ret:
			return ret

		ret = _TerminalSizeHelper_posix_ioctl.____ioctl_GWINSZ(1)
		if ret:
			return ret

		ret = _TerminalSizeHelper_posix_ioctl.____ioctl_GWINSZ(2)
		if ret:
			return ret

		try:
			# NOTE: ctermid() is not available on all platforms
			with os.open(os.ctermid(), os.O_RDONLY) as fin:
				ret = _TerminalSizeHelper_posix_ioctl.____ioctl_GWINSZ(fin)
				return ret
		except:
			pass

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
		ret = _TerminalSizeHelper_posix_ioctl.__posix_getTerminalSize()
		if ret is None:
			return os.terminal_size(80, 24)
		return ret
	#

	@staticmethod
	def getCusorPosition() -> terminal_cursor_position:
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)

		try:
			tty.setcbreak(fd)

			sys.stdout.write("\x1b[6n")
			sys.stdout.flush()

			response = ""
			while True:
				ch = sys.stdin.read(1)
				response += ch
				if ch == "R":
					break

		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

		_row, _col = map(int, response.lstrip("\x1b[").rstrip("R").split(";"))
		return terminal_cursor_position(_col, _row)

	#

#

















