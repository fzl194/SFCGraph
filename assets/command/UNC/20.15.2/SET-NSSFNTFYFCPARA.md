---
id: UNC@20.15.2@MMLCommand@SET NSSFNTFYFCPARA
type: MMLCommand
name: SET NSSFNTFYFCPARA（设置通知流控参数配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NSSFNTFYFCPARA
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF流控管理
status: active
---

# SET NSSFNTFYFCPARA（设置通知流控参数配置）

## 功能

**适用NF：NSSF**

该命令用于配置NSSF订阅通知流程流控参数信息。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| FCSWITCH | NOTIFYBW |
| --- | --- |
| FUNC_ON | 6 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCSWITCH | 通知流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否开启NSSF的订阅通知流控功能。若开关设置为“FUNC_ON”，NSSF单个POD发送的订阅通知所占带宽会被限制在配置值范围内，超出限制的订阅通知延迟到下一秒发送。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSSFNTFYFCPARA查询当前参数配置值。<br>配置原则：无 |
| NOTIFYBW | 单个VM发送订阅通知带宽(MB/s) | 可选必选说明：可选参数<br>参数含义：该参数用于表示NSSF所在的POD每秒发送订阅通知的带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~100。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSSFNTFYFCPARA查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [通知流控参数配置（NSSFNTFYFCPARA）](configobject/UNC/20.15.2/NSSFNTFYFCPARA.md)

## 使用实例

设置通知流控参数配置，通知流控开关为开，单个VM发送订阅通知带宽为6MB/s。

```
SET NSSFNTFYFCPARA: FCSWITCH=FUNC_ON, NOTIFYBW=6;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置通知流控参数配置（SET-NSSFNTFYFCPARA）_97258366.md`
