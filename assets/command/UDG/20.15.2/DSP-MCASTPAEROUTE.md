---
id: UDG@20.15.2@MMLCommand@DSP MCASTPAEROUTE
type: MMLCommand
name: DSP MCASTPAEROUTE（查询组播引流表项信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MCASTPAEROUTE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MRM
- 组播引流表项信息
status: active
---

# DSP MCASTPAEROUTE（查询组播引流表项信息）

## 功能

该命令用于显示组播引流表项信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MCASTPAEROUTE]] · 组播引流表项信息（MCASTPAEROUTE）

## 使用实例

显示组播引流表项信息：

```
DSP MCASTPAEROUTE:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast;
```

```
RETCODE = 0 操作成功。

结果如下
------------------------
VPN实例名称    地址族      源地址         组地址       叶子个数    Include叶子个数    表项建立时间      表项标记

_public_       IPv4单播    192.168.0.1    239.0.0.1    1           1                  00:00:23          PAE
_public_       IPv4单播    192.168.0.2    239.0.0.2    2           1                  00:00:52          PAE
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MCASTPAEROUTE.md`
