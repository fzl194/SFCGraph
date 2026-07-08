---
id: UNC@20.15.2@MMLCommand@DSP UDMBYPASSNUM
type: MMLCommand
name: DSP UDMBYPASSNUM（显示UDM Bypass用户数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: UDMBYPASSNUM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 可靠性管理
- AMF的UDM故障BYPASS功能
status: active
---

# DSP UDMBYPASSNUM（显示UDM Bypass用户数）

## 功能

**适用NF：AMF**

该命令用于查询AMF系统内处于UDM Bypass状态的用户数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [UDM Bypass用户数（UDMBYPASSNUM）](configobject/UNC/20.15.2/UDMBYPASSNUM.md)

## 使用实例

查看AMF系统内处于UDM Bypass状态的用户数，执行如下命令：

```
%%DSP UDMBYPASSNUM:;%%
RETCODE = 0  操作成功

结果如下
------------------------
POD ID    UDM Bypass用户数

uncpod-0  10
total     10
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示UDM-Bypass用户数（DSP-UDMBYPASSNUM）_96589089.md`
