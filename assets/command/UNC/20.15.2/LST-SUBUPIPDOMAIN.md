---
id: UNC@20.15.2@MMLCommand@LST SUBUPIPDOMAIN
type: MMLCommand
name: LST SUBUPIPDOMAIN（查询当前UPF扩展类型绑定的IP域）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SUBUPIPDOMAIN
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UPF IP Domain管理
status: active
---

# LST SUBUPIPDOMAIN（查询当前UPF扩展类型绑定的IP域）

## 功能

**适用NF：SMF、PGW-C**

该命令用于查看当前UPF扩展类型绑定的IPDOMAIN。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPNODE | UPF节点标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示UPF节点标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| BINDINGTYPE | Ip域所绑定的信元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示与Ip域所绑定的信元类型。<br>数据来源：全网规划<br>取值范围：<br>- “VpnInstance（使用Vpn实例进行绑定）”：使用Vpn实例进行IpDomain的绑定<br>- “AddrPoolGrpName（使用地址池组名称进行绑定）”：使用地址池组名称进行IpDomain的绑定<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例名 | 可选必选说明：该参数在"BINDINGTYPE"配置为"VpnInstance"时为条件必选参数。<br>参数含义：该参数用于指定VPN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：<br>本参数取值与ADD APN命令中的“VPN实例名”参数取值保持一致时，关联关系生效。 |
| POOLGRPNAME | 地址池组名称 | 可选必选说明：该参数在"BINDINGTYPE"配置为"AddrPoolGrpName"时为条件必选参数。<br>参数含义：该参数用于指定地址池组的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~79。<br>默认值：无<br>配置原则：<br>本参数取值与ADD ADDRPOOLGRP命令中的“地址池组名称”参数取值保持一致时，关联关系生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SUBUPIPDOMAIN]] · 当前UPF扩展类型绑定的IP域（SUBUPIPDOMAIN）

## 使用实例

查询所有UPF扩展类型绑定的IPDOMAIN:

```
%%LST SUBUPIPDOMAIN:;%%
RETCODE = 0  操作成功

结果如下
------------------------
UPF节点标识     IP地址段归属的域   Ip域所绑定的信元类型     VPN实例名    地址池组名称

upf_instance_1    Domain_0          使用Vpn实例进行绑定        vpn1           NULL
(结果个数 = 1)

 -----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SUBUPIPDOMAIN.md`
