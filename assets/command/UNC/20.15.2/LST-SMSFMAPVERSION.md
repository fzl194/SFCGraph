---
id: UNC@20.15.2@MMLCommand@LST SMSFMAPVERSION
type: MMLCommand
name: LST SMSFMAPVERSION（查询SMSF使用的MAP接口版本）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSFMAPVERSION
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 版本号管理
- MAP版本号管理
status: active
---

# LST SMSFMAPVERSION（查询SMSF使用的MAP接口版本）

## 功能

**适用NF：SMSF**

该命令用于查询SMSF/VLR在MO流程中使用的MAP接口版本。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [SMSF使用的MAP接口版本（SMSFMAPVERSION）](configobject/UNC/20.15.2/SMSFMAPVERSION.md)

## 使用实例

运营商希望查询SMSF使用的MAP接口版本，执行如下命令：

```
LST SMSFMAPVERSION:;
%%LST SMSFMAPVERSION:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
        MAP 版本号 =  V2
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMSF使用的MAP接口版本（LST-SMSFMAPVERSION）_44007231.md`
