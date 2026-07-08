---
id: UNC@20.15.2@MMLCommand@ADD RESTOAPN
type: MMLCommand
name: ADD RESTOAPN（增加容灾APN特征参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: RESTOAPN
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- MME容灾管理
- 容灾APN特征管理
status: active
---

# ADD RESTOAPN（增加容灾APN特征参数）

## 功能

**适用网元：MME**

本命令用于增加支持容灾备份的APN，即APNNI。启用“MME链式备份特性”后，若用户激活的PDN连接的APNNI与本命令配置的APNNI匹配，此用户支持容灾备份功能；反之，用户不支持容灾备份功能。

## 注意事项

- 如果只购买“MME链式备份”的license，未购买“本地VLR”的license，“MME链式备份”特性只对VoLTE用户生效；如果同时购买“MME链式备份”和“本地VLR”的license，“MME链式备份”特性对4G用户生效。是否已购买“MME链式备份”、“本地VLR”的license，请执行 [**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md) 命令查看，生效的资源总数请执行[**DSP LICENSERES**](../../../../../../平台服务管理/操作维护/License管理/显示License资源（DSP LICENSERES）_51174310.md)命令查看。
- “IMS”为系统缺省的APNNI记录，无需增加，也不能删除。
- 本表最大允许配置3000条记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：本参数用于增加应用容灾备份功能的APNNI特征。<br>数据来源：全网规划<br>取值范围：1~62位字符串<br>默认值：无<br>配置原则：<br>- “IMS”为系统缺省记录，不允许重复添加。<br>- 若APNNI输入仅为通配符“*”，表示所有域名。若APNNI输入的字符串中出现“*”，认为是普通字符。<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESTOAPN]] · 容灾APN特征参数（RESTOAPN）

## 使用实例

当现网需要启用“WSFD- 201201 MME链式备份”特性时，用于增加支持容灾备份的APN特征，执行如下命令：

ADD RESTOAPN: APNNI="HUAWEI.COM";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加容灾APN特征参数(ADD-RESTOAPN)_26305924.md`
