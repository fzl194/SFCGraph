---
id: UDG@20.15.2@MMLCommand@LST BFD
type: MMLCommand
name: LST BFD（查询BFD全局配置信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: BFD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- BFD管理
- BFD全局配置
status: active
---

# LST BFD（查询BFD全局配置信息）

## 功能

该命令用于查询BFD全局配置信息。可以通过此命令来查询BFD使能情况、BFD延迟协商时长和BFD会话报文优先级配置值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/BFD]] · BFD全局配置信息（BFD）

## 使用实例

查询当前BFD全局配置：

```
LST BFD:;
```

```

RETCODE = 0  操作成功

结果如下
-------------

             BFD使能标志  =  TRUE
     会话延迟Up时间（s）  =  0
   动态BFD会话报文优先级  =  7
        使能MPLS被动会话  =  FALSE
(结果个数 = 1)
---  END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询BFD全局配置信息（LST-BFD）_00601193.md`
