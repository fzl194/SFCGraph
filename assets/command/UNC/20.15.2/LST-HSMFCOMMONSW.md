---
id: UNC@20.15.2@MMLCommand@LST HSMFCOMMONSW
type: MMLCommand
name: LST HSMFCOMMONSW（查询H-SMF通用控制开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HSMFCOMMONSW
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话管理拓展功能
- H-SMF会话管理拓展功能
status: active
---

# LST HSMFCOMMONSW（查询H-SMF通用控制开关）

## 功能

**适用NF：SMF**

该命令用于查询H-SMF通用控制开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/HSMFCOMMONSW]] · H-SMF通用控制开关（HSMFCOMMONSW）

## 使用实例

查询H-SMF通用控制开关：

```
%%LST HSMFCOMMONSW:;%%
RETCODE = 0  操作成功

结果如下
------------------------
服务节点IP地址开关 =  不使能
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询H-SMF通用控制开关（LST-HSMFCOMMONSW）_15082974.md`
