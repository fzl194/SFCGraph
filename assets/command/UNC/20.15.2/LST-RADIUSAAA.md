---
id: UNC@20.15.2@MMLCommand@LST RADIUSAAA
type: MMLCommand
name: LST RADIUSAAA（查询RADIUS AAA测量对象）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RADIUSAAA
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- RADIUS维护
- AAA统计对象
status: active
---

# LST RADIUSAAA（查询RADIUS AAA测量对象）

## 功能

**适用NF：PGW-C、SMF**

此命令用于查询RADIUS AAA测量对象。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RADIUSAAA]] · RADIUS AAA测量对象（RADIUSAAA）

## 使用实例

查询RADIUS AAA测量对象：

```
LST RADIUSAAA:;
```

```

RETCODE = 0  操作成功。

RADIUS Server IP地址
--------------------
IP地址  =  192.168.1.12
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RADIUSAAA.md`
