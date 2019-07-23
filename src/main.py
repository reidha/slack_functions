import daemon
from daemon import pidfile

import changestatus as cs

if __name__ == '__main__':
    cs.run(60)
    #with daemon.DaemonContext(
    #    pidfile=pidfile.TimeoutPIDLockFile('/var/run/sf/cs.pid')) as c:
    #    cs.run(10)
