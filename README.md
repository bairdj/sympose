Sympose is a meeting management and authentication wrapper for Jitsi Meet.
Its purpose is to provide simple authentication and meeting management for private Jitsi Meet instances.
I created this to secure my own Jitsi Meet instance without the limitations of the internal plain authentication and
without having to configure LDAP. Sympose uses room-based JWTs to authorise users to Jitsi.

![Dashboard](example/screenshot/dashboard.png)

### Features
* Create meetings with subjects at an allotted time
* Assign attendees to meetings. Other users do not have access
* Use the power of Django's admin to manage meetings and users
* Allows creation of anonymous JWTs, so you can share a link to unregistered guests without having to open the server
* Automatically generates unique room names, to avoid collision with common meeting subjects
* Compatible with Jitsi Meet mobile apps. Will automatically authenticate using the JWT
* Automatically sets user's display name in Jitsi

### Installation
You will need to have your own Jitsi Meet instance. The easiest way to get started is to use
[Jitsi Meet on Docker](https://github.com/jitsi/docker-jitsi-meet).

Then just install Django as normal and change the relevant JITSI_ settings in settings.py.
You will need to set JITSI_DOMAIN. The others can be left as default but you'll probably want to set a proper secret.
These settings need to match the JWT_ environment variables in Docker.

### Built using
* Django
* Bulma
* Jitsi Meet API

### Roadmap
* Send invitations
* Calendar invites
* Enhanced admin
* Better integration with Jitsi JS API
* Properly write JavaScript