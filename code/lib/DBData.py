class DBData:
    def __init__(self, conn_cursor, logging):
        self._cursor = conn_cursor
        self._logging = logging

    def get_data(self, limit=400000):
        self._logging.info('Retrieving data...')
        sql = 'SELECT '\
              '    t.text, '\
              '    t.category '\
              'FROM texts t '\
              'LIMIT %(limit)s'
        self._cursor.execute(sql, {'limit': limit})
        result = self._cursor.fetchall()
        
        self._logging.info('Found %d rows' % len(result))
        return result
