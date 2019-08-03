from ..utils import BasicSegment
import os


class Segment(BasicSegment):
    def add_to_powerline(self):
        powerline = self.powerline
        root_indicators = {
            'bash': ' \\$ ',
            'tcsh': ' %# ',
            'zsh': ' %# ',
            'bare': ' $ ',
        }
        bg = powerline.theme.CMD_PASSED_BG
        fg = powerline.theme.CMD_PASSED_FG
        if powerline.args.prev_error != 0:
            fg = powerline.theme.CMD_FAILED_FG
            bg = powerline.theme.CMD_FAILED_BG
        symbol = ' \uf0f0 ' if os.geteuid() == 0 else ' \uf007 '
        powerline.append(symbol, fg, bg, sanitize=False)
        #powerline.append(root_indicators[powerline.args.shell], fg, bg, sanitize=False)
