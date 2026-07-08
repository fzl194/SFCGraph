---
id: UNC@20.15.2@MMLCommand@LST SESSNCHRSTORECFG
type: MMLCommand
name: LST SESSNCHRSTORECFG（查询CHR存储配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SESSNCHRSTORECFG
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- CHR管理
- CHR存储配置
status: active
---

# LST SESSNCHRSTORECFG（查询CHR存储配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询CHR存储配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [CHR存储配置（SESSNCHRSTORECFG）](configobject/UNC/20.15.2/SESSNCHRSTORECFG.md)

## 使用实例

查询当前CHR存储方式设置情况：

```
LST SESSNCHRSTORECFG:;
RETCODE = 0  操作成功。

CHR存储配置
-----------
    异常CHR存盘开关  =  使能
所有CHR单据存储开关  =  不使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CHR存储配置（LST-SESSNCHRSTORECFG）_89030926.md`
