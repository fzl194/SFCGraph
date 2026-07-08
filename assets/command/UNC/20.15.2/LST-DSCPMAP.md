---
id: UNC@20.15.2@MMLCommand@LST DSCPMAP
type: MMLCommand
name: LST DSCPMAP（查询DSCP值到VLAN优先级的映射）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DSCPMAP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- DSCP映射VLAN优先级
status: active
---

# LST DSCPMAP（查询DSCP值到VLAN优先级的映射）

## 功能

该命令用于查询DSCP值到VLAN优先级的映射。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DSCP | DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用来表示DSCP值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无 |
| TYPE | 优先级类型 | 可选必选说明：可选参数<br>参数含义：该参数用来表示优先级类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- 8021p：8021p优先级。<br>- exp：EXP优先级。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DSCPMAP]] · DSCP值到VLAN优先级的映射（DSCPMAP）

## 使用实例

查询DSCP值到VLAN优先级的映射：

```
LST DSCPMAP:;
```

```

RETCODE = 0  操作成功
结果如下
-------------------------
DSCP值     优先级类型   优先级数值 
62         exp          5 
63         8021p        7 
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DSCPMAP.md`
