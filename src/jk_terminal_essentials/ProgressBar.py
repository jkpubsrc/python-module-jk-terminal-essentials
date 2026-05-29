

import math
import typing

import jk_typing
#import jk_utils
# import jk_logging
# import jk_json
# import jk_prettyprintobj






class ProgressBar(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	@jk_typing.checkFunctionSignature()
	def __init__(self, width:int, maximum:int|float):
		assert width > 0
		assert maximum > 0

		self.__charBlock = "#"
		self.__charEmpty = "·"
		self.__charUnknown = "?"
		self.__width = width
		self.__fMax = float(maximum)
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def progress(self, fProgress:int|float|None) -> str:
		if fProgress is None:
			return self.__charUnknown * self.__width

		assert isinstance(fProgress, (int, float))
		fProgress = float(fProgress)

		if fProgress < 0.0:
			f = 0.0
		else:
			if fProgress > self.__fMax:
				f = 1.0
			else:
				f = fProgress / self.__fMax

		nChars = math.ceil(f * self.__width)
		nCharsM1 = self.__width - nChars
		return self.__charBlock * nChars + self.__charEmpty * nCharsM1
	#

#





