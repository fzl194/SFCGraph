---
id: UNC@20.15.2@MMLCommand@EST M3LNK
type: MMLCommand
name: EST M3LNK（建立M3UA信令链路）
nf: UNC
version: 20.15.2
verb: EST
object_keyword: M3LNK
command_category: 调测类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- M3UA管理
- M3UA链路
status: active
---

# EST M3LNK（建立M3UA信令链路）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于建立M3UA信令链路。链路处于“SCTP偶联未建立”状态，执行该命令，建立链路。

## 注意事项

- 该命令执行后立即生效。
- 如果该链路之前以优雅方式释放，则链路建立后状态为“非激活”。
- 如果该链路之前以非优雅方式释放，则链路建立后状态为“激活”。
- 该命令只有在执行[**ADD M3LNK**](增加M3UA信令链路(ADD M3LNK)_72225983.md)命令时配置的参数“C/S模式”为“C(客户端模式)”的情形下才能执行。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNK | 链路号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示M3UA链路号。<br>取值范围：0~1279<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M3LNK]] · M3UA信令链路（M3LNK）

## 使用实例

建立链路号为1的M3UA链路：

EST M3LNK: LNK=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/建立M3UA信令链路（EST-M3LNK）_26146308.md`
