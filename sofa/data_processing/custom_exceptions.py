"""
This file is part of SOFA.
SOFA is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

SOFA is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with SOFA.  If not, see <http://www.gnu.org/licenses/>.
"""

# Custom import errors
class ImportError(Exception):
	pass

class UnableToReadMeasurementFileError(ImportError):
	pass

class UnableToReadImageFileError(ImportError):
	pass

class UnableToReadChannelFileError(ImportError):
	pass

class WrongImageSizeError(ImportError):
	pass

class WrongChannelSizeError(ImportError):
	pass

# Custom correction errors
class CorrectionError(Exception):
	pass

class UnableToLocateEndOfZerolineError(CorrectionError):
	pass

class UnableToLocateZeroCrossingAfterEozlError(CorrectionError):
	pass