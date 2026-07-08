---
id: UNC@20.15.2@MMLCommand@LST RSNRULE
type: MMLCommand
name: LST RSNRULE（查询RSN规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RSNRULE
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- 高可靠低时延传输
- 冗余PDU会话
status: active
---

# LST RSNRULE（查询RSN规则）

## 功能

**适用NF：SMF**

该命令用于查询RSN规则。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SST | 切片业务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定切片业务类型。网络切片标识（S-NSSAI）由切片业务类型（SST）和切片细分标识（SD）两部分组成，其中切片细分标识（SD）是可选的。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定切片细分标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是6。<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RSNRULE]] · RSN规则（RSNRULE）

## 使用实例

查询SST为1，SD为010101，DNN为huawei.com的RSN规则：

```
LST RSNRULE:SST=1,SD="010101",DNN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RSN规则（LST-RSNRULE）_05870169.md`
