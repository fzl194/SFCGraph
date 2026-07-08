---
id: UDG@20.15.2@MMLCommand@LST FABRICTRUNKMEMBER
type: MMLCommand
name: LST FABRICTRUNKMEMBER（查询Fabric-Trunk成员接口）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FABRICTRUNKMEMBER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP Fabric链路管理
- Fabric-Trunk成员接口管理
status: active
---

# LST FABRICTRUNKMEMBER（查询Fabric-Trunk成员接口）

## 功能

该命令用于查询NP卡Fabric-Trunk成员接口的基本信息。

## 注意事项

该命令仅适用于非NP卡基础上扩容NP卡的异构场景，在纯NP场景该命令不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRUNKNAME | Fabric-Trunk接口名称 | 可选必选说明：可选参数。<br>参数含义：该参数是Fabric-Trunk接口的名称。<br>数据来源：本端规划。<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>配置原则：无。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FABRICTRUNKMEMBER]] · Fabric-Trunk成员接口（FABRICTRUNKMEMBER）

## 使用实例

查询所有的Fabric-Trunk成员接口：

```
%%LST FABRICTRUNKMEMBER:;%%
RETCODE = 0  操作成功

结果如下
--------
Fabric-Trunk接口名称  Fabric-Trunk标识  框号  槽位号  端口号

Fabric-Trunk13         10                 0     5       3     
Fabric-Trunk14         11                 0     6       3     
Fabric-Trunk15         12                 0     7       3     
Fabric-Trunk19         8                  1     3       3     
Fabric-Trunk20         9                  1     4       3     
(结果数量 = 5)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FABRICTRUNKMEMBER.md`
