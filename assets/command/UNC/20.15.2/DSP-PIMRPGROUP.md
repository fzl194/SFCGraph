---
id: UNC@20.15.2@MMLCommand@DSP PIMRPGROUP
type: MMLCommand
name: DSP PIMRPGROUP（查询组播组对应的RP信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PIMRPGROUP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- 组播组对应的RP信息
status: active
---

# DSP PIMRPGROUP（查询组播组对应的RP信息）

## 功能

该命令用于显示组播组对应的RP信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| GRPADDR | 组地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为必选参数。<br>参数含义：该参数用于表示组地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PIMRPGROUP]] · 组播组对应的RP信息（PIMRPGROUP）

## 使用实例

显示组播组对应的RP信息：

```
DSP PIMRPGROUP:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,GRPADDR="239.5.5.5";
```

```
RETCODE = 0  操作成功

结果如下
--------
  VPN实例名称  =  _public_
       地址族  =  IPv4单播
       组地址  =  239.5.5.5
   BSR RP地址  =  192.168.2.1
   静态RP地址  =  10.8.8.8
       RP地址  =  192.168.2.1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PIMRPGROUP.md`
