class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.seq = []       # stores raw (normalized) values
        self.mult = 1       # global multiplier
        self.add  = 0       # global addend

    # ── helpers ──────────────────────────────────────────────────────────────

    def _inv(self, x: int) -> int:
        """Modular inverse via Fermat's little theorem (MOD is prime)."""
        return pow(x, self.MOD - 2, self.MOD)

    # ── public API ────────────────────────────────────────────────────────────

    def append(self, val: int) -> None:
        # Solve: raw * mult + add ≡ val  →  raw = (val - add) / mult
        raw = (val - self.add) % self.MOD * self._inv(self.mult) % self.MOD
        self.seq.append(raw)

    def addAll(self, inc: int) -> None:
        # true_new = raw * mult + (add + inc)
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        # true_new = raw * (mult*m) + (add*m)
        self.mult = self.mult * m % self.MOD
        self.add  = self.add  * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mult + self.add) % self.MOD