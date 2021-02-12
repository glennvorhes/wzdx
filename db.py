
import cx_Oracle
from cx_Oracle import Cursor
import warnings


_oracle_connection_dict = {}

_oracle_connections = {
    'transdb2': {
        'host': 'transport-db.cee.wisc.edu',
        'port': 1521,
        'usr': 'research',
        'pwd': 'its123'
    }
}



def get_oracle_connection(sid: str = 'transdb2') -> cx_Oracle.Connection:
    """
    Get a cx_Oracle connection

    :param sid: the sid, database identifier
    :return: the oracle connection
    """
    if sid in _oracle_connection_dict:
        the_connection = _oracle_connection_dict[sid]
        try:
            the_connection.ping()
            return the_connection
        except cx_Oracle.InterfaceError as ex:
            # printd(ex)
            pass

    db_dsn_tns = cx_Oracle.makedsn(_oracle_connections[sid]['host'], _oracle_connections[sid]['port'], sid)

    try:
        _oracle_connection_dict[sid] = cx_Oracle.connect(
            _oracle_connections[sid]['usr'],
            _oracle_connections[sid]['pwd'],
            db_dsn_tns)

        return _oracle_connection_dict[sid]
    except cx_Oracle.DatabaseError as ex:
        warnings.warn("Oracle database not available: [{0}".format(type(ex)))
        print(ex.args[0])
        return None