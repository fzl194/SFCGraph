---
id: UNC@20.15.2@MMLCommand@ADD SELECTCCTBYCC
type: MMLCommand
name: ADD SELECTCCTBYCC（增加基于CC配置融合计费模板处理）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SELECTCCTBYCC
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 融合计费模板绑定
status: active
---

# ADD SELECTCCTBYCC（增加基于CC配置融合计费模板处理）

## 功能

**适用NF：PGW-C、SMF、SGW-C**

该命令用于增加基于CC配置融合计费模板处理。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入101条记录。
- 不允许配置的CCVALUE和掩码CCMASK取与后的值不等于CCVALUE。
- 不允许配置的CCVALUE和掩码CCMASK取与后的值，与当前已有配置的CCVALUE和对应的CCMASK取与后的值相等。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTYPE | CC类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定计费属性。<br>数据来源：全网规划<br>取值范围：<br>- DEFAULT（未指定Charge Characteristic的值）<br>- VALUE（指定Charge Characteristic的值）<br>默认值：无<br>配置原则：无 |
| CCVALUE | Charge Characteristic值 | 可选必选说明：该参数在"CCTYPE"配置为"VALUE"时为条件必选参数。<br>参数含义：该参数用于指定特殊的CC值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| MASK | Charge Characteristic特定值掩码 | 可选必选说明：该参数在"CCTYPE"配置为"VALUE"时为条件可选参数。<br>参数含义：该参数用于指定CC的掩码，通过配置掩码可以实现全匹配CC值，还是只匹配部分bit位。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0001~0xFFFF。配置的计费属性掩码计费属性值参数做与运算后，需要等于计费属性值，否则配置失败。<br>默认值：无<br>配置原则：无 |
| PRIORITY | Charge Characteristic优先级 | 可选必选说明：该参数在"CCTYPE"配置为"VALUE"时为条件可选参数。<br>参数含义：该参数用于设置优先级。配置mask时必须指定优先级，不允许指定相同的优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：<br>不配置此参数时值默认为0。 |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：可选参数<br>参数含义：该命令用于指定融合计费模板（Converged Charging Template）名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD CCT**](../融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)<br>命令配置生成。 |
| SERVINGCCT | I-SMF/SGW使用的融合计费模板名称 | 可选必选说明：可选参数<br>参数含义：该命令用于指定I-SMF/SGW使用的融合计费模板（Converged Charging Template）名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD CCT**](../融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)<br>命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SELECTCCTBYCC]] · 基于CC配置融合计费模板处理（SELECTCCTBYCC）

## 使用实例

增加基于CC值为1234配置融合计费模板：

```
ADD SELECTCCTBYCC: CCTYPE=VALUE, CCVALUE="1234", CCTMPLTNAME="test";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SELECTCCTBYCC.md`
