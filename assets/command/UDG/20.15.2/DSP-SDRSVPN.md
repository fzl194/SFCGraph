---
id: UDG@20.15.2@MMLCommand@DSP SDRSVPN
type: MMLCommand
name: DSP SDRSVPN（显示SDRS中的VPN信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SDRSVPN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRSVPN（显示SDRS中的VPN信息）

## 功能

该命令用于查询SDRS中的VPN信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLID | Cell ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定SDR调试消息发送的CELLID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SDRSVPN]] · SDRS中的VPN信息（SDRSVPN）

## 使用实例

显示SDRS中的VPN信息

```
%%DSP SDRSVPN: CELLID="vup-pod-010-104-1-24__103__0";%%
RETCODE = 0  操作成功

结果如下
--------
Cell ID                 = vup-pod-010-104-1-24__103__0
VPN名称                 = _public_
SDRC分配VPN ID          = 1
下行是否经过LB          = 1
VPN地址信息总个数       = 1
VPN有效地址信息个数     = 1
实例ID                  = 281492156580946 0x1000400000452
VPN ID                  = 0
通信地址信息LOW TB      = 1106
通信地址信息TP          = 2416123937
有效通信地址            = TRUE
VPN版本信息             = 6728054339338254048
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SDRSVPN.md`
