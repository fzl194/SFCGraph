---
id: UNC@20.15.2@MMLCommand@LST HVNEGRCPSW
type: MMLCommand
name: LST HVNEGRCPSW（查询漫游参数协商开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HVNEGRCPSW
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- 漫游参数协商控制
status: active
---

# LST HVNEGRCPSW（查询漫游参数协商开关）

## 功能

**适用NF：SMF**

该命令用于查询V-SMF和H-SMF之间是否进行Roaming Charging Profile的协商。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HVNEGRCPSW]] · 漫游参数协商开关（HVNEGRCPSW）

## 使用实例

查询漫游参数协商开关：

```
%%LST HVNEGRCPSW:;%%
RETCODE = 0  操作成功

结果如下
------------------------
V-SMF漫游参数协商开关 =  不使能
H-SMF漫游参数协商开关 =  不使能
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HVNEGRCPSW.md`
