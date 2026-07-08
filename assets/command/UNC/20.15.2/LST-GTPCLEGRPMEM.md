---
id: UNC@20.15.2@MMLCommand@LST GTPCLEGRPMEM
type: MMLCommand
name: LST GTPCLEGRPMEM（查询GTP-C本地实体组成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPCLEGRPMEM
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
- GTP-C本地实体组成员
status: active
---

# LST GTPCLEGRPMEM（查询GTP-C本地实体组成员）

## 功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于查询GTP-C本地实体组成员的信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | 组号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GTP-C本地实体的组号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~31。该参数需要从ADD GTPCLEGRP命令中已配置的GRPID参数中取值。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [GTP-C本地实体组成员（GTPCLEGRPMEM）](configobject/UNC/20.15.2/GTPCLEGRPMEM.md)

## 使用实例

查询0号GTP-C本地实体组的信息。

```
%%LST GTPCLEGRPMEM: GROUPID=0;%%
RETCODE = 0  操作成功

结果如下
--------
组号  IP地址类型  IPv4地址  IPv6地址  VPN名称   描述信息  
    
0     IPv4        10.2.125.26     ::   _public_  s11          
0     IPv4        10.2.125.27     ::   _public_  s11   
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GTP-C本地实体组成员（LST-GTPCLEGRPMEM）_09654349.md`
