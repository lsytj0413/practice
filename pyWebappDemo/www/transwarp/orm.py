# coding=utf-8

"""
数据库ORM模块
"""

import logging, time
import db


class Field(object):
    """
    字段基类
    """

    _count = 0

    def __init__(self, **kw):
        self.name = kw.get('name', None)
        self._default = kw.get('default', None)
        self.primary_key = kw.get('primary_key', False)
        self.nullable = kw.get('nullable', False)
        self.updatable = kw.get('updatable', True)
        self.insertable = kw.get('insertable', True)
        self.ddl = kw.get('ddl', '')
        self._order = Field._count
        Field._count = Field._count + 1

    @property
    def default(self):
        d = self._default
        return d() if callable(d) else d

    def __str__(self):
        s = ['<%s:%s, %s, default(%s),' % (self.__class__.__name__, self.name, self.ddl, self._default)]
        self.nullable and s.append('N')
        self.updatable and s.append('U')
        self.insertable and s.append('I')
        s.append('>')
        return ''.join(s)


class StringField(Field):
    """
    字符串字段
    """

    def __init__(self, **kw):
        if not 'default' in kw:
            kw['default'] = ''
        if not 'ddl' in kw:
            kw['ddl'] = 'varchar(255)'
        super(StringField, self).__init__(**kw)


class IntegerField(Field):
    """
    整型字段
    """

    def __init__(self, **kw):
        if not 'default' in kw:
            kw['default'] = 0
        if not 'ddl' in kw:
            kw['ddl'] = 'bigint'
        super(IntegerField, self).__init__(**kw)


class FloatField(Field):
    """
    浮点型字段
    """

    def __init__(self, **kw):
        if not 'default' in kw:
            kw['default'] = 0.0
        if not 'ddl' in kw:
            kw['ddl'] = 'real'
        super(FloatField, self).__init__(**kw)


class BooleanField(Field):
    """
    bool字段
    """

    def __init__(self, **kw):
        if not 'default' in kw:
            kw['default'] = False
        if not 'ddl' in kw:
            kw['ddl'] = 'bool'
        super(BooleanField, self).__init__(**kw)


class TextField(Field):
    """
    文本字段
    """

    def __init__(self, **kw):
        if not 'default' in kw:
            kw['default'] = ''
        if not 'ddl' in kw:
            kw['ddl'] = 'text'
        super(TextField, self).__init__(**kw)


class BlobField(Field):
    """
    数据块字段
    """

    def __init__(self, **kw):
        if not 'default' in kw:
            kw['default'] = ''
        if not 'ddl' in kw:
            kw['ddl'] = 'blob'
        super(BlobField, self).__init__(**kw)


class VersionField(Field):
    """
    版本字段
    """

    def __init__(self, name=None):
        super(VersionField, self).__init__(name=name, default=0, ddl='bigint')


_triggers = frozenset(['pre_insert', 'pre_update', 'pre_delete'])


def _gen_sql(table_name, mappings):
    """
    构造建表sql语句
    """
    pk = None
    sql = ['-- generating SQL for {}:'.format(table_name), 'create table `%s`('%(table_name)]
    for f in sorted(mappings.values(), lambda x, y: cmp(x._order, y._order)):
        if not hasattr(f, 'ddl'):
            raise StandardError('no ddl in field "{}"'.format(f))
        ddl = f.ddl
        nullable = f.nullable
        if f.primary_key:
            pk = f.name
        sql.append(nullable and '  `%s` %s,' % (f.name, ddl) or '  `%s` %s not null,' % (f.name, ddl))
    sql.append('  primary key(`{}`)'.format(pk))
    sql.append(');')
    return '\n'.join(sql)


class ModelMetaclass(type):
    """
    ORM模型元类
    """

    def __new__(cls, name, bases, attrs):
        if name == 'Modle':
            return type.__new__(cls, name, bases, attrs)
        if not hasattr(cls, 'subclasses'):
            cls.subclasses = {}
        if not name in cls.subclasses:
            cls.subclasses[name] = name
        else:
            logging.warning('Redefine class: {}'.format(name))

        mappings = dict()
        primary_key = None
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                if not v.name:
                    v.name = k
                if v.primary_key:
                    if primary_key:
                        raise TypeError('Cannot define more than 1 primary key in class: {}'.format(name))
                    if v.updatable:
                        v.updatable = False
                    if v.nullable:
                        v.nullable = False
                    primary_key = v
                mappings[k] = v

        if not primary_key:
            raise TypeError('Primary key not defined in class: {}'.format(name))
        for k in mappings.iterkeys():
            attrs.pop(k)
        if not '__table__' in attrs:
            attrs['__table__'] = name.lower()
        attrs['__mappings__'] = mappings
        attrs['__primary_key__'] = primary_key
        attrs['__sql__'] = lambda self: __gen_sql(attrs['__table__'], mappings)
        for trigger in _triggers:
            if not trigger in attrs:
                attrs[trigger] = None
        return type.__new__(cls, name, bases, attrs)


class Model(dict):
    """
    ORM基类
    """

    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'dict' object has no attribute '{}'".format(key))

    def __setattr__(self, key, value):
        self[key] = value

    @classmethod
    def get(cls, pk):
        """
        通过primary_key 获取记录
        """
        d = db.select_one('select * from %s where %s=?' % (cls.__table__,
                                                           cls.__primary_key__.name),
                          pk)
        return cls(**d) if d else None

    @classmethod
    def find_first(cls, where, *args):
        """
        查找一条记录
        """
        d = db.select_one('select * from %s %s' % (cls.__table__, where),
                          *args
        )
        return cls(**d) if d else None

    @classmethod
    def find_all(cls, *args):
        """
        查找所有记录
        """
        L = db.select('select * from `%s`' % (cls.__table__))
        return [cls(**d) for d in L]

    @classmethod
    def find_by(cls, where, *args):
        """
        通过where条件返回记录
        """
        L = db.select('select * from `%s` %s' % (cls.__table__, where),
                      *args
        )
        return [cls(**d) for d in L]

    @classmethod
    def count_all(cls):
        """
        返回记录条数
        """
        return db.select_int('select count(`%s`) from `%s`' % (cls.__primary_key__.name,
                                                               cls.__table__
        ))

    @classmethod
    def count_by(cls, where, *args):
        """
        返回where筛选的记录条数
        """
        return db.select_int('select count(`%s`) from `%s` %s' % (cls.__primary_key__.name,
                                                                  cls.__table__,
                                                                  where),
                             *args
        )
