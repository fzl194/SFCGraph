---
id: UNC@20.15.2@MMLCommand@LST VLRMAPVERSION
type: MMLCommand
name: LST VLRMAPVERSION（查询VLR使用的MAP接口版本）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VLRMAPVERSION
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- MAP版本号管理
status: active
---

# LST VLRMAPVERSION（查询VLR使用的MAP接口版本）

## 功能

**适用NF：SMSF**

该命令用于查询VLR对接HLR业务中使用的MAP接口版本号。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [VLR使用的MAP接口版本（VLRMAPVERSION）](configobject/UNC/20.15.2/VLRMAPVERSION.md)

## 使用实例

运营商希望查询VLR对接HLR业务中使用的MAP接口版本号，执行如下命令：

```
LST VLRMAPVERSION:;
%%LST VLRMAPVERSION:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
        MAP 版本号 =  V3
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VLR使用的MAP接口版本（LST-VLRMAPVERSION）_53321874.md`
