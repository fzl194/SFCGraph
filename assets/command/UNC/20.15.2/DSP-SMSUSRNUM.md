---
id: UNC@20.15.2@MMLCommand@DSP SMSUSRNUM
type: MMLCommand
name: DSP SMSUSRNUM（显示SMSF中注册的用户数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMSUSRNUM
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 用户上下文管理
- SMS上下文
status: active
---

# DSP SMSUSRNUM（显示SMSF中注册的用户数）

## 功能

**适用NF：SMSF**

该命令用于查询当前在SMSF系统中注册的用户数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [SMSF中注册的用户数（SMSUSRNUM）](configobject/UNC/20.15.2/SMSUSRNUM.md)

## 使用实例

运营商想要查询系统中用户数，执行如下命令：

```
DSP SMSUSRNUM:;
%%DSP SMSUSRNUM:;%%
RETCODE = 0  操作成功

结果如下：
--------
注册用户数  PODID                     

0           sms-pod-7f777cfbff-tb2pl  
1           sms-pod-7f777cfbff-n8w6n  
0           sms-pod-7f777cfbff-nm652
1           total                     
(结果个数 = 4)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示SMSF中注册的用户数（DSP-SMSUSRNUM）_25120882.md`
