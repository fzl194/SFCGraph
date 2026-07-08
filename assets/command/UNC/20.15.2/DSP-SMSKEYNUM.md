---
id: UNC@20.15.2@MMLCommand@DSP SMSKEYNUM
type: MMLCommand
name: DSP SMSKEYNUM（显示SMSF/VLR用户关键信息表的用户数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMSKEYNUM
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

# DSP SMSKEYNUM（显示SMSF/VLR用户关键信息表的用户数）

## 功能

**适用NF：SMSF**

该命令用于查询SMSF/VLR用户关键信息表的用户数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSKEYNUM]] · SMSF/VLR用户关键信息表的用户数（SMSKEYNUM）

## 使用实例

当运营商希望查询SMSF/VLR用户关键信息表的用户数，执行如下命令：

```
DSP SMSKEYNUM:;
%%DSP SMSKEYNUM:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
                    PODID  =  uncpod-0
关键信息表的用户数(个)  =  1

(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示SMSF_VLR用户关键信息表的用户数（DSP-SMSKEYNUM）_81080353.md`
