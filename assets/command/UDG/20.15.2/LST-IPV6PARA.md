---
id: UDG@20.15.2@MMLCommand@LST IPV6PARA
type: MMLCommand
name: LST IPV6PARA（查询IPv6参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPV6PARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务编排功能管理
- 系统管理
- 资源管理
- IPv6Pmtu管理
status: active
---

# LST IPV6PARA（查询IPv6参数）

## 功能

该命令用于查询IPv6功能参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。数据来源：本端规划<br>取值范围：字符串类型，通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令获取。不支持对"VNFC类型名称"为VNFP、VNRS_VNFC、ACS、IPSEC_VNFC的VNFC进行查询。<br>默认值：无<br>配置原则：只能填写通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [IPv6参数（IPV6PARA）](configobject/UDG/20.15.2/IPV6PARA.md)

## 使用实例

查询IPv6功能参数。

LST IPV6PARA: SERVICEINSTANCE="CSLB_VNFC_999" ;

```
RETCODE = 0  操作成功。

结果如下
-------------------------
PMTU老化时长  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IPv6参数(LST-IPV6PARA)_29626975.md`
