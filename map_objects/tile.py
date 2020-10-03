class Tile:
    """
    A tile on a map.  It may/may not be blocked and may/may not block sight.
    """

    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # By default, if a tile is blocked it also blocks site
        if block_sight is None:
            block_sight = blocked
        
        self.block_sight = block_sight

        self.explored = False