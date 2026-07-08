---
id: UNC@20.15.2@MMLCommand@LST SMSBACKUPSW
type: MMLCommand
name: LST SMSBACKUPSW（查询SMSF热备容灾功能开关状态）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSBACKUPSW
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 热备容灾
status: active
---

# LST SMSBACKUPSW（查询SMSF热备容灾功能开关状态）

## 功能

**适用NF：SMSF**

该命令用于查询SMSF热备容灾功能开关状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSBACKUPSW]] · SMSF热备容灾功能开关状态（SMSBACKUPSW）

## 使用实例

运营商希望查询SMSF热备容灾功能开关状态时，执行如下命令：

```
LST SMSBACKUPSW:;
%%LST SMSBACKUPSW:;%%
RETCODE = 0  操作成功

结果如下：
--------------
 SMSF热备容灾功能开关  =  打开	

(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMSBACKUPSW.md`
