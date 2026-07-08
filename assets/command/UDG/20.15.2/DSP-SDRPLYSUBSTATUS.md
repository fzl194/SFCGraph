---
id: UDG@20.15.2@MMLCommand@DSP SDRPLYSUBSTATUS
type: MMLCommand
name: DSP SDRPLYSUBSTATUS（显示SDRC中保存的策略订阅关系）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SDRPLYSUBSTATUS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRPLYSUBSTATUS（显示SDRC中保存的策略订阅关系）

## 功能

该命令用于显示SDRC中保存的策略订阅关系。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLYTYPE | 策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定订阅者订阅的策略类型。<br>数据来源：本端规划<br>取值范围：<br>- APPROUTE（APPROUTE）<br>- TOPIC（TOPIC）<br>- VPN（VPN）<br>- VPNIP（VPNIP）<br>- TOKEN（TOKEN）<br>- KEYMATCH（KEYMATCH）<br>默认值：无<br>配置原则：无 |
| PLYKEY | 策略键值 | 可选必选说明：该参数在"PLYTYPE"配置为"TOKEN"、"KEYMATCH"时为条件必选参数。<br>参数含义：该参数用于指定策略键值，可以通过命令<br>[**DSP SDRPOLICYKEYS**](显示SDRC中的策略Key信息（DSP SDRPOLICYKEYS）_22132897.md)<br>获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SDRC中保存的策略订阅关系（SDRPLYSUBSTATUS）](configobject/UDG/20.15.2/SDRPLYSUBSTATUS.md)

## 使用实例

查询SDRC中保存的路由策略的订阅者信息：

```
%%DSP SDRPLYSUBSTATUS: PLYTYPE=TOKEN, PLYKEY=1007;%%
RETCODE = 0  操作成功

结果如下
--------
实例ID                进程标识                                      订阅时间             推送时间             订阅状态  

12369790900064901074  vsm-pod-fd475dc8f-ttwmp10-103-1-210__103__0  2022-11-01 14:48:51  2022-11-01 14:48:51  否
12369790900065032666  vsm-pod-fd475dc8f-6g5rr10-103-1-226__103__0  2022-11-01 14:48:51  2022-11-01 14:48:51  否
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示SDRC中保存的策略订阅关系（DSP-SDRPLYSUBSTATUS）_94588828.md`
