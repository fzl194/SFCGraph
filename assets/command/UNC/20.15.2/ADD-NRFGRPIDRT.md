---
id: UNC@20.15.2@MMLCommand@ADD NRFGRPIDRT
type: MMLCommand
name: ADD NRFGRPIDRT（增加NF组标识路由）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFGRPIDRT
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- NF实例组路由管理
status: active
---

# ADD NRFGRPIDRT（增加NF组标识路由）

## 功能

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增基于NF组标识的路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示通过NF组标识路由寻址的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- AUSF（AUSF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- PCF（PCF）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SMSF（SMSF）<br>默认值：无<br>配置原则：<br>当前NRF仅支持NFTYPE为AUSF、UDM、PCF、CUSTOM_OCS、SMSF的路由转发功能，其他NF类型为预留功能。 |
| NFGROUPID | NF组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示被寻址NF所在的NF实例组标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示当前NRF基于NF实例组标识寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数需通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFGRPIDRT]] · NF组标识路由（NRFGRPIDRT）

## 使用实例

- 运营商网络为三层组网，最高层PLMN-NRF，中间层H-NRF，最低层L-NRF。L-NRF1归属于H-NRF1，H-HRF1归属于PLMN-NRF。NF组标识为"nfgroupid01"的PCF归属于L-NRF1，当跨NRF进行服务发现，希望发现的目标为上述PCF时，需要在H-NRF1和PLMN-NRF上分别配置到PCF的路由信息。在H-NRF1上执行：
  ```
  ADD NRFGRPIDRT: NFTYPE=PCF, NFGROUPID="nfgroupid01", NEXTNRFGRPNAME="L-NRF1";
  ```
- 在PLMN-NRF上执行：
  ```
  ADD NRFGRPIDRT: NFTYPE=PCF, NFGROUPID="nfgroupid01", NEXTNRFGRPNAME="H-NRF1";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NRFGRPIDRT.md`
