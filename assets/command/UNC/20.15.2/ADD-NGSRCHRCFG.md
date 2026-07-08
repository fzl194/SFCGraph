---
id: UNC@20.15.2@MMLCommand@ADD NGSRCHRCFG
type: MMLCommand
name: ADD NGSRCHRCFG（增加AMF小范围CHR上报规则配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NGSRCHRCFG
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- CHR管理
- NG接入小范围CHR配置
status: active
---

# ADD NGSRCHRCFG（增加AMF小范围CHR上报规则配置）

## 功能

**适用NF：AMF**

该命令用于增加AMF小范围CHR上报规则配置。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入16条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置小范围CHR的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- SPECIFIC_IMSI（指定用户IMSI）<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIC_IMSI"时为条件必选参数。<br>参数含义：该参数用于指定IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是11~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| TMPLIDX | 流程控制模板索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CHR上报流程控制模板索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：<br>TMPLIDX参数依赖于ADD NGACCCHRPRCTMPL命令的TMPLIDX参数。 |

## 操作的配置对象

- [AMF小范围CHR上报规则配置（NGSRCHRCFG）](configobject/UNC/20.15.2/NGSRCHRCFG.md)

## 使用实例

增加IMSI前缀为12303000100，流程控制模板索引为0的小范围CHR上报规则配置，执行如下命令：

```
ADD NGSRCHRCFG: SUBRANGE=SPECIFIC_IMSI, IMSIPRE="12303000100", TMPLIDX=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加AMF小范围CHR上报规则配置（ADD-NGSRCHRCFG）_13800464.md`
