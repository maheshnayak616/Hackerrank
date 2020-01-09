class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        nn = S.replace("-", "")
        r = len(nn) % K
        if len(nn) <= K:
            return nn.upper()
        f = nn[:r]
        p = nn[r:] if r > 0 else nn
        s = "-".join([p[i:i + K] for i in range(0, len(p), K)])
        return ("{}-{}".format(f, s) if f else s).upper()
        