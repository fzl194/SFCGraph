---
id: UNC@20.15.2@MMLCommand@SET NGRANOVERLOADCTRL
type: MMLCommand
name: SET NGRANOVERLOADCTRL（设置5G基站过载监控参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NGRANOVERLOADCTRL
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGRAN接入管理控制
status: active
---

# SET NGRANOVERLOADCTRL（设置5G基站过载监控参数）

## 功能

![](设置5G基站过载监控参数（SET NGRANOVERLOADCTRL）_61307354.assets/notice_3.0-zh-cn_2.png)

当OVERLOADTHD参数设置过小时，无业务影响，可能误上报告警。

**适用NF：AMF**

该命令用来设置5G基站过载监控相关参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| TALISTDETECSW | OVERLOADTHD | RECOVERTHD | PERRIOD |
| --- | --- | --- | --- |
| Off | 800 | 500 | 60 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TALISTDETECSW | TALIST下基站过载检测开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否开启TALIST下基站过载检测功能。<br>数据来源：本端规划<br>取值范围：<br>- “On（ON）”：ON<br>- “Off（OFF）”：OFF<br>默认值：无。<br>配置原则：无 |
| OVERLOADTHD | 过载阈值(个) | 可选必选说明：该参数在"TALISTDETECSW"配置为"On"时为条件可选参数。<br>参数含义：该参数用于指定TALIST下基站数的过载阈值。当TALIST下基站接入数量大于或等于该阈值时上报“ALM-100486 TALIST下5G基站接入数过载”告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是100~2000，单位是个。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGRANOVERLOADCTRL查询当前参数配置值。<br>配置原则：<br>“过载阈值”应大于或等于“恢复阈值”。 |
| RECOVERTHD | 恢复阈值(个) | 可选必选说明：该参数在"TALISTDETECSW"配置为"On"时为条件可选参数。<br>参数含义：该参数用于指定TALIST下基站数过载恢复阈值。TALIST下基站数小于该阈值时恢复告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是50~2000，单位是个。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGRANOVERLOADCTRL查询当前参数配置值。<br>配置原则：<br>“恢复阈值”必须小于或等于“过载阈值”。 |
| PERRIOD | 核查周期(分钟) | 可选必选说明：该参数在"TALISTDETECSW"配置为"On"时为条件可选参数。<br>参数含义：该参数用于TALIST下基站过载的核查周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~1440，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGRANOVERLOADCTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [5G基站过载监控参数（NGRANOVERLOADCTRL）](configobject/UNC/20.15.2/NGRANOVERLOADCTRL.md)

## 使用实例

开启TALIST下基站数过载检测功能，过载阈值为400，过载恢复阈值为300，检测周期为60分钟，执行如下命令：

```
SET NGRANOVERLOADCTRL: TALISTDETECSW=On, OVERLOADTHD=400, RECOVERTHD=300, PERRIOD=60;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置5G基站过载监控参数（SET-NGRANOVERLOADCTRL）_61307354.md`
