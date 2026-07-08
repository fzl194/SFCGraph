---
id: UNC@20.15.2@MMLCommand@ADD LAIVLRBLACKLIST
type: MMLCommand
name: ADD LAIVLRBLACKLIST（增加LAIVLR黑名单）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LAIVLRBLACKLIST
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 256
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- MSC POOL管理
- LAIVLR黑名单管理
status: active
---

# ADD LAIVLRBLACKLIST（增加LAIVLR黑名单）

## 功能

**适用网元：MME**

该命令用于MSC POOL场景下，当BSC与某个或多个MSC连接中断但与其它MSC连接正常时，增加LAI与MSC/VLR的黑名单对应关系。 UNC 选择黑名单以外MSC POOL内的其它正常MSC/VLR进行服务。

## 注意事项

- 该命令执行后立即生效。
- 该表最大记录数为256。
- 执行前请确认LAI与MSC/VLR的黑名单对应关系配置是否正确，避免造成预期外的影响。
- 若配置的MSC/VLR不在MSC POOL内，则认为黑名单功能失效，会按照原有MSC/VLR选择方式重新进行选择，原有选择方式参见“WSFD-102301基于CSFB的语音业务”中的描述。
- 如果Pool里所有的MSC/VLR都被配成黑名单，则认为黑名单功能失效，会按照原有MSC/VLR选择方式重新进行选择，原有选择方式参见“WSFD-102301基于CSFB的语音业务”中的描述。
- “起始LAI”和“VLR号”的组合确定唯一一条LAI与VLR的黑名单对应关系记录。
- 同一个VLR号，可对应多个LAI区间，但是LAI区间不可以覆盖或重复。
- 同一个LAI区间，可对应多个VLR号，但不能超过32个，VLR号不可以重复。
- 配置黑名单后，针对联合附着/联合TAU接入系统的新用户可以立即生效，即选择到正确的MSC/VLR，但是对于系统上已有用户不能立即生效，可能造成一次语音被叫业务失败，后续UE自动回到4G网络发起联合附着/联合TAU可以重新选正确的MSC/VLR。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VN | VLR号 | 可选必选说明：必选参数<br>参数说明：该参数用于表示位置区对应的VLR号码。<br>前提条件：该参数必须先由<br>[**ADD VLR**](../../VLR管理/增加VLR配置信息(ADD VLR)_26305254.md)<br>命令定义。<br>数据来源：整网规划<br>取值范围： 1～15位十进制数字<br>默认值：无<br>配置原则：一个VLR号可对应多个LAI区间。 |
| BGNLAI | 起始LAI | 可选必选说明：必选参数<br>参数含义：该参数是指对应一个VLR号的LAI黑名单的起始位置区，由“MCC”、“MNC”和“LAC”组成。<br>数据来源：整网规划<br>取值范围：9~10位字符串<br>默认值：无<br>配置原则：<br>- “MCC”由3个阿拉伯数字组成，“MNC”由2到3个阿拉伯数字组成。<br>- “LAC”编码为16进制数，固定为4位，不足前面补0。 |
| ENDLAI | 终止LAI | 可选必选说明：可选参数<br>参数含义：该参数是指对应一个VLR号的LAI范围内数值最大的终止位置区，由“MCC”、“MNC”和“LAC”组成。<br>数据来源：整网规划<br>取值范围：9~10位字符串<br>默认值：无<br>配置原则：<br>- “MCC”由3个阿拉伯数字组成，“MNC”由2到3个阿拉伯数字组成。<br>- “LAC”编码为16进制数，固定为4位，不足前面补0。<br>- 输入参数终止LAI要大于或等于起始LAI。<br>- 如果未输入终止LAI且起始LAI完整则表示某个固定的起始LAI对应到某个VLR，即终止LAI等于起始LAI。请见命令使用实例2。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LAIVLRBLACKLIST]] · LAIVLR黑名单（LAIVLRBLACKLIST）

## 使用实例

1. 增加位置区标识范围为"308013101"到"308013103"的区域与VLR为"12345678912"的黑名单对应关系：
  ADD LAIVLRBLACKLIST: VN="12345678912", BGNLAI="308013101", ENDLAI="308013103";
2. 增加位置区标识为"308013104"的区域与VLR为"12345678912"的黑名单对应关系：
  ADD LAIVLRBLACKLIST: VN="12345678912", BGNLAI="308013104";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-LAIVLRBLACKLIST.md`
