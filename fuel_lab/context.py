"""解释已取得原文中的认证适用市场业务上下文。"""
from .evidence import records

def snapshot(db,known_at):
    rows=records(db,'context',known_at)
    if not rows:return None
    p=rows[-1]['payload']
    return {'standard':p['standard'],'recognized_markets':tuple(p['recognized_markets']),'claim_units':p['claim_units']}

def eligible(s,d,state,period):
    if state is None:return False,'缺少业务上下文'
    return (d['market'] in state['recognized_markets'],'现有标准不覆盖买方市场')

def metrics(allocations,state,period):
    if state is None:return {'context_gap':'缺少业务上下文'}
    return {'attribute_units_declared':state['claim_units'],'recognized_markets':list(state['recognized_markets'])}
