# R5: 网络切片 + 专网策略 — 规则挖掘

## 0. 探索范围

| 领域 | 核心命令 |
|------|---------|
| 网络切片标识 | ADD SNSSAI |
| 切片接口绑定 | ADD SNSSAIUPINTF |
| 切片实例信息 | ADD SLICEINSTINFO |
| 专网动态分流 | SET DEDICATEDLBO |

---

## 1. 命令链路图

```
ADD SNSSAI (切片选择标识: SST + SD)
  ├→ ADD SNSSAIUPINTF (切片→N3逻辑接口绑定)
  ├→ ADD SNSSAIBWMUSRG (切片→BWM用户组绑定，见R3)
  ├→ ADD POOLGRPMAP (切片维度→地址池映射，见R2)
  └→ ADD SLICEINSTINFO (切片实例信息: NSIINFO + NSSIID)

SET DEDICATEDLBO (专网UPF动态分流功能开关)
```

---

## 2. 显式规则

| # | 规则 | 来源 | 严重度 |
|---|------|------|--------|
| R5-E01 | SNSSAI 最大 8192 条 | ADD SNSSAI | 警告 |
| R5-E02 | SNSSAIUPINTF 是高危命令，变更可能导致业务中断 | ADD SNSSAIUPINTF | 风险 |
| R5-E03 | SNSSAIUPINTF 默认接口(N3if1/1/0, Saif1/1/0)不能绑定 | ADD SNSSAIUPINTF | 错误 |
| R5-E04 | SNSSAIUPINTF 不支持 INSTANCE 数据面接口模式 | ADD SNSSAIUPINTF | 错误 |
| R5-E05 | SNSSAIUPINTF: MBS 会话的 n3mbif 不能绑定 | ADD SNSSAIUPINTF | 错误 |
| R5-E06 | SNSSAIUPINTF 只影响新的 PFCP 消息 | ADD SNSSAIUPINTF | 生效时机 |
| R5-E07 | SNSSAI 的 SST 必须在 0-255 范围内 | ADD SNSSAI | 错误 |
| R5-E08 | SNSSAI 的 SD 必须是 6 位十六进制 | ADD SNSSAI | 错误 |
| R5-E09 | SLICEINSTINFO 最大 128 条 | ADD SLICEINSTINFO | 警告 |

---

## 3. 隐式规则

### 3.1 切片标识跨命令一致性（slice_id_consistency）

**发现**：SST+SD 作为切片标识，在 SNSSAI、SNSSAIUPINTF、SNSSAIBWMUSRG、POOLGRPMAP 中都被引用，必须保持一致。

**证据**：
- ADD SNSSAI: 定义 SST+SD
- ADD SNSSAIUPINTF: 引用 SST+SD 绑定到接口
- ADD SNSSAIBWMUSRG: 引用 SST+SD 绑定到 BWM 用户组
- ADD POOLGRPMAP: 可能引用切片维度

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R5-I01 | SNSSAIUPINTF/SNSSAIBWMUSRG 引用的 SST+SD 必须在 SNSSAI 中已定义 | SNSSAI + 多命令 | 引用可达性 |
| R5-I02 | 删除 SNSSAI 前，需先删除引用它的 SNSSAIUPINTF 和 SNSSAIBWMUSRG | SNSSAI + 多命令 | 删除顺序 |
| R5-I03 | SD 缺省为 "ffffff"，引用时如果省略 SD 需确认与定义一致 | SNSSAI | 默认值一致性 |

### 3.2 切片接口绑定完整性（slice_interface_coverage）

**发现**：如果某个切片没有通过 SNSSAIUPINTF 绑定到 N3 接口，则该切片的用户数据面可能无法正确路由。

**证据**：
- ADD SNSSAIUPINTF: 只影响新的 PFCP 消息
- 未绑定的切片使用默认接口

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R5-I04 | 每个在用的 SNSSAI 应至少有一个 SNSSAIUPINTF 绑定（除非使用默认接口） | SNSSAI + SNSSAIUPINTF | 查找表覆盖度 |
| R5-I05 | 同一 SST+SD 绑定到不同 N3 接口时，流量可能分散到不同路径 | SNSSAIUPINTF | 一致性 |

### 3.3 默认对象保护（default_object_protection）

**发现**：SNSSAIUPINTF 禁止绑定默认接口（N3if1/1/0, Saif1/1/0），这是一种系统保护机制。

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R5-I06 | 默认接口是系统保留的，不能被切片绑定覆盖 | SNSSAIUPINTF | 系统保护 |
