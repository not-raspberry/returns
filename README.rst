returns
=======
.. image:: https://travis-ci.org/not-raspberry/returns.svg?branch=master
    :target: https://travis-ci.org/not-raspberry/returns
.. image:: https://coveralls.io/repos/not-raspberry/returns/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/not-raspberry/returns?branch=master


What is it?
-----------
The easiest way to return a value of a known type, with named fields accessible via attributes.

For whom?
---------
For people too lazy to create namedtuples by themselves.


Examples
--------
.. code:: python

    import returns

    # Name generated from function name:
    @returns.namedtuple('monkeys', 'snakes')
    def get_monkeys_and_snakes():
        return 'A lot!', 'Even more!'

    get_monkeys_and_snakes() # -> GetMonkeysAndSnakes(monkeys='A lot!', snakes='Even more!')


    # With a custom name:
    @returns.namedtuple('hyenas', 'lions', name='HyaenaeEtLeones')
    def get_hyenas_and_lions():
        return 'A herd.', 42

    get_hyenas_and_lions() # -> HyaenaeEtLeones(hyenas='A herd.', lions=42)


Trivia
------
As every library that does almost nothing, this one is also weirdly named. ``returns`` is not even a
noun. It looks like a keyword. Add insult to injury, the name ``returns.namedtuple`` may be mistaken
with the ``namedtuple`` from ``collections``.

But c'mon! It reads like a sentence! ``@returns.namedtuple`` - it's like 'returns namedtuple',
right? That's what cool-kid programming is all about!
