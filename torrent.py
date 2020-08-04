import libtorrent as lt
import fnmatch
import os
import time
import sys
from upload import upload

link = 'magnet:?xt=urn:btih:BF937884BDB76D2B9B16B73E95DAD5541DB1F4EC&dn=Drake+-+If+You%27re+Reading+This+It%27s+Too+Late+%282015+%29+%28320kbps%29&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2920%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce'

def torrent():
    '''Download from a magnet link'''

    ses = lt.session()
    ses.listen_on(6881, 6891)
    params = {'save_path': './Downloads'}

    h = lt.add_magnet_uri(ses, link, params)
    print("starting", h.name())

    while not h.is_seed():
        s = h.status()

        state_str = [
            "queued",
            "checking",
            "downloading metadata",
            "downloading",
            "finished",
            "seeding",
            "allocating",
            "checking fastresume",
        ]
        print(
            "\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s"
            % (
                s.progress * 100,
                s.download_rate / 1000,
                s.upload_rate / 1000,
                s.num_peers,
                state_str[s.state],
            )
        )
        sys.stdout.flush()
        time.sleep(1)

    print(h.name(), "complete")
    upload()
torrent()
