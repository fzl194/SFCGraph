---
id: UNC@20.15.2@MMLCommand@LST OCSGROUP
type: MMLCommand
name: LST OCSGROUP（查询Ocs组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OCSGROUP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- OCS Diameter连接
- OCS Group
status: active
---

# LST OCSGROUP（查询Ocs组）

## 功能

**适用NF：PGW-C、SMF**

此命令用来查询指定的OCS组。

## 注意事项

- 如果查询一个OCS组，需要输入OCS组的名称。
- 如果查询所有的OCS组，则不需要输入参数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSGRPNAME | Ocs组名称 | 可选必选说明：可选参数<br>参数含义：ocs组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：如果不配置则是要查询所有的OCS组。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OCSGROUP]] · Ocs组（OCSGROUP）

## 使用实例

查询名称为“ocsgroup1”的OCS组：

```
LST OCSGROUP:;
```

```

RETCODE = 0  操作成功。

Ocs组信息
---------
Ocs组名称  =  ocsgroup1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-OCSGROUP.md`
