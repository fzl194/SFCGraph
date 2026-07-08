---
id: UNC@20.15.2@MMLCommand@LST ALLOWDNN
type: MMLCommand
name: LST ALLOWDNN（查询允许本地专网分流的DNN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ALLOWDNN
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 本地分流管理
status: active
---

# LST ALLOWDNN（查询允许本地专网分流的DNN）

## 功能

**适用NF：AMF**

该命令用于增加查询进行本地专网分流的UE请求DNN和替换DNN。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REQDNN | UE请求DNN | 可选必选说明：可选参数<br>参数含义：该参数用于指定允许进行本地专网分流的UE请求DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| REPLDNN | PDU会话替换DNN | 可选必选说明：可选参数<br>参数含义：该参数用于指定允许本地专网分流的替换DNN，在PDU会话创建时使用selectedDnn带给SMF，该DNN由PCF在满足条件时下发。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ALLOWDNN]] · 允许本地专网分流的DNN（ALLOWDNN）

## 使用实例

查询系统中当前配置的本地专网分流策略，执行如下命令：

```
%%LST ALLOWDNN:;%%
RETCODE = 0  操作成功

结果如下
------------------------
     UE请求DNN  =  1234567
PDU会话替换DNN  =  ABCDEF
(结果个数  = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ALLOWDNN.md`
