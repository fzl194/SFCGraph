---
id: UNC@20.15.2@MMLCommand@LST DFTSRVNODEPLMN
type: MMLCommand
name: LST DFTSRVNODEPLMN（查询默认PLMN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DFTSRVNODEPLMN
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 缺省服务节点PLMN
status: active
---

# LST DFTSRVNODEPLMN（查询默认PLMN）

## 功能

**适用NF：SGW-C、PGW-C、GGSN**

该命令用于查看UNC设备默认的PLMN。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODETYPE | 结点类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元类型。<br>数据来源：本端规划<br>取值范围：<br>- SGSN（SGSN）<br>- SGW（SGW）<br>- PGW（PGW）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [默认PLMN（DFTSRVNODEPLMN）](configobject/UNC/20.15.2/DFTSRVNODEPLMN.md)

## 使用实例

查看PGW默认所属的PLMN：

```
%%LST DFTSRVNODEPLMN:;%%
RETCODE = 0  操作成功

结果如下
--------
结点类型  =  SGSN
PLMN标识  =  12345
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询默认PLMN（LST-DFTSRVNODEPLMN）_09652630.md`
