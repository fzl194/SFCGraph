---
id: UDG@20.15.2@MMLCommand@LST QOSSHAPE
type: MMLCommand
name: LST QOSSHAPE（查询QosShape配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: QOSSHAPE
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 流量管理
- QoS shaping配置
status: active
---

# LST QOSSHAPE（查询QosShape配置）

## 功能

**适用NF：UPF**

该命令用于查询用户上下行shaping功能的全局开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/QOSSHAPE]] · QosShape配置（QOSSHAPE）

## 使用实例

查询全局的QosShape功能开关：

```
LST QOSSHAPE:;
```

```

RETCODE = 0  操作成功。

QosShape配置信息
----------------
用户漫游类型    上行RAT类型    下行RAT类型

本地            NULL           NULL       
漫游            NULL           NULL       
拜访            NULL           NULL       
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询QosShape配置（LST-QOSSHAPE）_82837672.md`
