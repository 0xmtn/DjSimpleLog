DjSimpleLog
===========

A simple logger for Django
It can be used in development stage.<br />
<br />
<b>Usage:</b><br />
Put the code into settings.py.<br /> Then add following to __ __init__ __.py inside every `app`.<br />
import logging<br />
LOG = logging.getLogger('`app`')<br />
<br />
Then add this to every file where you're going to use 'LOG':<br />
from `app` import LOG<br />
<br />
LOG.debug("BLAHBLAHABLAHAL")<br />
<br />
And finally (and for now) add 'logs/access.log' to the roots of every app of your project.<br />
<br />
That's it. <br />
