---
id: UDG@20.15.2@MMLCommand@ADD RELAYRFCHKRULE
type: MMLCommand
name: ADD RELAYRFCHKRULE（增加媒体中继引用检查规则）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: RELAYRFCHKRULE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继引用检查规则
status: active
---

# ADD RELAYRFCHKRULE（增加媒体中继引用检查规则）

## 功能

**适用NF：PGW-U、UPF**

该命令用于增加媒体中继引用检查规则。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYRFCHKNAME | 媒体中继引用检查名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定媒体中继引用检查名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| CHECKMODE | 检测模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定检测模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BLACKLIST：黑名单模式。<br>- WHITELIST：白名单模式。<br>默认值：无<br>配置原则：无 |
| BLKURLLISTNAME | 黑名单URL列表名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CHECKMODE”配置为“BLACKLIST”时为必选参数。<br>参数含义：该参数用来指定黑名单URL列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| WHTURLLISTNAME | 白名单URL列表名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CHECKMODE”配置为“WHITELIST”时为必选参数。<br>参数含义：该参数用来指定白名单URL列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| NOREFERACT | 未携带Referer字段的动作 | 可选必选说明：可选参数<br>参数含义：该参数用于指定未携带Referer字段的动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DEFAULT：缺省处理动作，白名单场景按检查失败处理，执行失败动作，黑名单场景按检查通过处理，允许业务访问。<br>- SUCCESS：检查通过，允许业务访问。<br>- FAILURE：检查失败，执行失败动作。<br>默认值：DEFAULT<br>配置原则：无 |
| CHECKFAILACT | 检查失败动作 | 可选必选说明：可选参数<br>参数含义：该参数用于指定检查失败动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FORBIDDEN：拒绝。<br>- REDIRECT：重定向。<br>默认值：FORBIDDEN<br>配置原则：无 |
| IGNORESCHEME | 忽略Scheme | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启或关闭忽略Scheme开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：ENABLE<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [媒体中继引用检查规则（RELAYRFCHKRULE）](configobject/UDG/20.15.2/RELAYRFCHKRULE.md)

## 使用实例

假如需要创建一组媒体中继引用检查规则，则命令如下：

```
ADD RELAYRFCHKRULE: RELAYRFCHKNAME="test", CHECKMODE=WHITELIST, WHTURLLISTNAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加媒体中继引用检查规则（ADD-RELAYRFCHKRULE）_44232398.md`
