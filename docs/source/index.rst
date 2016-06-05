
``vclock`` - vector clocks for Python
=====================================

Clocks across various machines are not synchronised. Clock drift is
likely to occur. For distributed systems you need logical clocks to
preserve ordering between events. ``vclock`` is a simple, functional
library, built in the style of heapq_ for manipulating them::

   >>> import vclock
   >>> clock = vclock.from_size(3)
   >>> vclock.increment(clock, 2)
   (0, 0, 1)

.. _heapq: https://docs.python.org/3.5/library/heapq.html

API
---

.. NOTE::
   None of the functions which operate on multiple clocks check if two
   vector clocks are of the same size. By default and by design
   only the values of the 'shortest' clock are taken into account.

.. autofunction:: vclock.from_size

      >>> vclock.from_size(3)
      (0, 0, 0)

.. autofunction:: vclock.merge

      >>> vclock.merge((1, 2), (2, 1))
      (2, 2)

.. autofunction:: vclock.compare

      >>> vclock.compare((1, 2), (2, 2))
      -1
      >>> vclock.compare((1, 2), (0, 0))
      1
      >>> vclock.compare((1, 2), (1, 2))
      0
      >>> vclock.compare((1, 2), (2, 1))
      0

.. autofunction:: vclock.sort

      >>> vclock.sort([
      ...  [1, (1, 2)],
      ...  [2, (2, 2)],
      ...  [3, (1, 1)],
      ... ], key=lambda a: a[0])
      [(1, 1), (1, 2), (2, 2)]

.. autofunction:: vclock.is_concurrent

      >>> vclock.is_concurrent((1, 2), (1, 2))
      False
      >>> vclock.is_concurrent((1, 2), (2, 1))
      True

.. autofunction:: vclock.increment

      >>> vclock.increment((0, 1), 0)
      (1, 1)
