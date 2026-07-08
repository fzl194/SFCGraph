---
id: UNC@20.15.2@MMLCommand@SET ISMFASMFRESET
type: MMLCommand
name: SET ISMFASMFRESET（设置I-SMF对A-SMF的故障恢复策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ISMFASMFRESET
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- A-SMF故障处理策略管理
status: active
---

# SET ISMFASMFRESET（设置I-SMF对A-SMF的故障恢复策略）

## 功能

**适用NF：SMF**

该命令用于设置I-SMF的A-SMF故障恢复功能。

## 注意事项

- 该命令执行后在下次A-SMF故障时生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ASMFRESEL | RATE | VORECOVERSW |
| --- | --- | --- |
| ON | 5 | OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ASMFRESEL | A-SMF故障重选开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定I-SMF和A-SMF的接口故障时，是否通过扫描任务释放在该I-SMF和A-SMF上建立的PDU会话，达到重建PDU会话的效果。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。<br>配置原则：无 |
| RATE | 扫描速率 | 可选必选说明：该参数在"ASMFRESEL"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于指定每个DS每秒扫描的会话数。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ISMFASMFRESET查询当前参数配置值。<br>配置原则：<br>DS个数 × 扫描速率 = 整系统扫描速率。<br>DS个数来源于如下命令输出结果中记录个数：<br>DSP FRAMEDBG: DBGSTR="SmcCtrlSvc coordinator all";如果结果没有分批显示，则记录个数为回显中“结果个数”字段的值减1；如果结果分批显示，则记录个数为最终的结果个数减1。 |
| VORECOVERSW | 语音业务快速恢复开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定I-SMF感知到A-SMF故障时，在该I-SMF上的语音会话进行业务请求时是否快速恢复语音业务。<br>数据来源：本端规划<br>取值范围：<br>- OFF（关闭）<br>- GRACEFUL_RECOVERY（优雅恢复）<br>- FORCE_RECOVERY（强制恢复）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ISMFASMFRESET查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [I-SMF对A-SMF的故障恢复策略（ISMFASMFRESET）](configobject/UNC/20.15.2/ISMFASMFRESET.md)

## 使用实例

设置A-SMF故障重选开关为开启，扫描速率为5，语音业务快速恢复开关关闭。

```
SET ISMFASMFRESET:ASMFRESEL=ON,RATE=5,VORECOVERSW=OFF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置I-SMF对A-SMF的故障恢复策略（SET-ISMFASMFRESET）_70382397.md`
