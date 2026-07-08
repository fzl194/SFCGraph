---
id: UNC@20.15.2@MMLCommand@SET SBILINKSETCFG
type: MMLCommand
name: SET SBILINKSETCFG（设置服务化接口链路集属性）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SBILINKSETCFG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口链路集管理
status: active
---

# SET SBILINKSETCFG（设置服务化接口链路集属性）

## 功能

该命令用于设置服务化接口链路集的属性配置信息，该属性设置后整系统生效。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SETAGINGTIME | FQDNCHECKSWITCH | FAULTLINKPCT | FAULTPROCESSPCT |
| --- | --- | --- | --- |
| 10 | ON | 50 | 20 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SETAGINGTIME | 链路集老化时间(小时) | 可选必选说明：可选参数<br>参数含义：该参数用于指定链路集老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~72，单位是小时。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SBILINKSETCFG查询当前参数配置值。<br>配置原则：无 |
| FQDNCHECKSWITCH | FQDN周期性检查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否开启周期性检查链路集FQDN对应的IP地址的功能。<br>数据来源：本端规划<br>取值范围：<br>- OFF（关闭）<br>- ON（打开）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SBILINKSETCFG查询当前参数配置值。<br>配置原则：无 |
| FAULTLINKPCT | 进程内链路集故障阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于判定链路集在单个HTTP进程中是否为故障，当故障链路数占比大于等于此参数，则认为进程内到对端的链路集故障。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。当该参数设置为0时，则按照默认值生效。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SBILINKSETCFG查询当前参数配置值。<br>配置原则：<br>如果针对所有链路集均生效，则配置该参数。如果针对某个对端NF的链路集生效，则使用<br>[**ADD SBILINKSETPROP**](../服务化接口链路集策略管理/增加SBI链路集策略（ADD SBILINKSETPROP）_29053325.md)<br>命令配置。如果都配置，则优先使用<br>[**ADD SBILINKSETPROP**](../服务化接口链路集策略管理/增加SBI链路集策略（ADD SBILINKSETPROP）_29053325.md)<br>的命令配置生效。 |
| FAULTPROCESSPCT | 系统内链路集故障阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于判定链路集在系统内是否为故障，当存在链路集故障的进程数占比大于等于此参数，则认为系统内链路集故障，该链路集对应的NF服务不可达。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。当该参数设置为0时，则按照默认值生效。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SBILINKSETCFG查询当前参数配置值。<br>配置原则：<br>如果针对所有链路集均生效，则配置该参数。如果针对某个对端NF的链路集生效，则使用<br>[**ADD SBILINKSETPROP**](../服务化接口链路集策略管理/增加SBI链路集策略（ADD SBILINKSETPROP）_29053325.md)<br>命令配置。如果都配置，则优先使用<br>[**ADD SBILINKSETPROP**](../服务化接口链路集策略管理/增加SBI链路集策略（ADD SBILINKSETPROP）_29053325.md)<br>的命令配置生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SBILINKSETCFG]] · 服务化接口链路集属性（SBILINKSETCFG）

## 使用实例

设置链路集老化时间为10，可以执行如下命令：

```
SET SBILINKSETCFG:SETAGINGTIME=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置服务化接口链路集属性（SET-SBILINKSETCFG）_83653668.md`
