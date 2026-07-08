---
id: UNC@20.15.2@MMLCommand@LST IPALLOCBYLOCSW
type: MMLCommand
name: LST IPALLOCBYLOCSW（查询基于位置区地址分配的开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPALLOCBYLOCSW
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 基于位置区地址分配开关配置
status: active
---

# LST IPALLOCBYLOCSW（查询基于位置区地址分配的开关）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令查询指定位置区组或所有的基于位置区地址分配的开关信息。

## 注意事项

- 该命令指定位置区组类型和名称时，表示查询指定位置区组基于位置区地址分配的开关信息。
- 指定位置区组的类型而不指定名称时，表示查询指定类型位置区组基于位置区地址分配的开关信息。
- 不指定位置区组的类型和名称时，表示查询所有基于位置区组地址分配的开关信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCATIONGRPNAME | 位置区组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于标识位置区组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRTACGROUP或ADD ADDRLACGROUP命令配置生成。 |
| LOCATIONGRPTYPE | 位置区组类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区组类型。<br>数据来源：本端规划<br>取值范围：<br>- LAC（LAC）<br>- TAC（TAC）<br>默认值：无<br>配置原则：<br>- 配置类型为TAC，LOCATIONGRPNAME必须由ADD ADDRTACGROUP新增。<br>- 配置类型为LAC，LOCATIONGRPNAME必须由ADD ADDRLACGROUP新增。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPALLOCBYLOCSW]] · 基于位置区地址分配的开关（IPALLOCBYLOCSW）

## 使用实例

查询名为tac1的TAC-GROUP基于位置区地址分配的开关信息：

```
%%LST IPALLOCBYLOCSW: LOCATIONGRPTYPE=TAC;%%
RETCODE = 0 操作成功

结果如下
-------
位置区组类型  =  TAC
位置区组名称  =  1
    IPv4开关  =  去使能
    IPV6开关  =  去使能
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询基于位置区地址分配的开关（LST-IPALLOCBYLOCSW）_49644920.md`
