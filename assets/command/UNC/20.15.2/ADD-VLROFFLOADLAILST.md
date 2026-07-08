---
id: UNC@20.15.2@MMLCommand@ADD VLROFFLOADLAILST
type: MMLCommand
name: ADD VLROFFLOADLAILST（增加位置区列表）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: VLROFFLOADLAILST
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 128
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- MSC POOL管理
- 基于LAI的IMSI分离配置信息
status: active
---

# ADD VLROFFLOADLAILST（增加位置区列表）

## 功能

**适用网元：MME**

本命令用于增加一个待处理的LAI，当执行 [**STR VLROFFLOADBYLAI**](../基于LAI的IMSI分离业务/启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)_26305240.md) 命令后，系统会对该LAI对应的TAI下面联合附着的4G用户执行IMSI分离操作。本命令可用于将BSC/RNC设备从一个MSC POOL下割接到另一个MSC POOL下时CSFB业务主动恢复场景。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为128。
- 如果在对4G用户执行IMSI分离操作任务的运行期间（可通过[**DSP VLROFFLOADBYLAI**](../基于LAI的IMSI分离业务/显示IMSI分离4G用户任务运行状态(DSP VLROFFLOADBYLAI)_26145426.md)查询）执行本命令，则系统不会立即处理新的任务，本次任务结束后，再次执行[**STR VLROFFLOADBYLAI**](../基于LAI的IMSI分离业务/启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)_26305240.md)命令系统才会处理。
- LAI与TAI的对应关系由[**ADD TAILAI**](../../TAI与LAI对应关系/增加TAI与LAI对应关系(ADD TAILAI)_72345017.md)命令配置。
- 此命令涉及CSFB被叫恢复特性（特性编号：WSFD-102503，license部件编码：LKV2CSCR01），执行命令前请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“打开”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LAI | LAI | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区标识，标识一个位置区。<br>数据来源：整网规划<br>取值范围：9～10位的字符串<br>默认值：无<br>配置原则：<br>- LAI由MCC，MNC，LAC组成。<br>- MCC为3个BCD码字符，MNC为2个或者3个BCD码字符。<br>- LAC编码为16进制数，固定为4位，不足在前面补0。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLROFFLOADLAILST]] · 位置区列表（VLROFFLOADLAILST）

## 使用实例

**任务描述：**

假设某运营商将BSC/RNC设备从一个MSC POOL下割接到另一个MSC POOL下，为避免BSC/RNC下的用户长时间滞留在旧的MSC POOL上，造成CSFB被叫业务失败，可通过本命令指定BSC/RNC下的LAI，然后再执行 [**STR VLROFFLOADBYLAI**](../基于LAI的IMSI分离业务/启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)_26305240.md) 启动对该LAI对应的TAI下面联合附着的4G用户执行IMSI分离操作的任务。

**配置脚本：**

1. 增加一个待处理的LAI到LAI列表，LAI的值为“308010001”：
  ADD VLROFFLOADLAILST: LAI="308010001";
2. 对本命令配置的所有LAI对应的TAI下面联合附着的4G用户，执行IMSI分离操作：
  STR VLROFFLOADBYLAI:;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-VLROFFLOADLAILST.md`
