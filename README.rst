returns
=======
.. image:: https://travis-ci.org/not-raspberry/returns.svg?branch=master
    :target: https://travis-ci.org/not-raspberry/returns

For people too lazy to create namedtuples by themselves.


.. code:: python

    import returns

    @returns.namedtuple('monkeys', 'snakes')
    def get_monkeys_and_snakes():
        return 'A lot!', 'Even more!'

    get_monkeys_and_snakes() # -> GetMonkeysAndSnakes(monkeys='A lot!', snakes='Even more!')
