---
id: UNC@20.15.2@MMLCommand@ADD NFROUTINGIND
type: MMLCommand
name: ADD NFROUTINGIND（增加选路指示器）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NFROUTINGIND
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- 号段配置管理
- 选路指示器号段管理
status: active
---

# ADD NFROUTINGIND（增加选路指示器）

## 功能

**适用NF：NRF**

该命令用于在NRF上新增选路指示器。选路指示器是SUCI组成的一部分，用于使用SUCI进行AUSF和UDM的选择。

在NRF可以为NF组配置支持的选路指示器。此配置对NF组内所有NF实例生效。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。
- NF的号段信息可以通过注册携带，也可以通过MML命令在NRF上配置，建议采用其中一种方式进行控制。如果NF注册已携带，且NRF上也进行了配置，NRF都会判断NF号段生效。

- 最多可输入10240条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFGROUPID | NF组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示支持ROUTIINGIND号段的NF组标识，该参数可以通过LST NFGROUP命令查看。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |
| ROUTINGIND | 选路指示器 | 可选必选说明：必选参数<br>参数含义：该参数用于表示支持ROUTIINGIND号段信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~4。取值范围0-9999。<br>默认值：无<br>配置原则：<br>当NF组支持ROUTINGIND为通配时，需要将ROUTINGIND设置为ALL。 |

## 操作的配置对象

- [选路指示器（NFROUTINGIND）](configobject/UNC/20.15.2/NFROUTINGIND.md)

## 使用实例

对NF组标识为nfgroup001的NF组添加一个值为1000的选路指示器：

```
ADD NFROUTINGIND: NFGROUPID="nfgroup001", ROUTINGIND="1000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加选路指示器（ADD-NFROUTINGIND）_09653295.md`
