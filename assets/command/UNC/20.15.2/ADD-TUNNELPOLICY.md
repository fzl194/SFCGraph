---
id: UNC@20.15.2@MMLCommand@ADD TUNNELPOLICY
type: MMLCommand
name: ADD TUNNELPOLICY（增加隧道策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TUNNELPOLICY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- VPN隧道管理
- 隧道策略
status: active
---

# ADD TUNNELPOLICY（增加隧道策略）

## 功能

该命令用于增加隧道策略。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNLPOLICYNAME | 隧道策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于表示隧道策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～39。<br>默认值：无 |
| DESCRIPTION | 隧道策略描述 | 可选必选说明：可选参数<br>参数含义：该参数用于表示隧道策略描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～80。<br>默认值：无 |
| TNLPOLICYTYPE | 隧道策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示隧道策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- invalid：无效类型的隧道策略。<br>- tnlSelectSeq：隧道选择序列。<br>默认值：无 |
| LOADBALANCENUM | 负载均衡数 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TNLPOLICYTYPE”配置为“tnlSelectSeq”时为必选参数。<br>参数含义：该参数用于表示负载均衡数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～64。<br>默认值：无 |
| SELTNLTYPE1 | 第一优选隧道类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TNLPOLICYTYPE”配置为“tnlSelectSeq”时为必选参数。<br>参数含义：该参数用于表示选择隧道类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- lsp：LSP。<br>- gre：GRE。<br>默认值：无 |
| SELTNLTYPE2 | 第二优选隧道类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TNLPOLICYTYPE”配置为“tnlSelectSeq”时为可选参数。<br>参数含义：该参数用于表示选择隧道类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- invalid：INVALID。<br>- lsp：LSP。<br>- gre：GRE。<br>默认值：invalid |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TUNNELPOLICY]] · 隧道策略（TUNNELPOLICY）

## 使用实例

增加隧道策略：

```
ADD TUNNELPOLICY:TNLPOLICYNAME="tp",TNLPOLICYTYPE=tnlSelectSeq,LOADBALANCENUM=50,SELTNLTYPE1=gre,SELTNLTYPE2=lsp;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-TUNNELPOLICY.md`
