---
id: UNC@20.15.2@MMLCommand@MOD IPAREAGP
type: MMLCommand
name: MOD IPAREAGP（修改IP区域群）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IPAREAGP
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 基于位置分配IP地址管理
- IP区域群管理
status: active
---

# MOD IPAREAGP（修改IP区域群）

## 功能

**适用网元：SGSN、MME**

该命令用于修改IP区域群的属性。

## 注意事项

- 此命令执行后立即生效。
- 此配置涉及License（License部件编码：LKV2IPRL01），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域群标识 | 可选必选说明：必选参数<br>参数含义：该参数用于标识待修改的区域群。<br>数据来源：整网规划<br>取值范围：1~256<br>默认值：无 |
| IPAREASW | IP区域开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定打开或者关闭IP区域管理功能。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(开启)”<br>默认值：无<br>配置原则：建议值为“OFF(关闭)”。 |
| ROAMUSRSW | 漫游用户开关 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置漫游用户限制接入开关。<br>前提条件：该参数在<br>“IPAREASW(IP区域开关)”<br>参数设置为<br>“ON(开启)”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(开启)”<br>默认值：无<br>配置原则：建议值为“OFF(关闭)”。 |
| NONLOCALUSRSW | 本网异地用户开关 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置本网异地用户限制接入开关。<br>前提条件：该参数在<br>“IPAREASW(IP区域开关)”<br>参数设置为<br>“ON(开启)”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(开启)”<br>默认值：无<br>配置原则：建议值为“OFF(关闭)”。 |
| AREAN | 区域群名称 | 可选必选说明：可选参数<br>参数含义：该参数用于修改区域群名称。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPAREAGP]] · IP区域群（IPAREAGP）

## 使用实例

若对标识为1的IP区域群中漫游用户和本网异地用户限制接入，则将IP区域群记录修改如下：

MOD IPAREAGP: AREAID=1, IPAREASW=ON, ROAMUSRSW=ON, NONLOCALUSRSW=ON;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-IPAREAGP.md`
