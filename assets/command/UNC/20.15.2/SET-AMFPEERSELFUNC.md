---
id: UNC@20.15.2@MMLCommand@SET AMFPEERSELFUNC
type: MMLCommand
name: SET AMFPEERSELFUNC（设置AMF对端选择功能参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AMFPEERSELFUNC
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 可靠性管理
- AMF对端选择功能管理
status: active
---

# SET AMFPEERSELFUNC（设置AMF对端选择功能参数）

## 功能

**适用NF：AMF**

该命令用于控制不同场景下AMF选择对端的功能。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SCPSEPPRESEL | NFLOCATION | SCPRESELEN | AUSFRESELEN |
| --- | --- | --- | --- |
| OFF | UDM-1&SMF-1 | OFF | ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCPSEPPRESEL | SCP/SEPP重选开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定如下场景SCP/SEPP故障，导致业务消息无法发送给对端NF，是否开启SCP/SEPP重选功能：Model C/D模式下近端SCP故障；漫游场景下SEPP故障。当开关置为“ON(开启)”时表示上述场景下重选SCP/SEPP；当开关置为“OFF(关闭)”时表示上述场景下不重选SCP/SEPP。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（开启）”：开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPEERSELFUNC查询当前参数配置值。<br>配置原则：无 |
| NFLOCATION | 支持使用Location的对端NF类型 | 可选必选说明：可选参数<br>参数含义：对端NF支持使用多个IP地址跟AMF对接场景下，且对端NF类型属于该参数配置的范围，AMF支持使用该NF通过Location信元携带的地址进行后续消息交互。<br>当对端NF为UDM、SMF时，只有软参Dword71 Bit26的值为“1”，该参数才生效。<br>AMF、NSSF为预留字段，当前AMF暂不支持通过Location信元携带的地址进行后续消息交互。<br>若AMF使用Model D模式与对端NF通信，该参数不生效。<br>数据来源：全网规划<br>取值范围：<br>- UDM（UDM）<br>- SMF（SMF）<br>- AMF（AMF）<br>- SMSF（SMSF）<br>- PCF（PCF）<br>- AUSF（AUSF）<br>- NSSF（NSSF）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPEERSELFUNC查询当前参数配置值。<br>配置原则：无 |
| SCPRESELEN | SCP重选增强开关 | 可选必选说明：该参数在"SCPSEPPRESEL"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于指定Model C场景下，当SCP返回失败响应并指示近端SCP故障时，是否针对响应码504 Gateway Timeout且ProblemDetails为“TARGET_NF_NOT_REACHABLE”时进行SCP重选增强处理。当开关置为“ON(开启)”时表示上述场景下只重选对端NF，不重选SCP；当开关置为“OFF(关闭)”时表示上述场景下只重选SCP；<br>当本开关设置为“ON（开启）”时，是否重选对端NF还受NFType的重选功能开关控制。<br>该参数当前仅对LMF网元生效，对其他网元不生效。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（开启）”：开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPEERSELFUNC查询当前参数配置值。<br>配置原则：无 |
| AUSFRESELEN | AUSF重选增强开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制对端AUSF返回5xx错误码时，AMF在对ProblemDetails校验失败后是否重选AUSF以及重选后的AUSF响应消息携带ProblemDetails再次校验失败是否进入UDM Bypass状态。<br>当开关置为“ON(开启)”时表示上述场景下进行AUSF重选，重选后的AUSF响应消息携带ProblemDetails再次校验失败且AMF开启UDM全故障业务保活特性，允许用户进入UDM Bypass状态。当开关置为“OFF(关闭)”时表示上述场景下不进行AUSF重选。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（开启）”：开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPEERSELFUNC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFPEERSELFUNC]] · AMF对端选择功能控制参数（AMFPEERSELFUNC）

## 使用实例

关闭SCP/SEPP重选开关，执行如下命令：

```
SET AMFPEERSELFUNC: SCPSEPPRESEL=OFF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-AMFPEERSELFUNC.md`
