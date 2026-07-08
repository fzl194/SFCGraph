---
id: UNC@20.15.2@MMLCommand@LST PDUACTCTRL
type: MMLCommand
name: LST PDUACTCTRL（查询PDU会话激活控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PDUACTCTRL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- PDU会话激活控制参数
status: active
---

# LST PDUACTCTRL（查询PDU会话激活控制参数）

## 功能

**适用NF：AMF**

该命令用于查询基于DNN配置PDU会话激活处理策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户。<br>- “HOME_USER（本网用户）”：本网用户。<br>- “FOREIGN_USER（外网用户）”：外网用户。<br>- “IMSI_PREFIX（IMSI前缀）”：IMSI前缀。<br>- “SPECIFIC_IMSI（指定IMSI）”：指定IMSI。<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~14。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIC_IMSI"时为条件可选参数。<br>参数含义：该参数用于指定IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| DNNTYPE | DNN类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定请求DNN类型。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_DNN（所有DNN）”：表示请求DNN为任意DNN。<br>- “NOT_NULL_DNN（非空DNN）”：表示请求DNN为非空DNN。<br>- “NULL_DNN（空DNN）”：表示请求DNN为空DNN。<br>- “SPECIAL_DNN（指定DNN）”：表示请求DNN为指定DNN。<br>默认值：无<br>配置原则：<br>请求DNN为空时，选择“NULL_DNN”。<br>请求DNN为非空时，选择“NOT_NULL_DNN”。<br>请求DNN为指定DNN时，选择“SPECIAL_DNN”。<br>请求DNN包括空DNN和非空DNN时，选择“ALL_DNN”。 |
| DNN | 用户请求的DNN | 可选必选说明：该参数在"DNNTYPE"配置为"SPECIAL_DNN"时为条件可选参数。<br>参数含义：该参数用于指定用户请求的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PDUACTCTRL]] · PDU会话激活控制参数（PDUACTCTRL）

## 使用实例

查询基于DNN配置PDU会话激活处理策略，执行如下命令：

```
%%LST PDUACTCTRL:;%%
RETCODE = 0  操作成功

结果如下
------------------------
用户范围     IMSI前缀     IMSI             DNN类型     用户请求的DNN    处理策略  拒绝原因值  

本网用户     NULL         NULL             空DNN       NULL             直接拒绝  0             
指定IMSI     NULL         123456789012345  指定DNN     HUAWEI.COM       直接拒绝  0             
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PDUACTCTRL.md`
