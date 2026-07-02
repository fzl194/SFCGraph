// review-ui v3：三面板(命令/步骤/特性)平铺 + 主区内嵌子卡片(3 层嵌套 + 折叠策略)
// spec: docs/superpowers/specs/2026-07-02-review-ui-by-layer-design.md
let DATA = null, REV = null, CUR = null, FOCUS = "main";
const TBY = {}, RULES_BY = {}, DPS_BY = {};
const COLLAPSE = window.CHIP_COLLAPSE_AT || 15;
const COLLAPSE_LIGHT = window.CHIP_COLLAPSE_AT_LIGHT || 8;
const PANEL_LAYERS = ["atom", "compound", "feature"];  // generalized 不进焦点环(spec §3.5)
const PANEL_TITLES = { atom: "命令 atom", compound: "步骤 compound", feature: "特性 feature", generalized: "泛化 generalized" };

const $ = (id) => document.getElementById(id);
const esc = (s) => (s == null ? "" : String(s)).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const short = (ref) => (ref || "").split("@").pop();
const toast = (m) => { const t = $("toast"); t.textContent = m; t.classList.add("show"); setTimeout(() => t.classList.remove("show"), 1400); };

function statusOf(sid) {
  const r = (REV.records || {})[sid];
  return r && r.length ? r[r.length - 1].verdict : "待审查";
}
const ICON = { "通过": ["✓", "ic-ok"], "驳回": ["✕", "ic-bad"], "待补": ["◐", "ic-maybe"], "待审查": ["·", "ic-pend"] };

async function init() {
  let a, r;
  try { a = await fetch("/api/assets").then(x => x.json()); }
  catch (e) { renderFatal("审查服务未响应(请在 review-ui 目录运行 python serve.py)"); return; }
  try { r = await fetch("/api/review-state").then(x => x.json()); }
  catch (e) { r = { nf_version: "UDG@20.15.2", records: {} }; }
  DATA = a; REV = r;
  $("nfver").textContent = DATA.nf_version;
  for (const t of DATA.tasks) TBY[t._short] = t;
  for (const x of DATA.rules) {
    const o = short(x.owner_task_ref || "");
    (RULES_BY[o] = RULES_BY[o] || []).push(x);
  }
  for (const d of DATA.dps) {
    const o = short(d.owner_task_ref || "");
    (DPS_BY[o] = DPS_BY[o] || []).push(d);
  }
  renderStats();
  renderPanels();
  const h = location.hash.match(/#\/t\/(.+)$/);
  const initial = (h && h[1] && TBY[h[1]]) ? h[1] : (DATA.by_layer.feature[0] || DATA.by_layer.atom[0] || null);
  go(initial, true);
}

function renderFatal(msg) {
  $("main").innerHTML = `<div class="empty">${esc(msg)}</div>`;
  $("panels").innerHTML = "";
}

function renderStats() {
  const T = DATA.tasks;
  const c = l => T.filter(t => t.task_layer === l).length;
  const reviewed = T.filter(t => (REV.records[t._short] || []).length > 0).length;
  const byV = v => T.filter(t => statusOf(t._short) === v).length;
  $("stats").innerHTML = [
    ["<b>" + T.length + "</b>", "task"], ["<b>" + c("atom") + "</b>", "atom"],
    ["<b>" + c("compound") + "</b>", "compound"], ["<b>" + c("feature") + "</b>", "feature"],
    ["<b>" + DATA.dps.length + "</b>", "决策点"], ["<b>" + DATA.rules.length + "</b>", "规则"],
    ["<b style='color:var(--ok)'>" + byV("通过") + "</b>", "通过"],
    ["<b style='color:var(--bad)'>" + byV("驳回") + "</b>", "驳回"],
    ["<b style='color:var(--maybe)'>" + byV("待补") + "</b>", "待补"],
  ].map(([n, l]) => `<div class="stat">${n}<span>${l}</span></div>`).join("");
  $("dn").textContent = reviewed; $("dt").textContent = T.length;
  $("pbar").style.width = (T.length ? reviewed * 100 / T.length : 0) + "%";
}

// ---------- panels (left side) ----------
function renderPanels() {
  const by = DATA.by_layer;
  const layers = [...PANEL_LAYERS, "generalized"];
  const html = layers.map(layer => {
    const sids = by[layer] || [];
    return `<section class="panel" data-layer="${layer}">
      <h4>${esc(PANEL_TITLES[layer])} <span class="cnt">${sids.length}</span></h4>
      <div class="pfilter"><input placeholder="筛选 ${esc(layer)}…" data-pfilter="${layer}" oninput="window._pf(event)"></div>
      <ul class="nest" id="pl-${layer}"></ul>
    </section>`;
  }).join("");
  $("panels").innerHTML = html;
  // populate lists
  for (const layer of layers) renderPanelList(layer);
}

function renderPanelList(layer) {
  const sids = DATA.by_layer[layer] || [];
  const ul = $("pl-" + layer);
  if (!ul) return;
  const html = sids.map(sid => {
    const t = TBY[sid]; if (!t) return "";
    const ic = ICON[statusOf(sid)];
    const cur = sid === CUR ? " cur" : "";
    return `<li><div class="node${cur}" data-act="go" data-s="${esc(sid)}" title="${esc(t.task_logical_name || "")}"><span class="ic ${ic[1]}">${ic[0]}</span><span class="bid">${esc(sid)}</span><span class="nm">${esc(t.task_logical_name || "")}</span></div></li>`;
  }).join("");
  ul.innerHTML = html || `<li><div class="empty" style="padding:6px;font-size:11px">（无）</div></li>`;
}

window._pf = (e) => {
  const layer = e.target.dataset.pfilter;
  const q = e.target.value.trim().toLowerCase();
  const sids = DATA.by_layer[layer] || [];
  const ul = $("pl-" + layer);
  if (!ul) return;
  const html = sids.filter(sid => {
    const t = TBY[sid]; if (!t) return false;
    return !q || sid.toLowerCase().includes(q) || (t.task_logical_name || "").toLowerCase().includes(q);
  }).map(sid => {
    const t = TBY[sid];
    const ic = ICON[statusOf(sid)];
    const cur = sid === CUR ? " cur" : "";
    return `<li><div class="node${cur}" data-act="go" data-s="${esc(sid)}" title="${esc(t.task_logical_name || "")}"><span class="ic ${ic[1]}">${ic[0]}</span><span class="bid">${esc(sid)}</span><span class="nm">${esc(t.task_logical_name || "")}</span></div></li>`;
  }).join("");
  ul.innerHTML = html || `<li><div class="empty" style="padding:6px;font-size:11px">（无匹配）</div></li>`;
};

// ---------- navigation ----------
function go(sid, push) {
  if (!sid || !TBY[sid]) sid = DATA.by_layer.feature[0] || DATA.by_layer.atom[0] || null;
  if (!sid) return;
  CUR = sid;
  // FOCUS 自动跟随 layer(spec §5.1)
  const layer = TBY[sid].task_layer;
  FOCUS = (layer === "generalized") ? "main" : (PANEL_LAYERS.includes(layer) ? layer : "main");
  if (push !== false) history.replaceState(null, "", "#/t/" + sid);
  // 刷新左面板高亮(轻量:只切换 .cur)
  document.querySelectorAll("#panels .node").forEach(n => { n.classList.toggle("cur", n.dataset.s === sid); });
  renderMain(sid);
  // 滚动 CUR 到可视
  const curNode = document.querySelector(`#panels .node[data-s="${sid}"]`);
  if (curNode) curNode.scrollIntoView({ block: "nearest" });
}

function panelOrder(layer) { return DATA.by_layer[layer] || []; }
function navPrev() {
  if (!PANEL_LAYERS.includes(FOCUS)) { toast("切换面板先按 Tab"); return; }
  const list = panelOrder(FOCUS);
  const i = list.indexOf(CUR);
  if (i > 0) go(list[i - 1]);
}
function navNext() {
  if (!PANEL_LAYERS.includes(FOCUS)) { toast("切换面板先按 Tab"); return; }
  const list = panelOrder(FOCUS);
  const i = list.indexOf(CUR);
  if (i >= 0 && i < list.length - 1) go(list[i + 1]);
}

// ---------- main: task detail + embedded children ----------
function chips(arr, cls) {
  const seen = new Set(); const out = [];
  for (const ref of (arr || [])) {
    const s = short(ref); if (!s || seen.has(s) || !TBY[s]) continue;
    seen.add(s);
    const t = TBY[s];
    const ic = ICON[statusOf(s)];
    out.push(`<span class="chip ${cls || ""}" data-jump="${esc(s)}" title="${esc(s)} ${esc(t.task_logical_name || "")}"><span class="ic ${ic[1]}">${ic[0]}</span> ${esc(s)} ${esc(t.task_logical_name || "")}</span>`);
  }
  return out;
}

function chipListWithCollapse(arr, label) {
  const items = chips(arr);
  if (!items.length) return `<span style="color:var(--faint);font-size:11px">（无）</span>`;
  if (items.length <= COLLAPSE) return items.join("");
  const head = items.slice(0, 5).join("");
  const rest = items.slice(5).join("");
  return `${head}<span class="more-btn" data-act="more-chips">展开更多 (剩余 ${items.length - 5} 个)</span><span data-more-body hidden>${rest}</span>`;
}

function relList(rels) {
  return (rels || []).map(r => {
    const ctx = (r.propagated_context || []).map(c => c.context_name).join(",");
    return `<div class="rel"><span class="rt">${esc(r.relation_type || "")}</span> ${esc(short(r.from_task_ref || ""))}<span class="arr">→</span>${esc(short(r.to_task_ref || ""))}${
      r.requiredness && r.requiredness !== "required" ? ` <span class="tag">${esc(r.requiredness)}</span>` : ""}${
      r.condition_ref ? ` <span class="tag amber">if ${esc(short(r.condition_ref))}</span>` : ""}${
      ctx ? `<span class="ctx">[${esc(ctx)}]</span>` : ""}</div>`;
  }).join("");
}

function dpCard(d) {
  const opts = (d.options || []).map(o => {
    const imps = (o.impacts || []).map(im => `<div class="imp"><span class="e e-${esc(im.effect_type)}">${esc(im.effect_type)}</span><span>${esc(short(im.target_ref || ""))}</span><span style="color:var(--mute);font-family:inherit">${esc(im.effect_detail || "")}</span></div>`).join("");
    return `<div class="opt"><div class="on">▸ ${esc(o.option_name || "")}${o.option_value ? ` <span style="color:var(--mute);font-family:var(--mono)">=${esc(o.option_value)}</span>` : ""}</div>${imps}</div>`;
  }).join("");
  return `<div class="dp"><h4>${esc(d.decision_name || "")} <span style="font-size:11px;color:var(--mute);font-family:var(--mono)">(${esc(short(d.decision_id || ""))})</span></h4>
    <div class="meta">挂 ${esc(short(d.owner_task_ref || ""))} · ${esc(d.decision_type || "")} · ${esc(d.decision_question || "")}</div>${opts}</div>`;
}

function ruleCard(r) {
  const c = r.constraint || {};
  return `<div class="rulec"><div class="rh"><span class="sev ${esc(r.severity || "")}">${esc(r.severity || "")}</span>
    <b class="mono">${esc(short(r.rule_id || ""))}</b> <span style="color:var(--mute);font-size:11px">${esc(r.rule_type || "")}</span>
    <span>${esc(r.rule_name || "")}</span></div>
    <div class="cx">${esc(c.expression || "")}${r.violation_effect ? ` · 影响: ${esc(r.violation_effect)}` : ""}</div></div>`;
}

// renderChildren(sids, depth): depth 0=chip; depth 1=embedded L2 card(default collapsed); depth 2=不再渲染
function renderChildren(sids, depth) {
  if (!sids || !sids.length) return `<span style="color:var(--faint);font-size:11px">（无）</span>`;
  if (depth <= 0) {
    return chips(sids).join("") || `<span style="color:var(--faint);font-size:11px">（无）</span>`;
  }
  // depth >= 1: L2 卡片(默认折叠其内部 chip 列)
  return sids.map(sid => {
    const t = TBY[sid]; if (!t) return "";
    const ic = ICON[statusOf(sid)];
    const subSids = DATA.relation_targets[sid] || [];
    const subIds = subSids.map(s => TBY[s]?.task_id).filter(Boolean);
    const head = `<div class="ec-head" data-act="toggle-l2" data-s="${esc(sid)}">
      <span class="ec-tw">▸</span>
      <span class="ic ${ic[1]}">${ic[0]}</span>
      <span class="bid mono">${esc(sid)}</span>
      <span class="nm" style="max-width:240px;overflow:hidden;text-overflow:ellipsis">${esc(t.task_logical_name || "")}</span>
      <span style="color:var(--mute);font-size:10px;margin-left:auto">(${subSids.length} 子)</span>
    </div>`;
    const body = `<div class="ec-body" hidden>
      <div style="font-size:11px;color:var(--mute);margin-bottom:3px">${esc(t.task_layer)} · ${esc(t.task_category || "")}${t.ref ? ' · ref: ' + esc(short(t.ref)) : ""}</div>
      ${renderChildren(subSids, depth - 1)}
    </div>`;
    return `<div class="ec collapsed" data-ec-sid="${esc(sid)}">${head}${body}</div>`;
  }).join("");
}

function renderMain(sid) {
  const t = TBY[sid]; if (!t) { $("main").innerHTML = '<div class="empty">无</div>'; return; }
  const st = statusOf(sid);
  const L = t.task_layer;

  // 主区:参数 / 编排 / DP / rule / 复用 / 父容器
  let detail = "";
  const pb = t.parameter_bindings || [];
  if (pb.length) {
    detail = `<table class="tbl"><tbody>${pb.map(b => `<tr><td class="k">${esc(short(b.parameter_ref || ""))}</td><td>${
      b.binding_type ? `<span class="tag">${esc(b.binding_type)}</span>` : ""}${
      b.variable_source ? `<span class="tag green">${esc(b.variable_source)}</span>` : ""}${
      b.requiredness ? `<span class="tag ${b.requiredness === "optional" ? "" : "amber"}">${esc(b.requiredness)}</span>` : ""}${
      b.value != null ? ` <b>=${esc(b.value)}</b>` : ""}${
      b.decision_ref ? ` <span class="tag purple">→DP ${esc(short(b.decision_ref))}</span>` : ""}${
      b.source_ref ? ` <span style="color:var(--mute)">← ${esc(short(b.source_ref))}</span>` : ""}</td></tr>`).join("")}</tbody></table>`;
  }
  const rels = t.task_relations || [];
  if (rels.length) detail += `<div style="margin-top:6px">${relList(rels)}</div>`;

  const dps = DPS_BY[sid] || [];
  const rules = RULES_BY[sid] || [];
  const containers = DATA.tree.containers[sid] || [];

  // 编排下层(渲染 L1 内嵌区,含两级折叠)
  const subSids = DATA.relation_targets[sid] || [];
  let subSection = "";
  if (subSids.length) {
    subSection = `<section class="blk"><h3>编排下层 (${subSids.length})</h3>`;
    if (subSids.length > COLLAPSE) {
      const head3 = subSids.slice(0, COLLAPSE_LIGHT);
      const rest = subSids.slice(COLLAPSE_LIGHT);
      subSection += `<div data-l1-initial>${renderChildren(head3, 1)}</div>
        <span class="more-btn" data-act="more-l1">展开更多 (剩余 ${rest.length} 个)</span>
        <div data-l1-rest hidden>${renderChildren(rest, 1)}</div>`;
    } else {
      subSection += renderChildren(subSids, 1);
    }
    subSection += `</section>`;
  }

  $("main").innerHTML = `<div class="page">
    <header>
      <div class="row1">
        <span class="badge b-${L}">${L}</span>
        <h2 class="mono">${esc(sid)}</h2>
        <span class="pstatus ${st}">${esc(st)}</span>
        ${t.ref ? `<span class="ref mono">ref: ${esc(short(t.ref))}</span>` : ""}
      </div>
      <div class="intent">${esc(t.task_intent || "")}</div>
      <div class="kv"><span>category: ${esc(t.task_category || "")}</span><span>status: ${esc(t.status || "")}</span>${(t.source_evidence_ids || []).length ? `<span>证据: ${esc(t.source_evidence_ids.map(x => short(x) || x).join(", "))}</span>` : ""}${t._params ? `<span>${t._params} 参数</span>` : ""}${t._relations ? `<span>${t._relations} 编排边</span>` : ""}</div>
    </header>

    <section class="blk"><h3>task 详情</h3>${detail || '<div class="empty">无参数/编排</div>'}${t.notes ? `<div class="cx" style="margin-top:6px;background:#f8fafc;border:1px solid var(--line);padding:7px 10px;border-radius:5px">📝 ${esc(t.notes)}</div>` : ""}</section>

    ${subSection}

    <section class="blk"><h3>引用方 (${containers.length})</h3><div class="rellist">${chipListWithCollapse(containers.map(c => TBY[c]?.task_id).filter(Boolean))}</div></section>

    ${L === "atom" && (t._reuse_by || []).length ? `<section class="blk"><h3>复用面 (被 ${t._reuse_by.length} 个特性引用)</h3><div class="rellist">${chipListWithCollapse(t._reuse_by)}</div></section>` : ""}

    <section class="blk"><h3>其决策点 (${dps.length})</h3>${dps.length ? dps.map(dpCard).join("") : '<div class="empty">无</div>'}</section>
    <section class="blk"><h3>其规则 (${rules.length})</h3>${rules.length ? rules.map(ruleCard).join("") : '<div class="empty">无</div>'}</section>

    ${renderReview(sid, st)}
  </div>`;
}

function renderReview(sid, st) {
  const recs = (REV.records || {})[sid] || [];
  const hist = recs.slice().reverse().map(r => `<div class="hitem"><div class="hmeta"><b class="pstatus ${esc(r.verdict)}" style="font-size:9px;padding:2px 5px">${esc(r.verdict)}</b>${esc(r.ts)} · ${esc(r.reviewer || "")}</div>${r.note ? `<div class="note">${esc(r.note)}</div>` : ""}</div>`).join("");
  return `<section class="review">
    <h3 style="margin:0 0 4px;font-size:13px">审查(当前:<b class="pstatus ${st}" style="font-size:11px;padding:3px 7px">${esc(st)}</b>)</h3>
    <div style="font-size:11px;color:var(--mute);margin-bottom:6px">一次审查覆盖本 task + 其 rule + 其 DP;note 可点名具体对象。</div>
    <div class="vbtns">
      <button class="vbtn ok" data-verdict="通过">✓ 通过</button>
      <button class="vbtn bad" data-verdict="驳回">✕ 驳回</button>
      <button class="vbtn maybe" data-verdict="待补">◐ 待补</button>
    </div>
    <textarea id="rnote" placeholder="审查意见(可选;点"通过"可留空=快速批准)"></textarea>
    <div class="hist"><b style="font-size:12px">历史记录(${recs.length})</b>${hist || '<div class="empty" style="padding:10px">尚无记录</div>'}</div>
  </section>`;
}

async function postReview(verdict) {
  const sid = CUR; if (!sid) return;
  const note = ($("rnote") || {}).value || "";
  toast("提交中…");
  try {
    const r = await fetch("/api/review", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ object_id: sid, verdict, note }) });
    const d = await r.json();
    if (d.ok) {
      REV.records[sid] = d.records;
      $("rnote").value = "";
      renderStats();
      renderPanels();
      renderMain(sid);
      toast("已记录:" + verdict);
    } else toast("失败:" + (d.msg || ""));
  } catch (e) { toast("提交失败:" + e.message); }
}

// ---------- events ----------
document.addEventListener("click", (e) => {
  const t = e.target;
  const node = t.closest("[data-act='go']");
  if (node) { go(node.dataset.s); return; }
  const jump = t.closest("[data-jump]");
  if (jump) { go(jump.dataset.jump); return; }
  const vb = t.closest("[data-verdict]");
  if (vb) { postReview(vb.dataset.verdict); return; }
  // L2 卡片折叠切换(spec §3.5:仅 click 响应,不响应 Enter/Space)
  const l2 = t.closest("[data-act='toggle-l2']");
  if (l2) {
    const sid = l2.dataset.s;
    const card = document.querySelector(`.ec[data-ec-sid="${CSS.escape(sid)}"]`);
    if (!card) return;
    const body = card.querySelector(".ec-body");
    const tw = l2.querySelector(".ec-tw");
    const willOpen = body.hasAttribute("hidden");
    if (willOpen) body.removeAttribute("hidden"); else body.setAttribute("hidden", "");
    card.classList.toggle("collapsed", !willOpen);
    if (tw) tw.textContent = willOpen ? "▾" : "▸";
    return;
  }
  // "展开更多" chip 列表
  const more = t.closest("[data-act='more-chips']");
  if (more) {
    const sib = more.nextElementSibling;
    if (sib) { sib.removeAttribute("hidden"); more.remove(); }
    return;
  }
  // L1 内嵌区两级折叠
  const moreL1 = t.closest("[data-act='more-l1']");
  if (moreL1) {
    const sib = moreL1.nextElementSibling;
    if (sib) { sib.removeAttribute("hidden"); moreL1.remove(); }
    return;
  }
});

window.addEventListener("keydown", (e) => {
  // textarea focus 时,1/2/3 全部 no-op(避免吞用户输入数字;spec §3.6)
  if (e.target.tagName === "TEXTAREA") return;
  if (e.key === "ArrowLeft") navPrev();
  else if (e.key === "ArrowRight") navNext();
  else if (e.key === "1") postReview("通过");
  else if (e.key === "2") postReview("驳回");
  else if (e.key === "3") postReview("待补");
  else if (e.key === "Tab") {
    // FOCUS 循环:atom → compound → feature → main → atom(spec §5.1)
    e.preventDefault();
    const seq = ["atom", "compound", "feature", "main"];
    FOCUS = seq[(seq.indexOf(FOCUS) + 1) % seq.length];
    toast("焦点: " + (FOCUS === "main" ? "主区" : PANEL_TITLES[FOCUS]));
  }
});
window.addEventListener("hashchange", () => { const h = location.hash.match(/#\/t\/(.+)$/); if (h && h[1] !== CUR) go(h[1], false); });
window._nav = (k) => { if (k === "prev") navPrev(); else if (k === "next") navNext(); };

init();