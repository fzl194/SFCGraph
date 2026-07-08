---
id: UNC@20.15.2@MMLCommand@DSP SDRPOLICYKEYS
type: MMLCommand
name: DSP SDRPOLICYKEYS（显示SDRC中的策略Key信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SDRPOLICYKEYS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRPOLICYKEYS（显示SDRC中的策略Key信息）

## 功能

该命令用于显示SDRC中的策略Key信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYTYPE | 策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定策略类型。<br>数据来源：本端规划<br>取值范围：<br>- AppRoute（AppRoute）<br>- Token（Token）<br>- Service（Service）<br>- NextHop（NextHop）<br>- KeyMatch（KeyMatch）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SDRPOLICYKEYS]] · SDRC中的策略Key信息（SDRPOLICYKEYS）

## 使用实例

查询AppRoute存储的key信息：

```
%%DSP SDRPOLICYKEYS: POLICYTYPE=AppRoute;%%
RETCODE = 0  操作成功

结果如下
--------
Sdrc存储策略的Key
125
114
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SDRPOLICYKEYS.md`
