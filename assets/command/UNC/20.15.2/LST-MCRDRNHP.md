---
id: UNC@20.15.2@MMLCommand@LST MCRDRNHP
type: MMLCommand
name: LST MCRDRNHP（查询组播报文重定向策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MCRDRNHP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MRM
- 组播报文重定向策略配置
status: active
---

# LST MCRDRNHP（查询组播报文重定向策略）

## 功能

该命令用来查询组播报文重定向策略配置。

## 注意事项

NA

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。默认值：无。<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例信息。 |
| IPVERSION | 地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定下一跳地址为IPv4类型或IPv6类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4类型。<br>- IPv6：IPv6类型。<br>默认值：IPv4<br>配置原则：无 |
| NEXTHOPADDRV4 | IPv4下一跳地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定下一跳IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| NEXTHOPADDRV6 | IPv6下一跳地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定下一跳IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MCRDRNHP]] · 组播报文重定向策略（MCRDRNHP）

## 使用实例

查询组播报文重定向策略配置：

```
%%LST MCRDRNHP: IPVERSION=IPv4;%%
RETCODE = 0  操作成功  
结果如下: 
---------
        VPN名称  =  vrf1
       地址类型  =  IPv4
 IPv4下一跳地址  =  192.168.0.1
 IPv6下一跳地址  =  :: 
(结果个数 = 1)
 ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MCRDRNHP.md`
