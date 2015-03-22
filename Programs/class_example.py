class A:
    def set_mess(self, msg):
        self.message = msg
        print self.message

    def __str__(self):
        return self.message

    def __init__(self, msg):
        self.message = msg
        print 'in constructor'
        print self.message