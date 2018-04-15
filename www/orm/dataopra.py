'''
Created on 2018年4月15日

@author: bomber
'''
import logging
import aiomysql


def log(sql, args=[]):
    logging.info('sql: %s (args: %s)' % (sql, args))


async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (await __pool) as conn:
        cur = await conn.cursor(aiomysql)
        await cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = await cur.fechmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs

    
async def execute(sql, args):
    log(sql, args)
    with (await __pool) as conn:
        try:
            cur = await conn.cursor()    
            await cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount()
            await cur.close()
        except BaseException as e:
            raise
        return affected
