---
id: UNC@20.15.2@MMLCommand@LST CGGROUP
type: MMLCommand
name: LST CGGROUP（查询CG组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CGGROUP
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- CG组管理
- CG组
status: active
---

# LST CGGROUP（查询CG组）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用来查询指定的CG组。

## 注意事项

- 如果查询一个CG组，需要输入CG组的ID。
- 如果查询所有的CG组，则不需要输入参数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CGGRPID | CG组ID | 可选必选说明：可选参数<br>参数含义：CG组的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32。<br>默认值：无<br>配置原则：如果不输入该参数则是要查询所有的CG组。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CGGROUP]] · CG组（CGGROUP）

## 使用实例

查询所有的CG组：

```
LST CGGROUP:;
```

```

RETCODE = 0  操作成功。

CG组信息
--------------------
CG组ID  =  1
CG组描述  =  CGGroup1
(结果个数 = 1)
---END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CGGROUP.md`
