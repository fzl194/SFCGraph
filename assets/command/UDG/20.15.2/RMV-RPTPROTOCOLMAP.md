---
id: UDG@20.15.2@MMLCommand@RMV RPTPROTOCOLMAP
type: MMLCommand
name: RMV RPTPROTOCOLMAP（删除业务报表承载协议映射配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RPTPROTOCOLMAP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务报表管理
- 报表本地策略管理
- 业务报表承载协议映射
status: active
---

# RMV RPTPROTOCOLMAP（删除业务报表承载协议映射配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除业务报表承载协议映射配置。当运营商希望删除业务报表承载协议映射配置，则配置该命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLLEVEL | 协议等级 | 可选必选说明：必选参数<br>参数含义：该参数用于指示配置的协议组、协议级别。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PROTOCOLGROUP：协议组级别。<br>- PROTOCOL：协议级别。<br>默认值：无<br>配置原则：无 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOL”时为必选参数。<br>参数含义：该参数用于设置协议名称。数据源为UPF支持识别的所有类型的协议、子协议。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOLGROUP”时为必选参数。<br>参数含义：该参数用于设置协议组名称。数据源为UPF支持识别的所有默认协议组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [业务报表映射承载协议分类配置（RPTPROTOCOLMAP）](configobject/UDG/20.15.2/RPTPROTOCOLMAP.md)

## 使用实例

假如运营商需要删除p2p协议组业务报表承载协议映射配置：

```
RMV RPTPROTOCOLMAP: PROTOCOLLEVEL=PROTOCOLGROUP, PROTGROUPNAME="p2p";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除业务报表承载协议映射配置（RMV-RPTPROTOCOLMAP）_27889297.md`
