---
id: UNC@20.15.2@MMLCommand@DSP MCASTPAEELB
type: MMLCommand
name: DSP MCASTPAEELB（查询组播引流表项叶子信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MCASTPAEELB
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MRM
- 组播引流表项叶子表信息
status: active
---

# DSP MCASTPAEELB（查询组播引流表项叶子信息）

## 功能

该命令用于显示组播引流表项叶子信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| SRCADDR | 源地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为必选参数。<br>参数含义：该参数用于表示组播源地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| GRPADDR | 组地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为必选参数。<br>参数含义：该参数用于表示组播组地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MCASTPAEELB]] · 组播引流表项叶子信息（MCASTPAEELB）

## 使用实例

显示组播引流表项叶子信息：

```
DSP MCASTPAEELB:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,SRCADDR="0.0.0.0",GRPADDR="239.2.2.2";
```

```
RETCODE = 0 操作成功。

结果如下
------------------------
  VPN实例名称  =  _public_
       地址族  =  IPv4单播
       源地址  =  0.0.0.0
       组地址  =  239.2.2.2
PAE Group索引  =  2
     过滤模式  =  Include模式
 表项建立时间  =  00:00:01
     表项标记  =  PAE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询组播引流表项叶子信息（DSP-MCASTPAEELB）_00866289.md`
