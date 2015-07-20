def isNumber(self, s):
    try:
        float(s)
        return True
    except Exception, e:
        return False
