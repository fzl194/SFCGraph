---
id: UNC@20.15.2@MMLCommand@ADD IMEILIB
type: MMLCommand
name: ADD IMEILIB（增加IMEI库记录）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IMEILIB
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
- Smartphone管理
- 终端类型识别
- IMEI库管理
status: active
---

# ADD IMEILIB（增加IMEI库记录）

## 功能

**适用网元：SGSN、MME**

此命令用于增加IMEI库记录。IMEI库为IMEI TAC和终端类型的对应关系表，用于按照IMEI TAC识别智能终端类型。

当需要增加一条IMEI TAC和终端类型的对应记录时，需要执行此命令。

## 注意事项

- 此命令最大记录为20000条。
- 此命令执行后立即生效。
- 添加IMEI TAC对应的终端类型记录后，要使用基于终端类型的性能统计功能，还需要加载License项“Smartphone话务模型统计”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEITAC | 设备型号核准号码 | 可选必选说明：必选参数<br>参数含义：该参数用于设置用户的设备型号核准号码。<br>数据来源：本端规划<br>取值范围：8~15位十进制数<br>默认值：无 |
| UETYPE | 终端类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置设备型号核准号码对应的终端类型。<br>数据来源：本端规划<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>默认值：无 |
| UEDESC | 终端详细信息 | 可选必选说明：可选参数<br>参数含义：该参数是对用户终端类型的详细描述。<br>数据来源：本端规划<br>取值范围：长度为255位的字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMEILIB]] · IMEI库记录（IMEILIB）

## 使用实例

增加设备型号核准号码为12345678，用户终端类型为黑莓的记录：

ADD IMEILIB: IMEITAC="12345678", UETYPE=BLACKBERRY;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加IMEI库记录（ADD-IMEILIB）_26145734.md`
