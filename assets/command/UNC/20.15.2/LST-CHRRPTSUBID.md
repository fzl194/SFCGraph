---
id: UNC@20.15.2@MMLCommand@LST CHRRPTSUBID
type: MMLCommand
name: LST CHRRPTSUBID（查询CHR本地存盘用户）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHRRPTSUBID
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- CHR管理
- CHR本地存盘用户
status: active
---

# LST CHRRPTSUBID（查询CHR本地存盘用户）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于显示所有指定的本地存储CHR表单的用户。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHRRPTSUBID]] · CHR本地存盘用户（CHRRPTSUBID）

## 使用实例

显示IMSI指定用户本地存储CHR表单的信息：

```
LST CHRRPTSUBID:;

RETCODE = 0  操作成功。

CHR本地存盘用户信息
-------------------
                               IMSI  =  122222222222222
                 流程模板索引  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CHRRPTSUBID.md`
