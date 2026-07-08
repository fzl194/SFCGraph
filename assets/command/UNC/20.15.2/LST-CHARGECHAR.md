---
id: UNC@20.15.2@MMLCommand@LST CHARGECHAR
type: MMLCommand
name: LST CHARGECHAR（查询对本地用户、漫游用户、拜访用户所采用的计费属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHARGECHAR
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
- 计费控制
- 基本计费属性
status: active
---

# LST CHARGECHAR（查询对本地用户、漫游用户、拜访用户所采用的计费属性）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

LST CHARGECHAR命令用来查询计费属性。

如果不指定可选参数，该命令将显示所有配置的计费属性名的属性信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCNAME | 计费属性名称 | 可选必选说明：可选参数<br>参数含义：计费属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHARGECHAR]] · 对本地用户、漫游用户、拜访用户所采用的计费属性（CHARGECHAR）

## 使用实例

CCName名称为“cc”的计费属性的显示配信息：

```
LST CHARGECHAR:;
```

```

RETCODE = 0  操作成功

计费属性
--------
                    计费属性名称  =  cc
                本地用户计费属性  =  0x0800
                漫游用户计费属性  =  0x0100
                拜访用户计费属性  =  0x0400
本地用户使用Serving Node计费属性  =  允许
漫游用户使用Serving Node计费属性  =  禁止
拜访用户使用Serving Node计费属性  =  禁止
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询对本地用户、漫游用户、拜访用户所采用的计费属性（LST-CHARGECHAR）_09896812.md`
