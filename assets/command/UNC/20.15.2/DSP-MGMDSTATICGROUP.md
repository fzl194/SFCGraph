---
id: UNC@20.15.2@MMLCommand@DSP MGMDSTATICGROUP
type: MMLCommand
name: DSP MGMDSTATICGROUP（显示IGMP静态加入信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MGMDSTATICGROUP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MGMD
- IGMP静态组播组配置
status: active
---

# DSP MGMDSTATICGROUP（显示IGMP静态加入信息）

## 功能

该命令用于显示IGMP静态加入信息。

## 注意事项

- 大量数据时命令会限制输出条数固定1000条，防止网管回显超时。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| MASTERSLAVETYPE | OMU类型 | 可选必选说明：可选参数<br>参数含义：该参数表示OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER：主。<br>- SLAVE：备。<br>默认值：MASTER |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MGMDSTATICGROUP]] · IGMP静态组配置（MGMDSTATICGROUP）

## 使用实例

显示IGMP静态加入信息：

```
DSP MGMDSTATICGROUP:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast;
```

```
RETCODE = 0  操作成功。

结果如下
--------
   VPN实例名称  =  _public_
      接口名称  =  Ethernet64/0/5
    静态组地址  =  239.0.0.1
静态组的源地址  =  10.0.0.1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MGMDSTATICGROUP.md`
