---
id: UDG@20.15.2@MMLCommand@ADD INSAPROTOCOL
type: MMLCommand
name: ADD INSAPROTOCOL（增加黑白名单协议配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: INSAPROTOCOL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 8192
category_path:
- 用户面服务管理
- 业务匹配策略
- 智能SA管理
- 协议类型配置
status: active
---

# ADD INSAPROTOCOL（增加黑白名单协议配置）

## 功能

**适用NF：PGW-U、UPF**

增加黑白名单协议配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8192。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTTYPE | 协议类型 | 可选必选说明：必选参数<br>参数含义：该参数用来表示配置协议类型。<br>数据来源：本端规划<br>取值范围：<br>- BLACK：黑名单协议。<br>- ENHANCE：待增强协议。<br>默认值：无<br>配置原则：无 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：必选参数<br>参数含义：协议组包含的协议的名字。<br>数据来源：本端规划<br>取值范围：1、字符串类型，输入长度范围为1～31; 2、不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的子协议，可以通过工程命令smctrldsp protocol-list sub-protocol查询。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/INSAPROTOCOL]] · 黑白名单协议配置（INSAPROTOCOL）

## 使用实例

增加一个http待增强协议：

```
ADD INSAPROTOCOL:PROTTYPE=ENHANCE, PROTOCOLNAME="http";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加黑白名单协议配置（ADD-INSAPROTOCOL）_56405096.md`
