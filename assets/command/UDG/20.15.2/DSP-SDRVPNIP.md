---
id: UDG@20.15.2@MMLCommand@DSP SDRVPNIP
type: MMLCommand
name: DSP SDRVPNIP（查询SDRC中的VPNIP信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SDRVPNIP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRVPNIP（查询SDRC中的VPNIP信息）

## 功能

该命令用于查询SDRC中的VPNIP信息，若命令不接任何参数，则该命令列出SDRC中所有VPNIP的信息，否则显示特定的VPNIP信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPNIP策略的vpn名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SDRVPNIP]] · SDRC中的VPNIP信息（SDRVPNIP）

## 使用实例

显示SDRC中VPNNAME等于_public_的VPNIP信息

```
%%DSP SDRVPNIP:;%%
RETCODE = 0  操作成功

结果如下
--------
vpn名称  =  _public_
Address Family  =  0
源地址  =  "10.11.2.11"

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SDRVPNIP.md`
