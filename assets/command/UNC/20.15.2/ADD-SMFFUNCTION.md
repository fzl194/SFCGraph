---
id: UNC@20.15.2@MMLCommand@ADD SMFFUNCTION
type: MMLCommand
name: ADD SMFFUNCTION（添加SMF功能实例信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SMFFUNCTION
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# ADD SMFFUNCTION（添加SMF功能实例信息）

## 功能

**适用NF：SMF**

该命令用于添加SMF功能实例信息。

## 注意事项

- 该命令执行后立即生效。

- 该命令当前版本仅支持配置1条记录，否则会影响北向功能。

- 最多可输入100条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | NF实例号 | 可选必选说明：必选参数<br>参数含义：NF实例号。用于SMF与北向网管对接使用，通过NFInstance ID可以实现与北向网管上与网元的话统、告警信息的关联。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：<br>该参数需要根据北向网管的要求来填写，例如，填写为在MANO上创建VNF时的InstanceID。 |
| NAME | NF功能实例描述 | 可选必选说明：可选参数<br>参数含义：NF功能实例描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |
| ADMINSTATE | 管理状态 | 可选必选说明：可选参数<br>参数含义：管理状态。<br>数据来源：本端规划<br>取值范围：<br>- Locked（锁定）<br>- Unlocked（未锁定）<br>- ShuttingDown（关机）<br>默认值：Unlocked<br>配置原则：无 |
| OPERATIONSTATE | 运行状态 | 可选必选说明：可选参数<br>参数含义：运行状态。<br>数据来源：本端规划<br>取值范围：<br>- Enabled（运行）<br>- Disabled（不运行）<br>默认值：Enabled<br>配置原则：无 |
| FQDN | FQDN | 可选必选说明：可选参数<br>参数含义：FQDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，大小写不敏感，FQDN不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |
| MAXPDUSESSIONS | 最大PDU会话数 | 可选必选说明：可选参数<br>参数含义：最大PDU Session数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| MAXQFI | 最大QFI数 | 可选必选说明：可选参数<br>参数含义：最大QFI数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SMF功能实例信息（SMFFUNCTION）](configobject/UNC/20.15.2/SMFFUNCTION.md)

## 使用实例

新增SMF功能实体号为Instanceid01,SMF功能实体描述为nfdescription01,管理状态为Locked,运行状态为Enabled,FQDN为fqdn01的SMF功能实例信息：

```
ADD SMFFUNCTION: INSTANCEID="Instanceid01", NAME="nfdescription01", ADMINSTATE=Locked, OPERATIONSTATE=Enabled, FQDN="fqdn01";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/添加SMF功能实例信息（ADD-SMFFUNCTION）_09653246.md`
