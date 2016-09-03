=============================================================
 logging -- Report Status, Error, and Informational Messages
=============================================================

.. module:: logging
    :synopsis: Report status, error, and informational messages.

:Purpose: Report status, error, and informational messages.
:Python Version: 2.3 and later

The :mod:`logging` module defines a standard API for reporting errors
and status information from applications and libraries. The key
benefit of having the logging API provided by a standard library
module is that all Python modules can participate in logging, so an
application's log can include messages from third-party modules.

Logging in Applications vs. Libraries
=====================================

Application developers and library authors can both use
:mod:`logging`, but each audience has different considerations to keep
in mind.  

Application developers configure the :mod:`logging` module, directing
the messages to appropriate output channels.  It is possible to log
messages with different verbosity levels or to different
destinations. Handlers for writing log messages to files, HTTP
GET/POST locations, email via SMTP, generic sockets, or OS-specific
logging mechanisms are all included, and it is possible to create
custom log destination classes for special requirements not handled by
any of the built-in classes.

Developers of libraries can also use :mod:`logging` and have even less
work to do.  Simply create a logger instance for each context, using
an appropriate name, and then log messages using the standard levels.
As long as a library uses the logging API with consistent naming and
level selections, the application can be configured to show or hide
messages from the library, as desired.

Logging to a File
=================

Most applications are configured to log to a file. Use the
:func:`basicConfig()` function to set up the default handler so that
debug messages are written to a file.

.. include:: logging_file_example.py
    :literal:
    :start-after: #end_pymotw_header

After running the script, the log message is written to
``logging_example.out``:

.. {{{cog
.. outfile = path(cog.inFile).parent / 'logging_example.out'
.. outfile.unlink()
.. cog.out(run_script(cog.inFile, 'logging_file_example.py'))
.. }}}

::

	$ python logging_file_example.py

	FILE:
	DEBUG:root:This message should go to the log file
	

.. {{{end}}}


Rotating Log Files
==================

Running the script repeatedly causes more messages to be appended to
the file. To create a new file each time the program runs, pass a
``filemode`` argument to :func:`basicConfig()` with a value of
``'w'``. Rather than managing the creation of files this way, though,
it is better to use a :class:`RotatingFileHandler`, which creates new
files automatically and preserves the old log file at the same time.

.. include:: logging_rotatingfile_example.py
    :literal:
    :start-after: #end_pymotw_header

The result is six separate files, each with part of the log
history for the application:

.. {{{cog
.. outfile = path(cog.inFile).parent / 'logging_rotatingfile_example.out'
.. deleted = [ f.unlink() for f in outfile.glob('*') ]
.. cog.out(run_script(cog.inFile, 'logging_rotatingfile_example.py'))
.. }}}

::

	$ python logging_rotatingfile_example.py

	logging_rotatingfile_example.out
	logging_rotatingfile_example.out.1
	logging_rotatingfile_example.out.2
	logging_rotatingfile_example.out.3
	logging_rotatingfile_example.out.4
	logging_rotatingfile_example.out.5

.. {{{end}}}

The most current file is always ``logging_rotatingfile_example.out``, and
each time it reaches the size limit it is renamed with the suffix ``.1``. Each of
the existing backup files is renamed to increment the suffix (``.1`` becomes ``.2``,
etc.) and the ``.5`` file is erased.

.. note::

  Obviously this example sets the log length much too small as an
  extreme example. Set *maxBytes* to a more appropriate value in a
  real program.

Verbosity Levels
================

Another useful feature of the :mod:`logging` API is the ability to
produce different messages at different *log levels*. This means code can be
instrumented with debug messages, for example, and the log level can
be set so that those debug messages are not written on a production
system.  :table:`Logging Levels` lists the logging levels defined by
:mod:`logging`.

.. table:: Logging Levels

   ========  =====
   Level     Value
   ========  =====
   CRITICAL  50
   ERROR     40
   WARNING   30
   INFO      20
   DEBUG     10
   UNSET      0
   ========  =====

The log message is only emitted if the handler and logger are
configured to emit messages of that level or higher. For example, if a
message is :const:`CRITICAL`, and the logger is set to :const:`ERROR`,
the message is emitted (50 > 40). If a message is a :const:`WARNING`,
and the logger is set to produce only messages set to :const:`ERROR`,
the message is not emitted (30 < 40).

.. include:: logging_level_example.py
    :literal:
    :start-after: #end_pymotw_header

Run the script with an argument like 'debug' or 'warning' to see which
messages show up at different levels:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'logging_level_example.py debug'))
.. cog.out(run_script(cog.inFile, 'logging_level_example.py info', include_prefix=False))
.. }}}

::

	$ python logging_level_example.py debug

	DEBUG:root:This is a debug message
	INFO:root:This is an info message
	WARNING:root:This is a warning message
	ERROR:root:This is an error message
	CRITICAL:root:This is a critical error message

	$ python logging_level_example.py info

	INFO:root:This is an info message
	WARNING:root:This is a warning message
	ERROR:root:This is an error message
	CRITICAL:root:This is a critical error message

.. {{{end}}}

Naming Logger Instances
=======================

All of the previous log messages all have 'root' embedded in them. The
:mod:`logging` module supports a hierarchy of loggers with different
names. An easy way to tell where a specific log message comes from is
to use a separate logger object for each module. Every new logger
inherits the configuration of its parent, and log messages sent to a
logger include the name of that logger. Optionally, each logger can be
configured differently, so that messages from different modules are
handled in different ways. Here is an example of how to log from
different modules so it is easy to trace the source of the message:

.. include:: logging_modules_example.py
    :literal:
    :start-after: #end_pymotw_header

And the output:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'logging_modules_example.py'))
.. }}}

::

	$ python logging_modules_example.py

	WARNING:package1.module1:This message comes from one module
	WARNING:package2.module2:And this message comes from another module

.. {{{end}}}

There are many more options for configuring logging, including
different log message formatting options, having messages delivered to
multiple destinations, and changing the configuration of a long-running
application on the fly using a socket interface. All of these options are
covered in depth in the library module documentation.


.. seealso::

    `logging <http://docs.python.org/library/logging.html>`_
        The standard library documentation for this module.