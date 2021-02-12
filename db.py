import cx_Oracle
import warnings
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import Session

usr = 'research'
pwd = 'its123'
_sid = cx_Oracle.makedsn('transport-db.cee.wisc.edu', 1521, 'transdb2')
cstr = 'oracle://{user}:{password}@{sid}'.format(user=usr, password=pwd, sid=_sid)

_oracle_connection_dict = {}
_oracle_engine_dict = {}
_oracle_session_dict = {}


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
    try:
        _oracle_connection_dict[sid] = cx_Oracle.connect(
            usr,
            pwd,
            _sid
        )

        return _oracle_connection_dict[sid]
    except cx_Oracle.DatabaseError as ex:
        warnings.warn("Oracle database not available: [{0}".format(type(ex)))
        print(ex.args[0])
        print(ex)
        return None


def get_oracle_engine(sid: str = 'transdb2') -> sqlalchemy.engine.base.Engine:

    if sid in _oracle_engine_dict:
        the_engine = _oracle_engine_dict[sid]
        the_connection = _oracle_connection_dict[sid]
        try:
            # the_connection.ping()
            return the_engine
        except cx_Oracle.InterfaceError as ex:
            # printd(ex)
            pass
    try:
        _oracle_engine_dict[sid] = create_engine(
            cstr,
            convert_unicode=False,
            pool_recycle=10,
            pool_size=50,
            echo=False
        )

        _oracle_connection_dict[sid] = _oracle_engine_dict[sid].connect()

        return _oracle_engine_dict[sid]
    except cx_Oracle.DatabaseError as ex:
        warnings.warn("Oracle database not available: [{0}".format(type(ex)))
        print(ex.args[0])
        print(ex)
        return None


def get_oracle_session(sid: str = 'transdb2') -> Session:

    if sid not in _oracle_session_dict:
        sqlalchemy_db_factory = sessionmaker(bind=get_oracle_engine())
        _oracle_session_dict[sid] = scoped_session(sqlalchemy_db_factory)

    return _oracle_session_dict[sid]
