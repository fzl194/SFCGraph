---
id: UNC@20.15.2@MMLCommand@ADD RSNRULE
type: MMLCommand
name: ADD RSNRULE（增加RSN规则）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: RSNRULE
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- 高可靠低时延传输
- 冗余PDU会话
status: active
---

# ADD RSNRULE（增加RSN规则）

## 功能

**适用NF：SMF**

该命令用于增加决策RSN值的规则。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SST | 切片业务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定切片业务类型。网络切片标识（S-NSSAI）由切片业务类型（SST）和切片细分标识（SD）两部分组成，其中切片细分标识（SD）是可选的。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定切片细分标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是6。<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |
| RSN | 冗余序列号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定冗余序列号。<br>数据来源：本端规划<br>取值范围：<br>- V1（主用节点）<br>- V2（辅用节点）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [RSN规则（RSNRULE）](configobject/UNC/20.15.2/RSNRULE.md)

## 使用实例

增加SST为1，SD为010101，DNN为huawei.com，RSN为V1的决策规则：

```
ADD RSNRULE:SST=1,SD="010101",DNN="huawei.com",RSN=V1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加RSN规则（ADD-RSNRULE）_05750161.md`
