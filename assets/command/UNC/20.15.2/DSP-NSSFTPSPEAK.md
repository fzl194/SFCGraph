---
id: UNC@20.15.2@MMLCommand@DSP NSSFTPSPEAK
type: MMLCommand
name: DSP NSSFTPSPEAK（显示NSSF每秒事务数峰值）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NSSFTPSPEAK
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF维测管理
status: active
---

# DSP NSSFTPSPEAK（显示NSSF每秒事务数峰值）

## 功能

**适用NF：NSSF**

该命令用于显示NSSF每秒事务数峰值信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NSSF每秒事务数峰值（NSSFTPSPEAK）](configobject/UNC/20.15.2/NSSFTPSPEAK.md)

## 使用实例

查询NSSF每秒事务数峰值信息。

```
%%DSP NSSFTPSPEAK:;%%
RETCODE = 0  执行成功

结果如下
--------
              POD名称  =  uncpod-0
24小时内最大值(个/秒)  =  35
48小时内最大值(个/秒)  =  38
    历史最大值(个/秒)  =  80
     48小时内峰值详情  =  0,0,0,0,0,0,35,0,0,0,0,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,38,0,0,30,0,0,0,0,0,0,0,0,0,0,1,2,1,2(current hour)
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NSSF每秒事务数峰值（DSP-NSSFTPSPEAK）_22678337.md`
