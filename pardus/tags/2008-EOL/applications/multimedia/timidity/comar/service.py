serviceType = "local"
serviceDesc = _({"en": "Timidity Virtual MIDI Sequencer for Alsa",
                 "tr": "Timidity Sanal MIDI Ardışımlayıcı"})

from comar.service import *
import os

@synchronized
def start():
    startDependencies("alsa-utils")

    if config.get("USE_ESOUND", "") == "yes":
        startDependencies("esound")

    # set up sound fonts
    patchset = config.get("PATCHSET", "shompatches")
    currentlink = "/usr/share/timidity/current"

    try:
        currentpatch = os.readlink(currentlink)
    except:
        currentpatch = None

    if patchset != currentpatch:
        if not os.path.exists("/usr/share/timidity/%s" % patchset) and not os.path.exists(patchset):
            fail("Failed to set patchset %s for Timidity" % patchset)
        else:
            if currentpatch:
                os.unlink(currentlink)
            os.symlink(patchset, currentlink)

    if config.get("TIMIDITY_PCM_NAME", "") != "":
        loadEnvironment()
        os.environ["TIMIDITY_PCM_NAME"]=config.get("TIMIDITY_PCM_NAME")

    startService(command="/usr/bin/timidity",
                 args="-iA %s" % config.get("TIMIDITY_OPTS", ""),
                 pidfile="/var/run/timidity.pid",
                 makepid=True,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/timidity.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/timidity.pid")
