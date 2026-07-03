# P1 步骤层重构追踪表 — UDG@20.15.2

> **范围**：仅 UDG（UNC 不在本轮）。共 90 个已建 task-feature（2-xxxxx），4 skip 见 task-index.md。
> **性质**：重构（把已有的改对），非新增。每个特性必须以其**激活/部署 md** 为真源（路径权威 `FeatureGraph/data/legacy/UDG_feature_files.csv`；具体激活 md 见各 task `source_evidence_ids`）。
> **方法**：①读激活 md（操作步骤+数据规划表"获取方法"列+任务示例脚本）②按 md 步骤结构核对/聚 compound ③复用 backbone(1-00001~04)按 §7.1 ④清伪 depends_on 边。
> **完整性判据（2026-07-02 增）**：特性 task 必须完整分解到命令层。若 md 操作步骤明示"详细配置参考X / 在X基础上配置Y"→ 完整配置=X+Y，必须把 X 的 compound/atom 引用编进来（差量特性，如 2-00006）；若 baseline 仅在"必备事项/前提条件"作外部前置→ 独立特性，不补（如 2-00007/08 等 24 个已 md 审计确认）。
> **形态判据**：单命令步骤=atom(不套compound)；≤2 atom 小特性=feature->atom 直挂(只清边)；3+ atom 且 md 分阶段=聚 compound。

## 状态总览
- STEP-OK(已有步骤层,需md复核): 17
- ATOM-CHAIN(直链,按atom数分流): 58
- SINGLE(单atom,直挂+清边): 13（原 11，2-00071/88 经 md 纠偏由 EMPTY 改 SINGLE）
- EMPTY(查md是否skip): 2（2-00078/79 确认纯概念 skip）
- 已 md 复核完成: 90 / 90（...批8：B3 起步 Portal/WebProxy/DNS/HTTP重定向；批9：B3 收尾 规则库2-00034(复用1-00001/03)+码率2-00035(md证伪backbone,纯BWM)+Shaping2-00038/小区负荷2-00040(清伪边)+STEP-OK 2-00036/37/39 复核，2 子 Agent + 主控复验；批10：B1 充电/PCC族 STEP-OK 14特性(2-00002~05/09~18)md复核,backbone 1-00001~04 引用全确认正确零yaml改动(印证充电族高质量存量)；后半 2-00012~18 详记(backbone 引用全确认正确,零伪边零dangling,2-00012一次重定向+2-00013 Referer核减+2-00014 IM REMARK_FPI+2-00015 IPv6 SA门控+2-00016 ADC双路径+2-00017 Shaping BWM6族+2-00018 QoS双触发)）
- **步骤库（compound）现状**：backbone 1-00001 计费三件套 / 1-00002 过滤链 / 1-00003 规则与用户模板绑定 / 1-00004 收尾（经 部署UPF md 验证）；1-00005 ICAP互通 / 1-00006 内容过滤策略链（2-00083）；1-00007~09 QoS复杂流分类B/C侧+策略组装 / 1-00010 DiffServ域映射 / 1-00011 ACL4规则（2-00065/66）；1-00016 APN级下行缓存 / 1-00017 全局下行缓存（2-00059/82 共享，§4.5.2 合并样板）；1-00012 地址池族（2-00020/25 共享，§4.5.2 合并样板）/ 1-00013 LoopBack接口族 / 1-00014 Tunnel接口族（2-00025）/ 1-00015 OSPF路由引入族（2-00027，与 2-00020 步骤2 Jaccard=1.0，未来迭代引用）/ 1-00018 路由策略族（2-00041，可复用 2-00047 BGP）/ 1-00019 OSPFv3路由引入族（2-00041，与 2-00027 OSPFv3 分支同构）/ 1-00020 IPv6接口组网族（2-00042，与 1-00013/14 同 atom 不同用途）/ 1-00021 L2TP激活前置（2-00045，§4.4.3 L2TP 相位聚合范例：两激活方式共享 License→VPNINST→GLOBALL2TP 相位，DP 0-00023 保留表达 changes_command_set 分叉）/ 1-00022 跨VPN外联口自动部署族（2-00047 BGP路由交叉，DP 0-00024 BFD二选一）/ 1-00023 IPSEC协商族（2-00067 IPSec，VNRS+IPSEC双配，DP 0-00033 多场景）/ 1-00024 IPFarm族（2-00057 IMS恢复，DP 0-00027/0-00028，与 Portal/WebProxy 同 atom 不同 SERVERTYPE）

## 逐特性清单

| task_id | feature_id | 名称 | 形态 | atoms | 重构动作 | 批次 | 状态 |
|---|---|---|---|---|---|---|---|
| 2-00001 | GWFD-020301 | 内容计费基本功能 | STEP-OK | 0 | md复核步骤结构(轻) | B1 充电/PCC族 | ✅done |
| 2-00002 | GWFD-020300 | 在线计费 | STEP-OK | 3 | ✅md复核:backbone链+0-00016/17/18在线专属(DP0-00004)对齐;零改动 | B1 充电/PCC族 | ✅done |
| 2-00003 | GWFD-010171 | 离线计费 | STEP-OK | 1 | ✅md复核:backbone链+0-00018(URRFAILACTION)+USAGERPTMODE=OFFLINE(DP0-00001);零改动 | B1 充电/PCC族 | ✅done |
| 2-00004 | GWFD-010173 | 融合计费 | STEP-OK | 0 | ✅md复核:backbone链对齐11步聚合;URRGROUP双URR(在线+离线);零改动 | B1 充电/PCC族 | ✅done |
| 2-00005 | GWFD-020351 | PCC基本功能 | STEP-OK | 3 | ✅md复核:0-00019→0-00003→1-00002→1-00003→0-00015对齐;动态/本地DP0-00007;零改动 | B1 充电/PCC族 | ✅done |
| 2-00006 | GWFD-020307 | TCP重传识别 | ATOM-CHAIN | 2 | ✅完整性修正:md明示"详细配置参考部署UPF"→补全 backbone 1-00001~04+差量0-00013(镜像2-00002);原仅编差量2命令是漏 | B1 充电/PCC族 | ✅done |
| 2-00007 | GWFD-020308 | 7层流量统计 | SINGLE | 1 | 确认feature->atom直挂+清伪边 | B1 充电/PCC族 | ✅done |
| 2-00008 | GWFD-020305 | 终端异常下行流量检测 | ATOM-CHAIN | 2 | 小特性:清伪边(无需compound) | B1 充电/PCC族 | ✅done |
| 2-00009 | GWFD-020302 | 基于业务时长的计费 | STEP-OK | 1 | ✅md复核:backbone链+license对齐;md脚本未展示TIME差异(文档缺口)记演进债;零改动 | B1 充电/PCC族 | ✅done |
| 2-00010 | GWFD-020303 | 基于业务流量的计费 | STEP-OK | 1 | ✅md复核:backbone链+metering=VOLUME对齐;零改动 | B1 充电/PCC族 | ✅done |
| 2-00011 | GWFD-020306 | 支持事件计费 | STEP-OK | 1 | ✅md复核:backbone链对齐;md未展示EVENT差异(文档缺口)记演进债;零改动 | B1 充电/PCC族 | ✅done |
| 2-00012 | GWFD-020356 | 计费信息实时提醒 | STEP-OK | 5 | ✅md复核确认(backbone引用正确:0-00022/23/24一次重定向+1-00001计费三件套+1-00002过滤链+1-00003规则绑定+0-00015);零伪边零dangling;REFRESHTYPE=USERPROFILE末位合理 | B1 充电/PCC族 | ✅done |
| 2-00013 | GWFD-020304 | 关联URL核减 | STEP-OK | 5 | ✅md复核确认(0-00019+1-00001三件套+L7子链0-00006/07/09无三四层FILTER+1-00003+0-00015);ISREFEREREN=ENABLE feature级;零伪边零dangling | B1 充电/PCC族 | ✅done |
| 2-00014 | GWFD-020359 | IM类业务无线资源管控 | STEP-OK | 4 | ✅md复核确认(1-00002过滤链any+0-00027 SIGNATUREDB+0-00009 PROTBINDFLOWF+1-00003+0-00015);REMARK_FPI演进债记review;零伪边 | B1 充电/PCC族 | ✅done |
| 2-00015 | GWFD-020352 | IPv6 SA | STEP-OK | 7 | ✅md复核确认(1-00002 IPv6+0-00027/28/29/30 PCC动作链DISCARD+1-00003+0-00015);不复用1-00001(md无独立URR);零伪边零dangling | B1 充电/PCC族 | ✅done |
| 2-00016 | GWFD-020357 | 增强的ADC基本功能 | STEP-OK | 3 | ✅md复核确认(双路径DP0-00011:ADC规则/复用PCC规则;1-00002+0-00031 ADCPARA+1-00001仅路径B+1-00003+0-00015);零伪边 | B1 充电/PCC族 | ✅done |
| 2-00017 | GWFD-020354 | 基于业务的Shaping | STEP-OK | 10 | ✅md复核确认(BWM6族0-00032~37双链汇于BWMRULE;1-00002+1-00003+0-00020 APN前置+0-00015);零伪边零dangling;propagation全核 | B1 充电/PCC族 | ✅done |
| 2-00018 | GWFD-020358 | 业务触发的QoS保证 | STEP-OK | 8 | ✅md复核确认(双路径DP0-00012 L7/L3L4;0-00038 QOSPROP+0-00039/40 L7专属分支+1-00002+1-00003+0-00015);UPGLBPMPARA缺命令§6-A债 | B1 充电/PCC族 | ✅done |
| 2-00019 | GWFD-020381 | 会话类QoS保证 | ATOM-CHAIN | 2 | ✅回填QOSCAR(0-00070)+APNQOSATTR,删stale误引用,清伪边;QOSSHAPE仍defer | B2 接入/路由/过载 | ✅done |
| 2-00020 | GWFD-010104 | 地址分配方式 | ATOM-CHAIN | 8 | ✅建1-00012地址池族+补建步骤2下行路由(6 atom) | B2 接入/路由/过载 | ✅done |
| 2-00021 | GWFD-010108 | 用户面地址自动检测 | SINGLE | 1 | ✅清feature-feature伪depends_on,降级note | B2 接入/路由/过载 | ✅done |
| 2-00022 | GWFD-010151 | 接入控制 | ATOM-CHAIN | 2 | ✅md复核确认正确(零改动) | B2 接入/路由/过载 | ✅done |
| 2-00023 | GWFD-010251 | 系统过载控制 | ATOM-CHAIN | 2 | ✅md复核;DEACTIVERATE/SOFTPARA atom仍缺保持defer | B2 接入/路由/过载 | ✅done |
| 2-00024 | GWFD-010102 | 路径管理 | ATOM-CHAIN | 4 | ✅md复核:parallel_with无需compound | B2 接入/路由/过载 | ✅done |
| 2-00025 | GWFD-010107 | 静态地址用户路由冗余 | ATOM-CHAIN | 16 | ✅复用1-00012+建1-00013/14(接口族) | B2 接入/路由/过载 | ✅done |
| 2-00026 | GWFD-010201 | QoS与流量管理 | ATOM-CHAIN | 8 | ✅md复核DP0-00016三方向;评估后不引用1-00010(避免割裂一体化任务) | B2 接入/路由/过载 | ✅done |
| 2-00027 | GWFD-010155 | Untrusted Non-3GPP | ATOM-CHAIN | 14 | ✅建1-00015 OSPF族(DP0-00017保留) | B2 接入/路由/过载 | ✅done |
| 2-00028 | GWFD-010253 | 防DDoS功能 | ATOM-CHAIN | 2 | ✅md复核确认正确(零改动) | B2 接入/路由/过载 | ✅done |
| 2-00029 | GWFD-010296 | NB-IoT终端标准接入 | SINGLE | 1 | ✅md复核确认正确(零改动) | B2 接入/路由/过载 | ✅done |
| 2-00030 | GWFD-110281 | 用户Portal | ATOM-CHAIN | 19 | ✅引用5 compound(1-00024 IPFarm族+1-00001/02/03/04 backbone);双规则SMARTREDIRECT+PCC;清可疑parallel边 | B3 业务感知 | ✅done |
| 2-00031 | GWFD-110282 | Web Proxy | ATOM-CHAIN | 16 | ✅引用4 compound(无七层);RULE=WEBPROXY+SVRIP维度;清draft误用must_be_last(REFRESHSRV实为mid-flow) | B3 业务感知 | ✅done |
| 2-00032 | GWFD-110283 | DNS纠错 | ATOM-CHAIN | 10 | ✅复用1-00002过滤链;DNS专属(ERRORCODE/DNSOVERWRITING)feature级;修parallel_with误用 | B3 业务感知 | ✅done |
| 2-00033 | GWFD-110284 | HTTP智能重定向 | ATOM-CHAIN | 10 | ✅复用1-00002过滤链;HTTP重定向专属(EXTENDEDFILTER/SMARTHTTPREDIR)feature级 | B3 业务感知 | ✅done |
| 2-00034 | GWFD-110321 | 支持内置百万级业务规则库 | ATOM-CHAIN | 11 | ✅复用1-00001计费三件套+1-00003规则绑定;2×REFRESHSRV mid-flow;OTT专属feature级 | B3 业务感知 | ✅done |
| 2-00035 | GWFD-110301 | 基于终端系统的码率差异化控制 | ATOM-CHAIN | 9 | ✅md证伪backbone复用(纯BWM域Jaccard=0);feature→atom直挂;draft→inferred | B3 业务感知 | ✅done |
| 2-00036 | GWFD-110302 | 基于上下行解耦的视频承载信令控制 | STEP-OK | 9 | ✅md复核步骤结构对齐;复用1-00002过滤链(含七层PROTBINDFLOWF变体)+1-00003规则绑定;QOSPROP(DECOUPLINGSW=ENABLE,rule0-00046)feature级;draft→inferred | B3 业务感知 | ✅done |
| 2-00037 | GWFD-110312 | 基于业务累计流量的策略控制 | STEP-OK | 8 | ✅md复核步骤结构对齐;复用1-00002+1-00003+计费三件套atom;ADD URR×2(ONLINE+MONITORINGKEY同atom0-00001)+URRGROUP双引用(cp_red+urrgroup1);draft→inferred | B3 业务感知 | ✅done |
| 2-00038 | GWFD-110313 | 基于智能Shaping的组级带宽控制 | ATOM-CHAIN | 3 | ✅md复核;清2条feature→atom伪depends_on(Shaping前置降级note);draft→inferred | B3 业务感知 | ✅done |
| 2-00039 | GWFD-110331 | 基于业务流标识的无线资源优化 | ATOM-CHAIN | 9 | ✅md复核;复用1-00002过滤链(无七层);SET FPIFUNC(0-00109)feature级触发器;ADD RULE×2(PCC+REMARK_FPI同atom0-00010,rule0-00049);md无USERPROFILE/RULEBINDING故不引1-00003;draft→inferred | B3 业务感知 | ✅done |
| 2-00040 | GWFD-110332 | 基于小区负荷上报的无线资源优化 | ATOM-CHAIN | 3 | ✅md复核2atom直挂;draft→inferred | B3 业务感知 | ✅done |
| 2-00041 | GWFD-020401 | IPv6承载上下文 | ATOM-CHAIN | 10 | ✅建1-00018路由策略族+1-00019 OSPFv3族 | B4 IPv6/VPN/HTTP识别 | ✅done |
| 2-00042 | GWFD-020402 | N6/Gi/SGi接口IPv6组网 | ATOM-CHAIN | 11 | ✅建1-00020 IPv6接口组网族 | B4 IPv6/VPN/HTTP识别 | ✅done |
| 2-00043 | GWFD-020403 | IPv4v6双栈接入 | ATOM-CHAIN | 7 | ✅复用1-00012地址池族(6→3边);双栈参数记演进债 | B4 IPv6/VPN/HTTP识别 | ✅done |
| 2-00044 | GWFD-020406 | IPv6 Prefix Delega | ATOM-CHAIN | 12 | ✅白名单链复用1-00012;OSPFv3含INTERFACE保持feature级(Jaccard0.75) | B4 IPv6/VPN/HTTP识别 | ✅done |
| 2-00045 | GWFD-020412 | L2TP VPN | ATOM-CHAIN | 13 | ✅建1-00021 L2TP激活前置(共享相位 License→VPNINST→GLOBALL2TP),DP0-00023保留 | B4 IPv6/VPN/HTTP识别 | ✅done |
| 2-00046 | GWFD-020422 | Direct Tunnel功能 | SINGLE | 1 | ✅depends_on→contains修正,md复核仅license | B4 IPv6/VPN/HTTP识别 | ✅done |
| 2-00047 | GWFD-020423 | 支持路由交叉功能(BGP Inter | ATOM-CHAIN | 9 | ✅建1-00022跨VPN自动部署族;0-00147三命令聚合债note;DP0-00024保留 | B4 IPv6/VPN/HTTP识别 | ✅done |
| 2-00048 | GWFD-110201 | HTTP2.0 Host识别 | ATOM-CHAIN | 11 | ✅复用backbone 1-00001计费三件套;L7FILTER变体+REFRESHSRV顺序按md直挂 | B4 IPv6/VPN/HTTP识别 | ✅done |
| 2-00049 | GWFD-110202 | HTTP2.0协议回落 | ATOM-CHAIN | 4 | ✅md复核三级开关链;补contains;笔误0-00148→0-00065修正 | B4 IPv6/VPN/HTTP识别 | ✅done |
| 2-00050 | GWFD-110203 | HTTPS业务地址识别 | ATOM-CHAIN | 18 | ✅复用backbone 1-00001/02/03;HTTPS必选+DNS可选(DP0-00025)两路径;18→13边 | B4 IPv6/VPN/HTTP识别 | ✅done |
| 2-00051 | GWFD-110251 | HTTP3.0 Host识别 | ATOM-CHAIN | 10 | ✅复用backbone 1-00001;QUIC开关+PROTBINDFLOWF无L7FILTER变体;REFRESHSRV顺序按md | B4 IPv6/VPN/HTTP识别 | ✅done |
| 2-00052 | GWFD-110252 | HTTP3.0 Host分析 | ATOM-CHAIN | 11 | ✅复用backbone 1-00001;L7FILTER URL变体;修draft propagated_context伪边;draft→inferred | B4 IPv6/VPN/HTTP识别 | ✅done |
| 2-00053 | GWFD-020251 | VoLTE基础语音业务 | ATOM-CHAIN | 4 | ✅md复核4atom直挂;IMS信令分类器多协议迭代note;draft→inferred | B5 语音/NB-IoT/QoS/ACL/IPSec | ✅done |
| 2-00054 | GWFD-020281 | VoNR基础语音业务 | SINGLE | 1 | ✅清feature→atom伪边(expands_to→contains);draft→inferred | B5 语音/NB-IoT/QoS/ACL/IPSec | ✅done |
| 2-00055 | GWFD-020282 | EPS Fallback | SINGLE | 1 | ✅清伪边;删feature→feature depends_on降级note;draft→inferred | B5 语音/NB-IoT/QoS/ACL/IPSec | ✅done |
| 2-00056 | GWFD-020252 | SRVCC | SINGLE | 1 | ✅清feature→atom depends_on→contains | B5 语音/NB-IoT/QoS/ACL/IPSec | ✅done |
| 2-00057 | GWFD-020253 | P-CSCF故障时IMS业务恢复 | ATOM-CHAIN | 6 | ✅建1-00024 IPFarm族;VPN/LOGICINF复用;DP0-00027/28保留 | B5 语音/NB-IoT/QoS/ACL/IPSec | ✅done |
| 2-00058 | GWFD-020254 | VoLTE业务快速恢复 | SINGLE | 1 | ✅清feature→atom depends_on→contains | B5 语音/NB-IoT/QoS/ACL/IPSec | ✅done |
| 2-00059 | GWFD-110601 | NB-IoT eDRX模式 | STEP-OK | 6 | ✅共享1-00016/17 | B5 语音/NB-IoT/QoS/ACL/IPSec | ✅done |
| 2-00060 | GWFD-110606 | 基于信令面的数据传输 | ATOM-CHAIN | 3 | ✅md复核;删feature→feature部署备注伪边 | B5 语音/NB-IoT/QoS/ACL/IPSec | ✅done |
| 2-00061 | GWFD-110607 | Non-IP数据传输 | ATOM-CHAIN | 3 | ✅md复核;删feature→feature部署备注伪边 | B5 语音/NB-IoT/QoS/ACL/IPSec | ✅done |
| 2-00062 | GWFD-110611 | 基于APN的NB-IoT终端接入速率 | ATOM-CHAIN | 2 | ✅md复核;删feature→feature部署备注伪边 | B5 语音/NB-IoT/QoS/ACL/IPSec | ✅done |
| 2-00063 | GWFD-110612 | 基于服务PLMN的NB-IoT终端接 | ATOM-CHAIN | 2 | ✅md复核;删feature→feature部署备注伪边 | B5 语音/NB-IoT/QoS/ACL/IPSec | ✅done |
| 2-00064 | IPFD-015002 | GRE | ATOM-CHAIN | 5 | ✅复用1-00013 LoopBack接口族;GRE/路由/增强feature级;DP0-00030保留 | B5 语音/NB-IoT/QoS/ACL/IPSec | ✅done |
| 2-00065 | IPFD-012001 | QoS | STEP-OK | 12 | ✅建1-00007/08/09/10 | B5 语音/NB-IoT/QoS/ACL/IPSec | ✅done |
| 2-00066 | IPFD-012002 | ACL | STEP-OK | 5 | ✅建1-00011+直挂0-00209 | B5 语音/NB-IoT/QoS/ACL/IPSec | ✅done |
| 2-00067 | IPFD-015004 | IPSec功能 | ATOM-CHAIN | 16 | ✅建1-00023 IPSEC协商族;VNRS接口链+IPSECINTFCFG must_be_last feature级;DP0-00033保留;16→12边 | B5 语音/NB-IoT/QoS/ACL/IPSec | ✅done |
| 2-00068 | GWFD-020154 | 用户面负载信息上报 | ATOM-CHAIN | 2 | ✅md复核License→PFCPLOADRPT对齐;零改动;draft→inferred | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00070 | GWFD-020161 | CU Full Mesh组网(UPF | ATOM-CHAIN | 2 | ✅md复核License→CPTEIDUALOC对齐;零改动 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00071 | GWFD-020162 | 用户面会话过载控制 | EMPTY | 0 | ✅纠偏:非EMPTY!md有SET SESSCHKFUNC(atom0-00220),补contains边 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00072 | GWFD-110910 | 支持Routing Behind M | ATOM-CHAIN | 5 | ✅md复核;专属命令零backbone复用;DP0-00035;零改动 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00073 | GWFD-110921 | 支持TWAMP | ATOM-CHAIN | 8 | ✅md复核;Full/Light双模式DP0-00036;TWAMP专属命令零backbone复用;零改动 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00074 | GWFD-110941 | 基于基站粒度的IPSQM | ATOM-CHAIN | 5 | ✅md复核;IPSQM专属命令零backbone复用;零改动 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00075 | GWFD-110641 | eMTC eDRX模式 | ATOM-CHAIN | 6 | ✅复用1-00016/1-00017下行缓存族(第3个eDRX,与2-00059/82 Jaccard=1.0);NORMALUSER演进债 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00076 | GWFD-110646 | 基于APN的eMTC终端接入速率控制 | ATOM-CHAIN | 2 | ✅md复核License→ADD APN对齐;零改动 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00077 | GWFD-110647 | 基于服务PLMN的eMTC终端接入速 | ATOM-CHAIN | 2 | ✅md复核License→ADD APN(可选)对齐;零改动 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00078 | NPFD-010000 | 配置管理 | EMPTY | 0 | ✅md确认skip(纯概念特性,仅EXP导出/查询类) | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00079 | NPFD-010004 | 设备管理-自动化配置 | EMPTY | 0 | ✅md确认skip(定义/原理/约束,无操作步骤无命令) | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00080 | NPFD-010014 | 支持NTP功能 | SINGLE | 1 | ✅md复核ADD NTPSVR(0-00248)对齐;零改动 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00081 | GWFD-020101 | 支持Reflective QoS | SINGLE | 1 | ✅md复核License(0-00019)激活类;零改动 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00082 | GWFD-110661 | 5G eDRX模式 | STEP-OK | 6 | ✅共享1-00016/17 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00083 | GWFD-110471 | URL过滤基本功能 | STEP-OK | 26 | ✅已重构:建1-00005/06+重用1-00001/03 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00084 | GWFD-020482 | 入不转板功能 | ATOM-CHAIN | 8 | ✅md复核确认(零改动,已inferred);feature→atom直挂(地址分配链与1-00012结构异:无APN步+加IPALLOCRULE,Jaccard<0.7不复用);precedes链0-00249→0-00056→POOL链→0-00250对齐md脚本序;演进债POOLTYPE=LOCAL/MASK必填记rule0-00094 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00085 | GWFD-111201 | 网络加速卡流量加速单元 | SINGLE | 1 | ✅md复核License(0-00019)激活类;零改动 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00087 | GWFD-112002 | 5G-A高通量会话 | ATOM-CHAIN | 2 | ✅md复核License→FLOWLETPARA对齐;零改动;draft→inferred | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00088 | GWFD-020451 | 端到端用户跟踪 | SINGLE | 1 | ✅纠偏:非EMPTY!md有SET LICENSESWITCH(0-00019),补contains边 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00089 | GWFD-112001 | Proxy UPF漫游功能 | ATOM-CHAIN | 11 | ✅重构:draft→inferred;复用1-00002过滤链(三四层加密检测,Jaccard0.83)+1-00003规则绑定(DP0-00041 gate);feature专属0-00280 SET NETYPE+0-00028 PCCACTIONPROP(阻断/通过双动作)+0-00003 PCCPOLICYGRP(URR组从已配数据获取,不引1-00001);relation_id 0-01850~0-01859 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00090 | GWFD-110404 | HTTPS业务行为识别 | ATOM-CHAIN | 3 | ✅md复核;专属三步链零backbone复用;DP0-00042 CFGPROTMODE;draft→inferred | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00091 | GWFD-112000 | 双故障Bypass | ATOM-CHAIN | 12 | ✅重构:draft→inferred;双任务(DP0-00043 gate缺省承载链);复用1-00002过滤链(两任务各一实例)+1-00001计费三件套(任务一双URR/任务二三URR)+1-00003规则绑定(任务二USERPROFILE共享);feature专属0-00282 SET IMSBYPASS+0-00038 QOSPROP+双REFRESHSRV模式(mid USERPROFILE+末ALL);relation_id 0-01860~0-01876 | B6 网管/eDRX/URL过滤/转发 | ✅done |
| 2-00092 | GWFD-020531 | 通用DNN漫游分流 | ATOM-CHAIN | 2 | ✅md复核License→RTSDNNPARA;公网/专网角色由rule0-00103;零改动;draft→inferred | B6 网管/eDRX/URL过滤/转发 | ✅done |
