---
id: UNC@20.15.2@MMLCommand@DSP PIMRPF
type: MMLCommand
name: DSP PIMRPF（查询PIM RPF路由信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PIMRPF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- PIM的RPF路由信息
status: active
---

# DSP PIMRPF（查询PIM RPF路由信息）

## 功能

该命令用于显示PIM协议RPF路由信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| DESTADDR | 目的地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为必选参数。<br>参数含义：该参数用于表示目的地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [PIM RPF路由信息（PIMRPF）](configobject/UNC/20.15.2/PIMRPF.md)

## 使用实例

显示PIM协议RPF路由信息：

```
DSP PIMRPF:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,DESTADDR="192.168.2.1";
```

```
RETCODE = 0  操作成功

结果如下
--------
   VPN实例名称  =  _public_
        地址族  =  IPv4单播
      目的地址  =  192.168.2.1
      接口名称  =  Ethernet64/0/4
 RPF下一跳地址  =  192.168.0.1
    引用的路由  =  192.168.2.1
引用的掩码长度  =  32
引用的路由类型  =  unicast
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PIM-RPF路由信息（DSP-PIMRPF）_50280706.md`
