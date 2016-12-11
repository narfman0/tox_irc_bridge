import sys
from pytox import ToxAV

class AV(ToxAV):
    def __init__(self, core, max_calls):
        self.core = self.get_tox()
        self.cs = None
        self.call_type = self.TypeAudio

    def on_invite(self, idx):
        self.cs = self.get_peer_csettings(idx, 0)
        self.call_type = self.cs['call_type']

        print('Incoming %s call from %d:%s ...' % (
                'video' if self.call_type == self.TypeVideo else 'audio', idx,
                self.core.get_name(self.get_peer_id(idx, 0))))

        self.answer(idx, self.call_type)
        print('Answered, in call...')

    def on_start(self, idx):
        self.change_settings(idx, {'max_video_width': 1920,
                                   'max_video_height': 1080})
        self.prepare_transmission(idx, self.jbufdc * 2, self.VADd,
                True if self.call_type == self.TypeVideo else False)

    def on_end(self, idx):
        self.kill_transmission()

        print('Call ended')

    def on_peer_timeout(self, idx):
        self.stop_call()

    def on_audio_data(self, idx, size, data):
        sys.stdout.write('.')
        sys.stdout.flush()
        self.send_audio(idx, size, data)

    def on_video_data(self, idx, width, height, data):
        sys.stdout.write('*')
        sys.stdout.flush()
        self.send_video(idx, width, height, data)
