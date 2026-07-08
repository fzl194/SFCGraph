---
id: UNC@20.15.2@MMLCommand@ADD ALLOWDNN
type: MMLCommand
name: ADD ALLOWDNN（增加允许本地专网分流的DNN）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ALLOWDNN
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 本地分流管理
status: active
---

# ADD ALLOWDNN（增加允许本地专网分流的DNN）

## 功能

**适用NF：AMF**

该命令用于增加允许进行本地专网分流的UE请求DNN和替换DNN，UE请求DNN和替换DNN都匹配时，才会创建或重建对应的本地分流PDU会话。

## 注意事项

- 该命令执行后立即生效。

- 该命令"REQDNN"和"REPLDNN"参数的取值不能与"ADD NGEMGCFG"命令中"DNN"参数的取值相同。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REQDNN | UE请求DNN | 可选必选说明：必选参数<br>参数含义：该参数用于指定允许进行本地专网分流的UE请求DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| REPLDNN | PDU会话替换DNN | 可选必选说明：必选参数<br>参数含义：该参数用于指定允许本地专网分流的替换DNN，在PDU会话创建时使用selectedDnn带给SMF，该DNN由PCF在满足条件时下发。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ALLOWDNN]] · 允许本地专网分流的DNN（ALLOWDNN）

## 使用实例

添加本地专网分流策略，执行如下命令：

```
ADD ALLOWDNN: REQDNN="1234567", REPLDNN="abcdef";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-ALLOWDNN.md`
