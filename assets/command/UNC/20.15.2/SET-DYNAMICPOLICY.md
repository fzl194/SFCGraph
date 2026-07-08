---
id: UNC@20.15.2@MMLCommand@SET DYNAMICPOLICY
type: MMLCommand
name: SET DYNAMICPOLICY（设置服务类型分配动态权重的管理策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DYNAMICPOLICY
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 权重分配管理
- 动态权重策略
status: active
---

# SET DYNAMICPOLICY（设置服务类型分配动态权重的管理策略）

## 功能

![](设置服务类型分配动态权重的管理策略（SET DYNAMICPOLICY）_24015952.assets/notice_3.0-zh-cn_2.png)

如果配置不合理会导致不同POD间负载不均衡。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置指定服务类型的动态权重调整的动态负载均衡参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SERVICETYPE | ADJUSTTHRESHOLD | GAPTHRESHOLD | GLBBASECOST | GAPBUSY |
| --- | --- | --- | --- | --- |
| UAM_0 | 65 | 6 | 5 | 10 |
| USM_0 | 65 | 6 | 5 | 10 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务类型。<br>数据来源：本端规划<br>取值范围：<br>- “UAM_0（UAM_0）”：涉及如下类型POD：接入/移动性管理POD。<br>- “USM_0（USM_0）”：涉及如下类型POD：会话管理POD。<br>默认值：无。<br>配置原则：无 |
| ADJUSTTHRESHOLD | 调整阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定动态负载的调整阈值，同类型业务POD CPU使用率小于此数值时不进行动态负载调整。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是40~100。单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DYNAMICPOLICY查询当前参数配置值。<br>配置原则：无 |
| GAPTHRESHOLD | 差值门限 | 可选必选说明：可选参数<br>参数含义：该参数用于指定动态负载的差值门限，同类型业务POD间CPU使用率差值小于此数值时不进行动态负载调整。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~20。单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DYNAMICPOLICY查询当前参数配置值。<br>配置原则：无 |
| GLBBASECOST | 基础消耗 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基础消耗，表示POD空载时的CPU使用率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~15。单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DYNAMICPOLICY查询当前参数配置值。<br>配置原则：无 |
| GAPBUSY | 忙时差值门限 | 可选必选说明：可选参数<br>参数含义：该参数用于指定忙时差值门限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~20。单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DYNAMICPOLICY查询当前参数配置值。<br>配置原则：<br>忙时周期内出现异常CPU的偏差值。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DYNAMICPOLICY]] · 服务类型分配动态权重的管理策略（DYNAMICPOLICY）

## 使用实例

对服务类型为USM_0，调整阈值为75，差值门限为7，基础消耗为6，忙时差值门限为10的POD配置动态权重，执行如下命令：

```
SET DYNAMICPOLICY: SERVICETYPE=USM_0, ADJUSTTHRESHOLD=75, GAPTHRESHOLD=7, GLBBASECOST=6, GAPBUSY=10, CONFIRM=Y;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置服务类型分配动态权重的管理策略（SET-DYNAMICPOLICY）_24015952.md`
