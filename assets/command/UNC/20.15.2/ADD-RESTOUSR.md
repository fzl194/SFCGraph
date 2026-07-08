---
id: UNC@20.15.2@MMLCommand@ADD RESTOUSR
type: MMLCommand
name: ADD RESTOUSR（增加容灾用户特征参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: RESTOUSR
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- MME容灾管理
- 容灾用户特征管理
status: active
---

# ADD RESTOUSR（增加容灾用户特征参数）

## 功能

**适用网元：MME**

本命令应用于MME链式备份业务调测，用于增加支持容灾备份的用户特征，即IMSI。

启用“WSFD- 201201 MME链式备份”特性license后，若“容灾功能运行模式”设定为“调测模式”，系统根据本命令的配置记录对用户的IMSI进行匹配，匹配成功的用户才能使用备份功能。

## 注意事项

- 如果只购买“MME链式备份”的license，未购买“本地VLR”的license，“MME链式备份”特性只对VoLTE用户生效；如果同时购买“MME链式备份”和“本地VLR”的license，“MME链式备份”特性对4G用户生效。是否已购买“MME链式备份”、“本地VLR”的license，请执行 [**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md) 命令查看，生效的资源总数请执行[**DSP LICENSERES**](../../../../../../平台服务管理/操作维护/License管理/显示License资源（DSP LICENSERES）_51174310.md)命令查看。
- 该命令执行后立即生效。
- 仅当[**SET RESTOFUNC**](../容灾功能管理/设置容灾功能(SET RESTOFUNC)_72345713.md)中“容灾功能运行模式”参数设置为“调测模式”时，本命令允许增加新记录。
- 本表最大允许配置16条记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：本参数用于增加应用容灾备份功能的IMSI前缀。<br>数据来源：本端规划<br>取值范围：5~15位数字<br>默认值：无<br>配置原则：允许配置最长包含关系的IMSI前缀（但不允许记录重复），任意一条记录匹配成功均认为符合满足容灾功能的用户。 |

## 操作的配置对象

- [容灾用户特征参数（RESTOUSR）](configobject/UNC/20.15.2/RESTOUSR.md)

## 使用实例

增加IMSI前缀为465231的用户，用于调测“WSFD- 201201 MME链式备份”特性，执行如下命令：

ADD RESTOUSR: IMSIPRE="465231";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加容灾用户特征参数(ADD-RESTOUSR)_26305926.md`
