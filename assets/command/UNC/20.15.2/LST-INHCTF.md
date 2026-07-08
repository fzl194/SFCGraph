---
id: UNC@20.15.2@MMLCommand@LST INHCTF
type: MMLCommand
name: LST INHCTF（查询禁止访问NCG的CTF实例）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: INHCTF
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 禁止访问NCG的CTF实例
status: active
---

# LST INHCTF（查询禁止访问NCG的CTF实例）

## 功能

**适用NF：NCG**

该命令用于查询禁止访问NCG的CTF实例。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数表示指定禁止访问NCG的CTF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。<br>默认值：无<br>配置原则：无 |
| IPADDRESSTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CTF的IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4地址）<br>- IPV6（IPv6地址）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPv4地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定IPv4类型地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>IPv4地址和IPv6地址至少配置一个。 |
| IPV6ADDRESS | IPv6地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定IPv6类型地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv4地址和IPv6地址至少配置一个。 |
| CHRSP | 计费响应 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接收被禁止CTF的计费请求消息时，NCG如何响应。<br>数据来源：全网规划<br>取值范围：<br>- “TooManyRequest_429（请求过多）”：NCG收到被禁止的CTF的计费请求后直接回复响应消息，错误码为429。<br>- “ServiceUnavailable_503（服务不可用）”：NCG收到被禁止的CTF的计费请求后直接回复响应消息，错误码为503。<br>- “NoResponse（无响应）”：NCG收到被禁止的CTF的计费请求后直接将消息丢弃。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@INHCTF]] · 禁止访问NCG的CTF实例（INHCTF）

## 使用实例

查询所有禁止访问NCG的CTF实例。

```
LST INHCTF:;
%%LST INHCTF:;%%
RETCODE = 0  操作成功

结果如下
------------------------
   NF实例标识  =  nfinstanceid001
   IP地址类型  =  IPv4地址
     IPv4地址  =  192.168.100.1
     IPv6地址  =  ::
     计费响应  =  请求过多
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-INHCTF.md`
