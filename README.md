Swift-Robots
------

Swift-Robots Middleware for OpenStack Swift, disallowing robots access to /


Install
-------

1) Install Swift-Rovots with ``sudo python setup.py install`` or ``sudo python
   setup.py develop`` or via whatever packaging system you may be using.

2) Alter your proxy-server.conf pipeline to have swift-robots:

Put it at the front!

    Was::

        [pipeline:main]
        pipeline = catch_errors cache tempauth proxy-server

    Change To::

        [pipeline:main]
        pipeline = robots catch_errors cache tempauth proxy-server

3) Add to your proxy-server.conf the section for the swift-robots WSGI filter::

    [filter:robots]
    use = egg:robots#robots