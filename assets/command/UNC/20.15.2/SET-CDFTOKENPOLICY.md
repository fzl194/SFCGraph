---
id: UNC@20.15.2@MMLCommand@SET CDFTOKENPOLICY
type: MMLCommand
name: SET CDFTOKENPOLICY（设置CDF token策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CDFTOKENPOLICY
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- CDF token策略
status: active
---

# SET CDFTOKENPOLICY（设置CDF token策略）

## 功能

![](设置CDF token策略（SET CDFTOKENPOLICY）_14295033.assets/notice_3.0-zh-cn_2.png)

当CDFTOKENPOLICY开关配置为使能且设置cdf token权重时，会影响各个cgfa-pod与cgfb-pod或cgfa2-pod与cgfb2-pod之间的token权重分配，从而影响话务量均衡。

**适用NF：NCG**

该命令用于设置cdf token权重上报开关。

当需要上报cdf token权重时，可配置cdf权重开关为使能。

## 注意事项

- 该命令执行后需要重新启动系统才能生效。

- 该命令需重启DCF进程才会生效。重启DCF进程的命令如下：
- RST MSPROCESS: PROCOBJECT=PROCNAME, PROCNAME="CELL_DCF";

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| WEIGHTSWITCH |
| --- |
| ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WEIGHTSWITCH | cdf token权重开关 | 可选必选说明：必选参数<br>参数含义：设置CDF token权重开关。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：需要上报cdf token权重时，需要配置权重开关为使能<br>- “DISABLE（不使能）”：不需要上报cdf token权重时，需要配置权重开关为不使能<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDFTOKENPOLICY]] · CDF token策略（CDFTOKENPOLICY）

## 使用实例

设置cdf token权重开关为使能：

```
+++    UNC/*MEID:0 MENAME:UNC_VNF_ncg001*/        2022-05-24 20:25:44+8:00
O&M    #3935
%%SET CDFTOKENPOLICY: WEIGHTSWITCH=ENABLE;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置CDF-token策略（SET-CDFTOKENPOLICY）_14295033.md`
