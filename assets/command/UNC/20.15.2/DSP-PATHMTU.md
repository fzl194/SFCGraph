---
id: UNC@20.15.2@MMLCommand@DSP PATHMTU
type: MMLCommand
name: DSP PATHMTU（查询路径MTU）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PATHMTU
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IP管理
- IP维护
status: active
---

# DSP PATHMTU（查询路径MTU）

## 功能

该命令用于查询路径MTU值。MTU值表示从源逻辑IP地址到目的逻辑IP地址这条链路允许通过的最大数据包大小。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCIP | 源端IP | 可选必选说明：必选参数<br>参数含义：该参数用于指定源端IP。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| DSTIP | 目的IP | 可选必选说明：必选参数<br>参数含义：该参数用于指定目的IP。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| VPNNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于描述路径VPN名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PATHMTU]] · 路径MTU（PATHMTU）

## 使用实例

查询源逻辑IP地址为fc00:fc01:0:0:0:0:0:2，目的逻辑IP地址为fc00:fc01:0:0:0:0:132:120的路径的MTU值：

```
DSP PATHMTU: SRCIP="fc00:fc01:0:0:0:0:0:2", DSTIP="fc00:fc01:0:0:0:0:132:120";
%%DSP PATHMTU: SRCIP="fc00:fc01:0:0:0:0:0:2", DSTIP="fc00:fc01:0:0:0:0:132:120";%%
RETCODE = 0  操作成功

结果如下
--------
     源端IP  =  fc00:fc01::2
     目的IP  =  fc00:fc01::132:120
    路径MTU  =  1500
VPN实例名称  =  _public_

(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PATHMTU.md`
