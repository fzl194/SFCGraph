---
id: UNC@20.15.2@MMLCommand@ADD SMACTIMEILIB
type: MMLCommand
name: ADD SMACTIMEILIB（增加IMEI库记录）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SMACTIMEILIB
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
- 业务安全管理
- 会话管理
- 激活过程管理
status: active
---

# ADD SMACTIMEILIB（增加IMEI库记录）

## 功能

**适用网元：SGSN、MME**

此命令用于增加终端IMEI记录。终端IMEI记录为IMEI TAC和终端类型的对应关系表，用于按照IMEI TAC识别智能终端类型。

## 注意事项

- 此命令最大记录为1000条。
- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEITAC | 设备型号核准号码 | 可选必选说明：必选参数<br>参数含义：该参数用于设置用户的设备型号核准号码。<br>数据来源：本端规划<br>取值范围：8位十进制数<br>默认值：无 |
| UETYPE | 终端类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置设备型号核准号码对应的终端类型。<br>数据来源：本端规划<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>默认值：无 |
| UEDESC | 终端详细信息 | 可选必选说明：可选参数<br>参数含义：该参数是对用户终端类型的详细描述。<br>数据来源：本端规划<br>取值范围：长度为32位的字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMACTIMEILIB]] · IMEI库记录（SMACTIMEILIB）

## 使用实例

配置针对BLACKBERRY终端类型，如果请求消息未携带APN，不进行请求信息纠正，且在用户签约野卡的情况下不进行纠错，拒绝该用户的激活请求，可以按照如下描述操作：

- 执行[**ADD SMACTIMEILIB**](增加IMEI库记录（ADD SMACTIMEILIB）_26305474.md)配置IMEI TAC与终端类型的映射关系；
- 执行[**ADD SMACTCTRL**](增加激活过程控制参数（ADD SMACTCTRL）_26305472.md)配置针对黑莓类型终端不进行请求信息纠正。

ADD SMACTIMEILIB: IMEITAC="12345678", UETYPE=BLACKBERRY;

ADD SMACTIMEILIB: IMEITAC="22345678", UETYPE=BLACKBERRY;

ADD SMACTCTRL: SUBRANGE=SPECIAL_UETYPE, UETYPE=BLACKBERRY, APNTYPE=NULL_APN, POLICY=MATCH_FAIL_NOTCORRECT, WILDCARDPLCY=REJECT;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SMACTIMEILIB.md`
