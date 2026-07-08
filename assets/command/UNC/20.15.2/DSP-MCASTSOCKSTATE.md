---
id: UNC@20.15.2@MMLCommand@DSP MCASTSOCKSTATE
type: MMLCommand
name: DSP MCASTSOCKSTATE（查询组播Socket信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MCASTSOCKSTATE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MRM
- 组播Socket信息
status: active
---

# DSP MCASTSOCKSTATE（查询组播Socket信息）

## 功能

该命令用于显示组播Socket信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| COMPONENTNAME | 组件名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组件名称。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PIMCORE：PIMCORE组件。<br>- DGMP：DGMP组件。<br>- PIMBSR：PIMBSR组件。<br>- PIMAGENT：PIMAGENT组件。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| IFNAME | 接口名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“COMPONENTNAME”配置为“DGMP”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“COMPONENTNAME”配置为“PIMAGENT”时为可选参数。<br>参数含义：该参数用于表示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MCASTSOCKSTATE]] · 组播Socket信息（MCASTSOCKSTATE）

## 使用实例

查询组播Socket信息：

```
DSP MCASTSOCKSTATE:VRFNAME= "_public_",ADDRESSFAMILY=ipv4unicast,COMPONENTNAME=PIMCORE;
```

```
RETCODE = 0  操作成功。

结果如下
--------
  VPN实例名称  =  _public_
       地址族  =  IPv4单播
     组件名称  =  Pimcore组件
      组件PID  =  14549016
      组件CID  =  2162032664
   Socket状态  =  Established
Socket组件CID  =  0x80650080
   Socket索引  =  1
       管道ID  =  524314
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询组播Socket信息（DSP-MCASTSOCKSTATE）_00840577.md`
