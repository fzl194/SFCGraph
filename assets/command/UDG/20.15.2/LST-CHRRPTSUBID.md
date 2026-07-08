---
id: UDG@20.15.2@MMLCommand@LST CHRRPTSUBID
type: MMLCommand
name: LST CHRRPTSUBID（查询CHR上报用户）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CHRRPTSUBID
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 呼叫日志管理
- CHR本地存盘用户配置
status: active
---

# LST CHRRPTSUBID（查询CHR上报用户）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于显示所有指定的本地存储CHR表单的用户。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/CHRRPTSUBID]] · CHR上报用户（CHRRPTSUBID）

## 使用实例

显示所有指定用户本地存储CHR表单的信息：

```
LST CHRRPTSUBID:;
```

```
%%
RETCODE = 0 操作成功。

CHR本地存盘用户信息
-------------------
    IMSI = 122222222222222
CHR 类型 = 信令CHR
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CHR上报用户（LST-CHRRPTSUBID）_64015294.md`
