import libtorrent as lt
import fnmatch
import os
import time
import sys
from upload import upload

link = ('magnet:?xt=urn:btih:64A1872D2A1B4B12153C25FE29FAECAE0F19399C&dn=DJ+Khaled++POPSTAR+%28feat.+Drake%29+Rap+Single+2020+320+kbps+Beats%E2%AD%90&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2920%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce')

def torrent():
    '''Download a magnet link'''

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
