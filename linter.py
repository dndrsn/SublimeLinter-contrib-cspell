from SublimeLinter.lint import Linter, STREAM_STDOUT


class CSpell(Linter):
    cmd = 'cspell stdin'
    defaults = {'selector': 'source'}
    regex = r'^[^:]*:(?P<line>\d+):(?P<col>\d+) - (?P<message>.*)$'
    error_stream = STREAM_STDOUT
