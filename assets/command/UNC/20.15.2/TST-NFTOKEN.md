---
id: UNC@20.15.2@MMLCommand@TST NFTOKEN
type: MMLCommand
name: TST NFTOKEN（测试Token分配）
nf: UNC
version: 20.15.2
verb: TST
object_keyword: NFTOKEN
command_category: 调测类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF业务调测
status: active
---

# TST NFTOKEN（测试Token分配）

## 功能

**适用NF：NRF**

该命令用于测试NRF上NF的Token分配流程。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | 源NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数表示Token请求的源NF实例标识，即NF服务消费者的NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。<br>默认值：无<br>配置原则：无 |
| TNFINSTANCEID | 目标NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数表示Token请求中的目标NF实例标识，即NF服务提供方的NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。<br>默认值：无<br>配置原则：无 |
| SCOPE | 目标服务名称列表 | 可选必选说明：必选参数<br>参数含义：该参数表示Token请求中的目标NF服务实例列表。如果有多个服务名称，用“%20”隔开。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| REQMCC | 源MCC | 可选必选说明：可选参数<br>参数含义：该参数表示Token请求的服务消费者NF所在的MCC。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| REQMNC | 源MNC | 可选必选说明：可选参数<br>参数含义：该参数表示Token请求的服务消费者NF所在的MNC。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| TMCC | 目标MCC | 可选必选说明：可选参数<br>参数含义：该参数表示Token请求的服务提供方NF的所在MCC。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| TMNC | 目标MNC | 可选必选说明：可选参数<br>参数含义：该参数表示Token请求的服务提供方NF的所在MNC。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFTOKEN]] · 测试Token分配（NFTOKEN）

## 使用实例

测试NF Token申请，其源NF实例标识为123e4567-e89b-12d3-a456-426655440000，目标NF实例标识为ac4567-e89b-12d3-a456-42665544，目标服务名称列表nsmf-pdusession：

```

TST NFTOKEN:NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000", TNFINSTANCEID="ac4567-e89b-12d3-a456-42665544", SCOPE="nsmf-pdusession";
%%TST NFTOKEN:NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000", TNFINSTANCEID="ac4567-e89b-12d3-a456-42665544", SCOPE="nsmf-pdusession";%%
RETCODE = 0    操作成功

结果如下
--------
Token应答结果                                                                                                                                                       

HEADER:
{"alg":"RS256","typ":"JWT"}
PAYLOAD:
{"aud":["ac4567-e89b-12d3-a456-42665544"],"exp":1571648867,"iss":"202b430d-9f66-4aa2-9420-ac9c9af33926","scope":"nsmf-pdusession","sub":"123e4567-e89b-12d3-a456-426655440000"}  
HEADER:
{"alg":"RS256","typ":"JWT"}
PAYLOAD:
{"aud":["ac4567-e89b-12d3-a456-42665544"],"exp":1571648867,"iss":"202b430d-9f66-4aa2-9420-ac9c9af33926","scope":"nsmf-pdusession","sub":"123e4567-e89b-12d3-a456-426655440000"}  

(结果个数 = 2)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/TST-NFTOKEN.md`
