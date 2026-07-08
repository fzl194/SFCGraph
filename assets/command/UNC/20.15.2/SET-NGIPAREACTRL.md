---
id: UNC@20.15.2@MMLCommand@SET NGIPAREACTRL
type: MMLCommand
name: SET NGIPAREACTRL（设置基于位置的地址分配控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NGIPAREACTRL
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- IP细分管理
- 5G地址细分控制参数
status: active
---

# SET NGIPAREACTRL（设置基于位置的地址分配控制参数）

## 功能

**适用NF：AMF**

该命令用于设置“基于位置的地址分配”的策略。

## 注意事项

- 该命令执行后立即生效。

- 相同流程中，对于同一种原因值映射配置，ADD NGCAUSEMAP命令优先级高于SET NGIPAREACTRL。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| DEAUSRSW | NGMMCAUSE | VONRDELAYREL |
| --- | --- | --- |
| OFF | 15 | OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEAUSRSW | 用户下线开关 | 可选必选说明：可选参数<br>参数含义：参数用于设置用户下线开关。若用户下线开关打开，系统会启动扫描，将已经在细分区域内注册的5G用户进行下线。对于本网用户，系统发起PDU会话去激活；对于漫游用户，系统发起网络侧去注册，去注册原因值通过“NGMMCAUSE(去注册原因值)”参数设置。当用户下线开关打开后增删细分区域或者增删细分DNN，系统会自动启动扫描任务。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（开启）”：开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGIPAREACTRL查询当前参数配置值。<br>配置原则：无 |
| NGMMCAUSE | 去注册原因值 | 可选必选说明：可选参数<br>参数含义：该参数表示在启用“基于位置的地址分配”功能后，UNC去注册漫游用户，或者拒绝漫游用户注册请求的原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~111。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGIPAREACTRL查询当前参数配置值。<br>配置原则：<br>系统初始设置值15，代表的含义为：#15 no suitable cells in tracking area。 |
| VONRDELAYREL | 语音会话延迟下线开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示语音会话延迟下线功能开关。当用户跨管控区移动导致AMF发起PDU会话去激活流程时，若参数设置为“ON”，语音会话携带定制原因值“REL_DUE_TO_ADR_SUBDV_CONSD_IMS”，语音通话结束后再触发会话重建，确保通话过程中会话不中断；若参数设置为“OFF”，语音会话携带原因值“REL_DUE_TO_REACTIVATION”，立即触发会话重建，导致语音通话中断。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（开启）”：开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGIPAREACTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGIPAREACTRL]] · 基于位置的地址分配控制参数（NGIPAREACTRL）

## 使用实例

对于细分区域的用户下线，对于漫游用户的去注册原因值设置为 #15 no suitable cells in tracking area。

```
SET NGIPAREACTRL: DEAUSRSW=ON, NGMMCAUSE=15;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置基于位置的地址分配控制参数（SET-NGIPAREACTRL）_96243157.md`
