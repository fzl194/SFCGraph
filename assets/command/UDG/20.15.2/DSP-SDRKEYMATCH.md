---
id: UDG@20.15.2@MMLCommand@DSP SDRKEYMATCH
type: MMLCommand
name: DSP SDRKEYMATCH（显示SDRC中的KeyMatch信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SDRKEYMATCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRKEYMATCH（显示SDRC中的KeyMatch信息）

## 功能

该命令用于查询SDRC中指定AppType的KeyMatch策略信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPTYPE | App类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示该KeyMatch所归属业务的类型，可通过<br>[**DSP SDRPOLICYKEYS**](显示SDRC中的策略Key信息（DSP SDRPOLICYKEYS）_22132897.md)<br>: POLICYTYPE=KeyMatch;命令获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SDRC中的KeyMatch信息（SDRKEYMATCH）](configobject/UDG/20.15.2/SDRKEYMATCH.md)

## 使用实例

使用如下命令查询SDRC中缓存的KeyMatch策略信息：

```
%%DSP SDRKEYMATCH: APPTYPE=1035;%%
RETCODE = 0  操作成功

结果如下
--------
App类型                        身份标识

1035                              65465
1035                              10554
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示SDRC中的KeyMatch信息（DSP-SDRKEYMATCH）_01704014.md`
