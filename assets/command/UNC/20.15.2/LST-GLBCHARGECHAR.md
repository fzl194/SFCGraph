---
id: UNC@20.15.2@MMLCommand@LST GLBCHARGECHAR
type: MMLCommand
name: LST GLBCHARGECHAR（查询对本地用户、漫游用户、拜访用户所采用的计费属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBCHARGECHAR
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
- 计费控制
- 计费参数
status: active
---

# LST GLBCHARGECHAR（查询对本地用户、漫游用户、拜访用户所采用的计费属性）

## 功能

**适用NF：PGW-C、SMF**

该命令用来查询配置对本地用户、漫游用户、拜访用户所采用的计费属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBCHARGECHAR]] · 对本地用户、漫游用户、拜访用户所采用的计费属性（GLBCHARGECHAR）

## 使用实例

查询配置对本地用户、漫游用户、拜访用户所采用的计费属性：

```
LST GLBCHARGECHAR:;
```

```

RETCODE = 0  操作成功。

全局计费属性
------------
            本地用户计费类型  =  0x0001
            漫游用户计费类型  =  0x0001
            拜访用户计费类型  =  0x0001
本地用户使用SGSN计费属性标志  =  允许
漫游用户使用SGSN计费属性标志  =  允许
拜访用户使用SGSN计费属性标志  =  允许
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询对本地用户、漫游用户、拜访用户所采用的计费属性（LST-GLBCHARGECHAR）_09896801.md`
