---
id: UNC@20.15.2@MMLCommand@ADD APNFUNC
type: MMLCommand
name: ADD APNFUNC（增加APNNI功能配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNFUNC
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
max_records: 128
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- APN功能配置
status: active
---

# ADD APNFUNC（增加APNNI功能配置）

## 功能

**适用网元：SGSN**

该命令用于增加VIP用户的APN信息。

## 注意事项

- 此表最大记录数为128，VIP用户的APN最多允许配置128个。
- “APNNI（APN网络标识）”和“APNPURPOSE（APN用途）”同时确定一条记录。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。<br>数据来源：整网规划<br>取值范围：长度不超过62的字符串<br>默认值： 无<br>配置原则：<br>- APN网络标识由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。<br>说明：- APN网络标识不区分大小写。<br>- APNNI在APN中所处的位置，例如：example1.com.mnc123.mcc123.gprs，其中NI= example1.com， OI= mnc123.mcc123.gprs。 |
| APNPURPOSE | APN用途 | 可选必选说明：必选参数<br>参数含义：该参数决定了该APNNI所属用户是VIP用户。<br>数据来源：整网规划<br>取值范围：<br>- “VIP(VIP用户)”:标识该APNNI所属用户为VIP用户。<br>默认值： 无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNFUNC]] · APNNI功能配置（APNFUNC）

## 使用实例

增加记录，配置APNNI为"huawei1.com"的用户为VIP用户：

ADD APNFUNC: APNNI="huawei1.com", APNPURPOSE=VIP;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-APNFUNC.md`
