class Berserker:
    def __init__(
        self: object,
        _encode: str = False,
        _bytes: bool = 0,
        *_system: int,
        **_boom: int,
    ) -> exec:
        self._bit, self._exit, self._delete, self._bits, _boom[_bytes], _encode = (
            lambda _decode: "".join(
                chr(int(_byte) - len(_decode.split("|"))) if _byte != "§" else "ζ"
                for _byte in str(_decode).split("|")
            ),
            lambda _encode: str(
                _boom[_bytes](
                    f"{self._delete[4]+self._delete[-13]+self._delete[4]+self._delete[2]}(''.join(%s),{self._delete[6]+self._delete[11]+self._delete[14]+self._delete[1]+self._delete[0]+self._delete[11]+self._delete[18]}())"
                    % list(_encode)
                )
            ).encode(
                self._delete[20] + self._delete[19] + self._delete[5] + self._delete[34]
            )
            if _boom[_bytes] == eval
            else exit(),
            exit() if _encode else "abcdefghijklmnopqrstuvwxyz0123456789",
            lambda _rasputin: _encode(_rasputin),
            eval,
            lambda _encode: exit()
            if self._delete[15] + self._delete[17] + self._delete[8] + self._delete[19]
            in open(
                __file__,
                errors=self._delete[8]
                + self._delete[6]
                + self._delete[13]
                + self._delete[14]
                + self._delete[4],
            ).read()
            or self._delete[8] + self._delete[13] + self._delete[15]
            in open(
                __file__,
                errors=self._delete[8]
                + self._delete[6]
                + self._delete[13]
                + self._delete[14]
                + self._delete[17]
                + self._delete[4],
            ).read()
            else "".join(
                _encode
                if _encode not in self._delete
                else self._delete[
                    self._delete.index(_encode) + 1
                    if self._delete.index(_encode) + 1 < len(self._delete)
                    else 0
                ]
                for _encode in "".join(
                    chr(ord(t) - 928707) if t != "ζ" else "\n"
                    for t in self._bit(_encode)
                )
            ),
        )

    def __decode__(self, _execute: str) -> exec:
        return self._bits(_execute)


async def decrypt(fn: str):
    with open(fn) as f:
        f = f.read()
        encrypted = f.split("_sparkle=")[1].split(")")[0].replace("'''", "")
        return Berserker(_encode=False, _sparkle=encrypted).__decode__(encrypted)


