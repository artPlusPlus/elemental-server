elemental-server
================

elemental-server provides an http/json interface to an elemental-backend.

elemental-server depends falcon as its WSGI application framework.

elemental-server is deliberately separate from elemental-backend. The goal
is to allow users who need control over their serving infrastructure the
freedom to build around the core elemental-backend. However, there is also a
set of users who do not want the hassle of setting up a server (often times
for good reason).