---
id: UNC@20.15.2@MMLCommand@RMV SUBUPIPDOMAIN
type: MMLCommand
name: RMV SUBUPIPDOMAIN（删除当前UPF扩展类型绑定的IP域）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SUBUPIPDOMAIN
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UPF IP Domain管理
status: active
---

# RMV SUBUPIPDOMAIN（删除当前UPF扩展类型绑定的IP域）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除当前UPF扩展类型绑定的IPDomain。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPNODE | UPF节点标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示UPF节点标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| IPDOMAIN | IP地址段归属的域 | 可选必选说明：可选参数<br>参数含义：该参数用于表示IP地址段归属的域。例如当两个UPF上的IP地址段中存在重叠的地址时，可以配置地址段1归属IPDOAMAIN1，地址段2归属IPDOMAIN2，随UE IP将IPDOMAIN携带给PCF，PCF检测到IP地址冲突，不影响用户正常使用业务。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>SMF为每个IP地址段归属的域提供不同的标识符（如SMF NF实例标识符）。 |
| BINDINGTYPE | Ip域所绑定的信元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示与Ip域所绑定的信元类型。<br>数据来源：全网规划<br>取值范围：<br>- “VpnInstance（使用Vpn实例进行绑定）”：使用Vpn实例进行IpDomain的绑定<br>- “AddrPoolGrpName（使用地址池组名称进行绑定）”：使用地址池组名称进行IpDomain的绑定<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例名 | 可选必选说明：该参数在"BINDINGTYPE"配置为"VpnInstance"时为条件必选参数。<br>参数含义：该参数用于指定VPN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：<br>本参数取值与ADD APN命令中的“VPN实例名”参数取值保持一致时，关联关系生效。 |
| POOLGRPNAME | 地址池组名称 | 可选必选说明：该参数在"BINDINGTYPE"配置为"AddrPoolGrpName"时为条件必选参数。<br>参数含义：该参数用于指定地址池的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~79。<br>默认值：无<br>配置原则：<br>本参数取值与ADD ADDRPOOLGRP命令中的“地址池组名称”参数取值保持一致时，关联关系生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SUBUPIPDOMAIN]] · 当前UPF扩展类型绑定的IP域（SUBUPIPDOMAIN）

## 使用实例

删除UPNODE为"upf_instance_1"的UPF与IPDomain的绑定关系:

```
RMV SUBUPIPDOMAIN: UPNODE="upf_instance_1", BINDINGTYPE=VpnInstance, VPNINSTANCE="vpn1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SUBUPIPDOMAIN.md`
