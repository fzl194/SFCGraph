---
id: UNC@20.15.2@MMLCommand@DSP IMSBYPASSUSER
type: MMLCommand
name: DSP IMSBYPASSUSER（显示进入语音PCF/PCRF故障Bypass状态的用户的IMSI列表）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: IMSBYPASSUSER
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 语音PCF_PCRF Bypass管理
status: active
---

# DSP IMSBYPASSUSER（显示进入语音PCF/PCRF故障Bypass状态的用户的IMSI列表）

## 功能

**适用NF：SMF、PGW-C**

该命令用于显示进入语音PCF/PCRF故障Bypass状态的用户的IMSI列表。

## 注意事项

该命令每个进程最多显示10个用户。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSBYPASSUSER]] · 进入语音PCF/PCRF故障Bypass状态的用户的IMSI列表（IMSBYPASSUSER）

## 使用实例

查询进入语音PCF/PCRF故障Bypass状态的用户的IMSI列表：

```
%%DSP IMSBYPASSUSER:;%%
RETCODE = 0  操作成功

结果如下
------------------------
国际移动用户标识  =  123031500010001
         POD名称  =  uncpod-0
    策略接口类型  =  Interface_N7
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-IMSBYPASSUSER.md`
