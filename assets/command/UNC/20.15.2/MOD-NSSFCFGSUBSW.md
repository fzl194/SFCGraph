---
id: UNC@20.15.2@MMLCommand@MOD NSSFCFGSUBSW
type: MMLCommand
name: MOD NSSFCFGSUBSW（修改按签约NSSAI分配Configed NSSAI的PLMN级别开关）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD NSSFCFGSUBSW（修改按签约NSSAI分配Configed NSSAI的PLMN级别开关）

## 功能

**适用NF：NSSF**

该命令用于修改按签约NSSAI生成configuredNssai信元的PLMN级别开关。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于描述移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位十进制数。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于描述移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2位或者3位十进制数。<br>默认值：无<br>配置原则：无 |
| CFGWITHSUBSW | 按签约NSSAI分配configuredNssai开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NSSF在处理切片选择请求时，响应消息中configuredNssai信元是否直接使用UE签约NSSAI生成。开关打开，configuredNssai信元为UE签约NSSAI；开关关闭，configuredNssai信元为PLMN支持NSSAI和UE签约NSSAI的交集。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFCFGSUBSW]] · 按签约NSSAI分配Configed NSSAI的PLMN级别开关（NSSFCFGSUBSW）

## 使用实例

假如运营商希望修改一条移动国家码为248、移动网号为37、按签约NSSAI分配configuredNssai开关为关闭的记录，执行以下命令。

```
MOD NSSFCFGSUBSW: MCC="248", MNC="37", CFGWITHSUBSW=FUNC_ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改按签约NSSAI分配Configed-NSSAI的PLMN级别开关（MOD-NSSFCFGSUBSW）_98061326.md`
