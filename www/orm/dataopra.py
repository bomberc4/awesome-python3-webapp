'''
Created on 2018年4月15日

@author: bomber
'''
import logging
import aiomysql

import orm.datapool as datapool


def log(sql, args=[]):
    logging.info('sql: %s (args: %s)' % (sql, args))


async def select(sql, args, size=None):
    log(sql, args)
    __pool=datapool.__pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fechmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs

    
async def execute(sql, args, autocommit=True):
    log(sql, args)
    __pool=datapool.__pool
    async with __pool.get() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor() as cur:
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount()
                if not autocommit:
                    await conn.commit()
                return affected
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
                raise