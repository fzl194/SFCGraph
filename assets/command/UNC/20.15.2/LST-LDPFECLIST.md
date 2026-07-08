---
id: UNC@20.15.2@MMLCommand@LST LDPFECLIST
type: MMLCommand
name: LST LDPFECLIST（查询FEC列表配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LDPFECLIST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP FEC列表
status: active
---

# LST LDPFECLIST（查询FEC列表配置）

## 功能

该命令用于查询FEC列表配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FECLISTNAME | FEC列表名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定FEC列表的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LDPFECLIST]] · FEC列表（LDPFECLIST）

## 使用实例

查询FEC列表配置：

```
LST LDPFECLIST:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
FEC列表名称  =  name1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询FEC列表配置（LST-LDPFECLIST）_49801438.md`
