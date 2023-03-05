class KeywordProcessor(object):

    def __init__(self):
        self._lastFoundKeyword = ""

    def isAswerInKeywordCollection(self, answer, keywordCollection):
        for keyword in keywordCollection:
            if keyword in answer:
                self._lastFoundKeyword = keyword
                return True
        return False

    @property
    def lastFoundKeyword(self):
        return self._lastFoundKeyword
