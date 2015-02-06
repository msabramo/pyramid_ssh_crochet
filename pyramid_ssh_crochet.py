import logging
import sys

import crochet
crochet.setup()


logger = logging.getLogger(__name__)


@crochet.run_in_reactor
def start_ssh_server(port, username, password, namespace):
    """
    Start an SSH server on the given port, exposing a Python prompt with the
    given namespace.
    """
    # This is a lot of boilerplate, see http://tm.tl/6429 for a ticket to
    # provide a utility function that simplifies this.
    from twisted.internet import reactor
    from twisted.conch.insults import insults
    from twisted.conch import manhole, manhole_ssh
    from twisted.cred.checkers import (
        InMemoryUsernamePasswordDatabaseDontUse as MemoryDB)
    from twisted.cred.portal import Portal

    sshRealm = manhole_ssh.TerminalRealm()
    def chainedProtocolFactory():
        return insults.ServerProtocol(manhole.Manhole, namespace)
    sshRealm.chainedProtocolFactory = chainedProtocolFactory

    sshPortal = Portal(sshRealm, [MemoryDB(**{username: password})])
    reactor.listenTCP(port, manhole_ssh.ConchFactory(sshPortal),
                      interface="127.0.0.1")


def includeme(config):
    """Function that gets called when client code calls config.include"""
    settings = config.registry.settings
    port = int(settings['pyramid_ssh_crochet.port'])
    username = settings['pyramid_ssh_crochet.username']
    password = settings['pyramid_ssh_crochet.password']
    start_ssh_server(
        port=port,
        username=username,
        password=password,
        namespace={'config': config,
                   'registry': config.registry,
                   'settings': config.registry.settings})
    logger.info("pyramid_ssh_crochet: Started ssh server on port %d", port)
