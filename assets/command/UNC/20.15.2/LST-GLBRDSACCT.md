---
id: UNC@20.15.2@MMLCommand@LST GLBRDSACCT
type: MMLCommand
name: LST GLBRDSACCT（查询全局RADIUS Accounting配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBRDSACCT
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
- RADIUS计费管理
- RADIUS基础参数
status: active
---

# LST GLBRDSACCT（查询全局RADIUS Accounting配置）

## 功能

**适用NF：PGW-C、SMF**

LST GLBRDSACCT命令用来显示全局Radius计费配置的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [全局RADIUS Accounting配置（GLBRDSACCT）](configobject/UNC/20.15.2/GLBRDSACCT.md)

## 使用实例

查询全局RADIUS Accounting配置：

```
LST GLBRDSACCT:;
```

```

RETCODE = 0  操作成功。

全局AAA计费配置
---------------
  发送RADIUS Accounting On/Off消息附加次数  =  1
每秒钟尝试发送Accounting Start消息的用户数  =  10
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局RADIUS-Accounting配置（LST-GLBRDSACCT）_09896777.md`
