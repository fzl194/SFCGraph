---
id: UNC@20.15.2@MMLCommand@LST RGRESCTRL
type: MMLCommand
name: LST RGRESCTRL（查询RG资源控制配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RGRESCTRL
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
- RG资源控制
status: active
---

# LST RGRESCTRL（查询RG资源控制配置）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询RG老化功能以及RG超出规格后的处理动作。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [RG资源控制配置（RGRESCTRL）](configobject/UNC/20.15.2/RGRESCTRL.md)

## 使用实例

查询RG资源控制配置。

```
LST RGRESCTRL:;
RETCODE = 0  操作成功

结果如下
------------------------
                   在线计费RG老化控制  =  使能
              在线计费RG老化时长 (分)  =  20
在线计费全局业务阻塞处理时间间隔 (分)  =  0
                   离线计费RG老化控制  =  使能
              离线计费RG老化时长 (分)  =  20
             超出业务最大规格处理动作  =  阻塞对应业务
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RG资源控制配置（LST-RGRESCTRL）_96242438.md`
