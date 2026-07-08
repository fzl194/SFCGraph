---
id: UNC@20.15.2@MMLCommand@LST CDFTOKENPOLICY
type: MMLCommand
name: LST CDFTOKENPOLICY（查询CDF token策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CDFTOKENPOLICY
command_category: 查询类
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

# LST CDFTOKENPOLICY（查询CDF token策略）

## 功能

**适用NF：NCG**

该命令用于查询cdf token权重上报开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WEIGHTSWITCH | cdf token权重开关 | 可选必选说明：可选参数<br>参数含义：设置CDF token权重开关。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：需要上报cdf token权重时，需要配置权重开关为使能<br>- “DISABLE（不使能）”：不需要上报cdf token权重时，需要配置权重开关为不使能<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDFTOKENPOLICY]] · CDF token策略（CDFTOKENPOLICY）

## 使用实例

查询cdf token权重开关配置：

```
+++    UNC/*MEID:0 MENAME:UNC_VNF_ncg001*/        2022-05-24 20:27:32+8:00
O&M    #3936
%%LST CDFTOKENPOLICY:;%%
RETCODE = 0  操作成功

结果如下
--------
cdf token权重开关  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CDF-token策略（LST-CDFTOKENPOLICY）_66773960.md`
