import Color
from TokenStore import TokenStore


class PlayerTokenStore(TokenStore):
    def validateWithdraw(self, old, new, color: Color) -> bool:

        if old - new < 0:
            raise RuntimeError("Cannot remove more gems than are in the store.")
        else:
            return True
