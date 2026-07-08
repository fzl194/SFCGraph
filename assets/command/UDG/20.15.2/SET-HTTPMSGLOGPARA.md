---
id: UDG@20.15.2@MMLCommand@SET HTTPMSGLOGPARA
type: MMLCommand
name: SET HTTPMSGLOGPARA（设置HTTP消息日志参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: HTTPMSGLOGPARA
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP消息日志管理
status: active
---

# SET HTTPMSGLOGPARA（设置HTTP消息日志参数）

## 功能

该命令用于设置HTTP消息日志的参数，该参数设置后整系统生效。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | TCPMSGSW | STOPCPUTHOLD | RESCPUTHOLD |
> | --- | --- | --- |
> | ON | 75 | 65 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TCPMSGSW | TCP消息日志开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置是否开启TCP消息日志功能。开启该功能后，会记录TCP的SYN、FIN、RST消息及其后续部分消息的报文头内容。<br>数据来源：本端规划<br>取值范围：<br>- “ON（打开）”：打开<br>- “OFF（关闭）”：关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPMSGLOGPARA查询当前参数配置值。<br>配置原则：无 |
| STOPCPUTHOLD | 停止记录的CPU阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于配置停止记录消息日志的CPU占用率阈值。当CPU占用率大于或等于该阈值时停止记录消息日志。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~100，单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPMSGLOGPARA查询当前参数配置值。<br>配置原则：<br>该参数的配置值必须大于参数“恢复记录的CPU阈值”的配置值。 |
| RESCPUTHOLD | 恢复记录的CPU阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于配置恢复记录消息日志的CPU占用率阈值。当CPU占用率小于或等于该阈值时恢复记录消息日志。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~100，单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPMSGLOGPARA查询当前参数配置值。<br>配置原则：<br>该参数的配置值必须小于参数“停止记录的CPU阈值”的配置值。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HTTPMSGLOGPARA]] · HTTP消息日志参数（HTTPMSGLOGPARA）

## 使用实例

如果需要打开HTTP消息日志开关，可以执行如下命令：

```
SET HTTPMSGLOGPARA: TCPMSGSW=ON;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置HTTP消息日志参数（SET-HTTPMSGLOGPARA）_59288797.md`
