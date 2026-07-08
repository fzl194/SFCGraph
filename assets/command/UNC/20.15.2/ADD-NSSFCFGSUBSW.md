---
id: UNC@20.15.2@MMLCommand@ADD NSSFCFGSUBSW
type: MMLCommand
name: ADD NSSFCFGSUBSW（增加按签约NSSAI分配Configed NSSAI的PLMN级别开关）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NSSFCFGSUBSW
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF功能开关配置
status: active
---

# ADD NSSFCFGSUBSW（增加按签约NSSAI分配Configed NSSAI的PLMN级别开关）

## 功能

**适用NF：NSSF**

该命令用于配置按签约NSSAI生成configuredNssai信元的PLMN级别开关，控制特定PLMN内NSSF在切片选择流程中configuredNssai信元的生成逻辑。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入128条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于描述移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位十进制数。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于描述移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2位或者3位十进制数。<br>默认值：无<br>配置原则：无 |
| CFGWITHSUBSW | 按签约NSSAI分配configuredNssai开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NSSF在处理切片选择请求时，响应消息中configuredNssai信元是否直接使用UE签约NSSAI生成。开关打开，configuredNssai信元为UE签约NSSAI；开关关闭，configuredNssai信元为PLMN支持NSSAI和UE签约NSSAI的交集。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [按签约NSSAI分配Configed NSSAI的PLMN级别开关（NSSFCFGSUBSW）](configobject/UNC/20.15.2/NSSFCFGSUBSW.md)

## 使用实例

假如运营商希望增加一条移动国家码为245、移动网号为38、按签约NSSAI分配configuredNssai开关为打开的记录，执行以下命令。

```
ADD NSSFCFGSUBSW: MCC="245", MNC="38", CFGWITHSUBSW=FUNC_ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加按签约NSSAI分配Configed-NSSAI的PLMN级别开关（ADD-NSSFCFGSUBSW）_44581263.md`
