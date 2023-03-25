class Health:
    columns = ['id', 'YearStart', 'YearEnd', 'LocationAbbr',
               'LocationDesc', 'Topic', 'Question']
    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))