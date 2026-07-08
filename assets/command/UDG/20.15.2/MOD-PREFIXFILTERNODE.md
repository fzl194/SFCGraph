---
id: UDG@20.15.2@MMLCommand@MOD PREFIXFILTERNODE
type: MMLCommand
name: MOD PREFIXFILTERNODE（修改IPv4地址前缀列表过滤器节点）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: PREFIXFILTERNODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- IP前缀列表
status: active
---

# MOD PREFIXFILTERNODE（修改IPv4地址前缀列表过滤器节点）

## 功能

该命令用于修改前缀过滤器相关属性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | IP前缀列表名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP前缀列表名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无<br>配置原则：不支持输入空格。 |
| NODESEQUENCE | IP前缀列表节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP前缀列表节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| MATCHMODE | IP前缀列表匹配模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP前缀列表匹配模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- permit：允许。<br>- deny：拒绝。<br>默认值：无<br>配置原则：如果为permit则通过前缀过滤器为允许，否则为不允许。 |
| ADDRESS | IP地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：IPv4地址。 |
| MASKLENGTH | 掩码长度 | 可选必选说明：必选参数<br>参数含义：该参数用于指定掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无 |
| GREATEREQUAL | 大于或等于 | 可选必选说明：可选参数<br>参数含义：该参数用于指定最小掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无<br>配置原则：<br>- 长度范围是可以表达为MASKLENGTH <= GREATEREQUAL <= LESSEQUAL <= 32。<br>- 如果只指定了GREATEREQUAL，前缀范围为[GREATEREQUAL，32]。<br>- 当只指定LESSEQUAL时，前缀范围为[MASKLENGTH，LESSEQUAL]。 |
| LESSEQUAL | 小于或等于 | 可选必选说明：可选参数<br>参数含义：该参数用于指定最大掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无<br>配置原则：<br>- 长度范围是可以表达为MASKLENGTH <= GREATEREQUAL <= LESSEQUAL <= 32。<br>- 如果只指定了LESSEQUAL，前缀范围为[MASKLENGTH，LESSEQUAL]。<br>- 当只指定GREATEREQUAL时，前缀范围为[GREATEREQUAL，32]。 |
| MATCHNETWORK | 是否匹配网络 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否匹配IP地址前缀为0的网段路由。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：MATCHNETWORK参数只有在Ipv4地址为0.0.0.0时才可以配置，主要是用来指定是否匹配网段路由。 |

## 操作的配置对象

- [IPv4地址前缀列表过滤器节点（PREFIXFILTERNODE）](configobject/UDG/20.15.2/PREFIXFILTERNODE.md)

## 使用实例

修改前缀过滤器，前缀过滤器名字为a，节点为1的过滤地址是10.1.1.1：

```
MOD PREFIXFILTERNODE:NAME="a",NODESEQUENCE=1,MATCHMODE=permit,ADDRESS="10.1.1.1", MASKLENGTH=32;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IPv4地址前缀列表过滤器节点（MOD-PREFIXFILTERNODE）_50280582.md`
