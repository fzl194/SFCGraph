## 第八章：License 前置门控

> 全部带宽控制特性的前置门控。来源：`three-layer-graph/04-command-graph.md` CMD-UDG-001/CMD-UNC-001、`01-business-graph.md` BusinessRule BR-BW-06、`feature-knowledge/cross-feature-analysis.md` §2/§5。

---

### K801: License 前置门控原理 [原理]

> BusinessRule BR-BW-06。

BWM/QoS/FUP/ADC 等策略类型**未启用 License 时，配置命令成功但功能不生效**，难以排查。License 是全部带宽控制特性的前置门控。

**关键隐性规则**：
- **UDG 与 UNC 的 License 编号体系完全独立**（发现四），需分别获取
- License 必须是配置流程的**第一步**（在 SA 特征库加载、BWM 全局使能之前）
- SET LICENSESWITCH 是元配置命令，控制后续特性功能可用性

---

### K802: UDG 侧 License 配置 [配置]

```mml
SET LICENSESWITCH:LICITEM="LKV3G5SABS01",SWITCH=ENABLE;   (SA-Basic)
SET LICENSESWITCH:LICITEM="LKV3G5PCCB01",SWITCH=ENABLE;   (PCC 基本功能)
SET LICENSESWITCH:LICITEM="LKV3G5TCSA01",SWITCH=ENABLE;   (BWM)
```

**UDG 侧典型 License 项**：
- SA-Basic：业务感知基础
- PCC 基本功能：PCC 框架基础
- BWM：带宽管理
- 各子特性按需开启

---

### K803: UNC 侧 License 配置 [配置]

```mml
SET LICENSESWITCH:LICITEM="LKV3TCBSA01",SWITCH=ENABLE;   (BWM UNC 侧)
```

**UNC 侧 License 独立**，不与 UDG 共享编号。

---

### K804: SET BANDWIDTHMNG — BWM 全局使能 [配置]

License 开启后，需全局使能 BWM 功能（BWM 场景前置）：

```mml
SET BANDWIDTHMNG:SWITCH=ENABLE;
```

参数：`SWITCH`（ENABLE/DISABLE）。

---

### K805: SA 特征库加载 [配置]

> Task T-008。SA-Basic 辐射范围最大，12 个特性直接依赖其业务识别能力。

```mml
LOD SIGNATUREDB:SAFILE="signature_db.dat";   (加载 SA 特征库)
LOD PARSERDB:PRFILE="parser_db.dat";         (加载解析库)
```

SA 引擎就绪后，L3/L4/L7 业务识别能力可用。后续 BWM/FUP/ADC/QoS 的业务匹配均依赖 SA。

---

### K806: SET SRVCOMMONPARA — SA 公共参数 [配置]

```mml
SET SRVCOMMONPARA:PARANAME="{name}",PARAVALUE="{value}";
```

配置 SA 引擎的公共参数（如识别模式、超时等）。

---

### K807: 前置门控完整链路 [配置]

带宽控制场景首次配置的前置门控完整顺序：
```
1. SET LICENSESWITCH（UDG 侧各 License 项）
2. LOD SIGNATUREDB / LOD PARSERDB（SA 特征库）
3. SET SRVCOMMONPARA（SA 公共参数，按需）
4. SET BANDWIDTHMNG:SWITCH=ENABLE（BWM 全局使能）
5. (UNC 侧) SET LICENSESWITCH + PCRF 组 + PCCFUNC
6. 开始业务级配置（BWMSERVICE/BWMCONTROLLER/...）
```

---

### K808: License 未开启的故障现象 [故障案例]

- 配置命令（ADD BWMSERVICE 等）执行**成功**但 BWM 策略不生效
- 业务流量未被限速/整形
- 无明确错误提示，排查困难

**排查方法**：LST LICENSESWITCH 检查对应 LICITEM 是否 ENABLE。
