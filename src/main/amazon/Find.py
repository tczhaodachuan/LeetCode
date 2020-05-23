class FileRule(object):
    def match(self, file):
        pass


class ExtentionFileRule(FileRule):
    def __init__(self, ext):
        self.ext = ext

    def match(self, file):
        return file.getName().endsWith("." + self.ext)


class SizeFileRuleOp(object):
    LT = 'LT'
    LTE = 'LTE'
    GT = 'GT'
    GTE = 'GTE'
    EQ = 'EQ'


class SizeFileRule(FileRule):

    def __init__(self, size, op):
        self.size = size
        self.op = op

    def match(self, file):
        if self.op == SizeFileRuleOp.LT:
            pass
        elif self.op == SizeFileRuleOp.LTE:
            pass


class LinuxFile(object):
    def __init__(self, path):
        self.path = path
        self.name = path.split('/')[-1]

    def getName(self):
        return self.name
