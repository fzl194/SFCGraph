---
id: UNC@20.15.2@MMLCommand@MOD GLBPCRFGROUP
type: MMLCommand
name: MOD GLBPCRFGROUP（修改全局PCRF组绑定关系）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: GLBPCRFGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- 全局PCRF组
status: active
---

# MOD GLBPCRFGROUP（修改全局PCRF组绑定关系）

## 功能

**适用NF：PGW-C、GGSN**

此命令用来修改绑定PCRF分组和指定号段的优先级。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 如果不输入PRIORITY，则修改命令不做任何处理。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置绑定的IMSIMSISDN号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：该参数使用ADD IMSIMSISDNSEG命令配置生成。 |
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置绑定的PCRF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。<br>默认值：无<br>配置原则：该参数使用ADD PCRFGROUP命令配置生成。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于设置优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：将PCRF组和号段绑定时，必须指定该绑定关系的优先级，优先级越小，级别越高。根据绑定关系进行PCRF组的选择时，如果能够匹配到两个PCRF组，则根据绑定关系的优先级进行下一步选择。 |
| DESCRIPTION | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于配置号段绑定PCRF组的描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBPCRFGROUP]] · 全局PCRF组绑定关系（GLBPCRFGROUP）

## 使用实例

修改GLBPCRFGROUP：IMSIMSISDNSEG为“ims”，PCRFGRPNAME为“pcr”：

```
MOD GLBPCRFGROUP:IMSIMSISDNSEG="ims",PCRFGRPNAME="pcr",PRIORITY=444;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改全局PCRF组绑定关系（MOD-GLBPCRFGROUP）_09897117.md`
