---
id: UNC@20.15.2@MMLCommand@RMV NFROUTINGIND
type: MMLCommand
name: RMV NFROUTINGIND（删除选路指示器）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV NFROUTINGIND（删除选路指示器）

## 功能

**适用NF：NRF**

该命令用于在NRF上删除选路指示器，例如应用于UDM割接的场景，需要在NRF上将原UDM配置的选路指示器删除。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFGROUPID | NF组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示支持ROUTIINGIND号段的NF组标识，该参数可以通过LST NFGROUP命令查看。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |
| ROUTINGIND | 选路指示器 | 可选必选说明：必选参数<br>参数含义：该参数用于表示支持ROUTIINGIND号段信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~4。取值范围0-9999。<br>默认值：无<br>配置原则：<br>当NF组支持ROUTINGIND为通配时，需要将ROUTINGIND设置为ALL。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFROUTINGIND]] · 选路指示器（NFROUTINGIND）

## 使用实例

对NF组标识为nfgroup001的NF组删除值为1000的选路指示器：

```
RMV NFROUTINGIND: NFGROUPID="nfgroup001", ROUTINGIND="1000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除选路指示器（RMV-NFROUTINGIND）_09654372.md`
