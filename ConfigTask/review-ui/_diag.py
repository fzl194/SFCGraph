import sys, json
sys.path.insert(0, ".")
import serve

assets = serve.build_assets()
tasks = assets["tasks"]
tree = assets["tree"]
by_short = {t["_short"]: t for t in tasks}

# 1. dangling relation endpoints
dangling = set()
for t in tasks:
    for r in (t.get("task_relations") or []):
        for k in ("from_task_ref","to_task_ref"):
            s = serve.short(r.get(k,""))
            if s and s not in by_short:
                dangling.add((t["_short"], k, s, r.get("relation_id","")))
print("=== dangling endpoints ===", len(dangling))
for d in sorted(dangling)[:30]: print(" ", d)

# 2. duplicate relation_ids
seen={}
dups=[]
for t in tasks:
    for r in (t.get("task_relations") or []):
        rid=r.get("relation_id","")
        if rid:
            if rid in seen: dups.append((rid, seen[rid], t["_short"]))
            else: seen[rid]=t["_short"]
print("=== duplicate relation_ids ===", len(dups))
for d in dups[:30]: print(" ", d)

# 3. tree cycles (tree_parent chain)
tp=tree["tree_parent"]
def cyc(s):
    seen=set(); x=s
    while x:
        if x in seen: return x
        seen.add(x); x=tp.get(x)
    return None
cycs=[s for s in by_short if cyc(s)]
print("=== tree cycles ===", len(cycs), cycs[:10])

# 4. relations where from==to (self-loop) or from/to empty
bad=[]
for t in tasks:
    for r in (t.get("task_relations") or []):
        f=serve.short(r.get("from_task_ref","")); o=serve.short(r.get("to_task_ref",""))
        if f==o or not f or not o: bad.append((t["_short"], r.get("relation_id",""), f, o, r.get("relation_type","")))
print("=== selfloop/empty endpoints ===", len(bad))
for b in bad[:30]: print(" ", b)

# 5. for the P0-affected + opened file: dump relList lines + tree children + containers
def show(sid):
    t=by_short.get(sid)
    if not t: print(f"-- {sid}: MISSING"); return
    print(f"\n===== {sid} ({t.get('task_layer')}) {t.get('task_logical_name')} =====")
    for r in (t.get("task_relations") or []):
        f=serve.short(r.get("from_task_ref","")); o=serve.short(r.get("to_task_ref",""))
        extra=[]
        if r.get("requiredness") and r["requiredness"]!="required": extra.append(r["requiredness"])
        if r.get("condition_ref"): extra.append("if "+serve.short(r["condition_ref"]))
        print(f"   {r.get('relation_type','?'):14} {f} -> {o}  {' '.join(extra)}")
    print("  containers(父/引用方):", tree["containers"].get(sid,[]))
    print("  children(子):", tree["children"].get(sid,[]))
for s in ["2-00010","2-00065","2-00066","2-00083","2-00023"]:
    show(s)

# 6. global: how many features have DIRECT atom->atom relations (no compound intermediary)
direct=0; total_feat=0
for t in tasks:
    if t.get("task_layer")=="feature":
        total_feat+=1
        has=False
        for r in (t.get("task_relations") or []):
            f=serve.short(r.get("from_task_ref","")); o=serve.short(r.get("to_task_ref",""))
            if f.startswith("0-") and o.startswith("0-"): has=True
        if has: direct+=1
print(f"\n=== features w/ direct atom->atom relations: {direct}/{total_feat} ===")
