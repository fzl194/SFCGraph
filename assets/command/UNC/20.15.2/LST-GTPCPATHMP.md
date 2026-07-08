---
id: UNC@20.15.2@MMLCommand@LST GTPCPATHMP
type: MMLCommand
name: LST GTPCPATHMP（查询GTP-C路径管理策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPCPATHMP
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C路径策略管理
status: active
---

# LST GTPCPATHMP（查询GTP-C路径管理策略）

## 功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

本命令用于查询GTP-C路径管理策略。

## 注意事项

当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 路径范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该配置影响的GTP-C路径范围。<br>数据来源：全网规划<br>取值范围：<br>- E_HOME（本网）<br>- E_FOREIGN（外网）<br>- E_SPECI_INTF（指定接口）<br>- E_SPECI_IP（指定IP）<br>默认值：无<br>配置原则：无 |
| INTFTYPE | 接口类型 | 可选必选说明：该参数在"RANGE"配置为"E_SPECI_INTF"时为条件可选参数。<br>参数含义：该参数用于指定GTP-C路径的接口类型。<br>数据来源：全网规划<br>取值范围：<br>- S11（S11接口）<br>- N26（N26接口）<br>- S5（S5接口）<br>- S8（S8接口）<br>- GN（Gn接口）<br>- GP（Gp接口）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [GTP-C路径管理策略（GTPCPATHMP）](configobject/UNC/20.15.2/GTPCPATHMP.md)

## 使用实例

查询所有GTP-C路径的管理策略配置：LST GTPCPATHMP:;

```
+++    UNC/*MEID:0 MENAME:unc*/        2019-12-09 16:39:05+8:00
O&M    #7033
%%LST GTPCPATHMP:;%%
RETCODE = 0  操作成功

结果如下
--------
路径范围  接口类型  IP地址类型  IPv4地址  IPv4地址掩码     IPv6地址   IPv6地址前缀长度  Echo请求发送开关  Echo请求发送间隔  Echo请求重发时间间隔  Echo请求最大发送次数  告警门限  描述信息  

指定IP    NULL      IPv4        10.1.1.1   255.255.255.255    ::         128               ON                60                3                     5                     1         NULL      
指定IP    NULL      IPv4        10.1.1.2   255.255.255.255    ::         128               ON                60                3                     5                     1         NULL      
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GTP-C路径管理策略（LST-GTPCPATHMP）_09653264.md`
