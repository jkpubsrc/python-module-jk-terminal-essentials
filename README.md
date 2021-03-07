jk_terminal_essentials
==========

Introduction
------------

This module provides essential constants and information about the terminal. This module is intended for implementing CLI tools and other applications running in a terminal.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/....)
* [pypi.python.org](https://pypi.python.org/pypi/jk_terminal_essentials)

How to use this module
----------------------

### Import this module

Please include this module into your application using the following code:

```python
import jk_terminal_essentials as te
```

### Colors

This module provides a variety of color constants. For example:

```python
print(te.FGCOLOR_RED + "Error!" + te.STYLE_RESET)
```

The following colors are supported:

```python
FGCOLOR_BLACK = "\x1b[30m"
FGCOLOR_RED = "\x1b[31m"
FGCOLOR_GREEN = "\x1b[32m"
FGCOLOR_YELLOW = "\x1b[33m"
FGCOLOR_BLUE = "\x1b[34m"
FGCOLOR_MAGENTA = "\x1b[35m"
FGCOLOR_CYAN = "\x1b[36m"
FGCOLOR_LIGHT_GRAY = "\x1b[37m"

FGCOLOR_DARK_GRAY = "\x1b[90m"
FGCOLOR_LIGHT_RED = "\x1b[91m"
FGCOLOR_LIGHT_GREEN = "\x1b[92m"
FGCOLOR_LIGHT_YELLOW = "\x1b[93m"
FGCOLOR_LIGHT_BLUE = "\x1b[94m"
FGCOLOR_LIGHT_MAGENTA = "\x1b[95m"
FGCOLOR_LIGHT_CYAN = "\x1b[96m"
FGCOLOR_WHITE = "\x1b[97m"
```

### Check for Color Support

To check if the current terminal supports colors:

```python
print(te.checkTerminalSupportsColors())
```

Contact Information
-------------------

This work is Open Source. This enables you to use this work for free.

Please have in mind this also enables you to contribute. We, the subspecies of software developers, can create great things. But the more collaborate, the more fantastic these things can become. Therefore Feel free to contact the author(s) listed below, either for giving feedback, providing comments, hints, indicate possible collaborations, ideas, improvements. Or maybe for "only" reporting some bugs:

* Jürgen Knauth: jknauth@uni-goettingen.de, pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



