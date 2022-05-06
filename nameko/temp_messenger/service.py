from nameko.rpc import rpc


class KonnichiwaService:
    name = 'konnichiwa.service'

    @rpc
    def konnichiwa(self):
        return 'konnichiwa'
 