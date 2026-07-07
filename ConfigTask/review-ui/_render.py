import sys; sys.path.insert(0, ".")
import serve
A = serve.build_assets()
T = A["tasks"]; tree = A["tree"]
TBY = {t["_short"]: t for t in T}
def short(r): return (r or "").split("@")[-1]
def chips(arr):
    out=[]
    for s in arr:
        t=TBY.get(s)
        if t: out.append(f"{s} {t.get('task_logical_name','')}")
    return out or ["（无）"]
def rellist(rels):
    lines=[]
    for r in (rels or []):
        rt=r.get("relation_type",""); f=short(r.get("from_task_ref","")); o=short(r.get("to_task_ref",""))
        tags=[]
        if r.get("requiredness") and r["requiredness"]!="required": tags.append(r["requiredness"])
        if r.get("condition_ref"): tags.append("if "+short(r["condition_ref"]))
        lines.append(f"   [{rt}] {f} -> {o}  {' '.join(tags)}".rstrip())
    return lines
def show(sid):
    t=TBY.get(sid)
    if not t: print(f"--- {sid} MISSING ---"); return
    parent = tree["tree_parent"].get(sid)
    cont = tree["containers"].get(sid, [])
    kids = tree["children"].get(sid, [])
    sibs = (tree["children"].get(parent,[]) if parent else []) 
    sibs = [x for x in sibs if x!=sid]
    print(f"\n########## {sid} [{t.get('task_layer')}] {t.get('task_logical_name')} ##########")
    print(f"  kv: {t.get('_params')} 参数 · {t.get('_relations')} 编排边")
    print(f"  -- task详情/内联relList ({t.get('_relations')}条) --")
    for l in rellist(t.get("task_relations")): print(l)
    print(f"  -- 关系面板 --")
    print(f"     tree_parent = {parent}")
    print(f"     父/引用方 containers({len(cont)}): {chips(cont)}")
    print(f"     子/编排下层 children({len(kids)}): {chips(kids)}")
    print(f"     兄弟({len(sibs)}): {chips(sibs[:8])}")
for s in ["2-00010","2-00065","2-00066","2-00083","2-00023","2-00001"]:
    show(s)
