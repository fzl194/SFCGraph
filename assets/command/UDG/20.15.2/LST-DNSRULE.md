---
id: UDG@20.15.2@MMLCommand@LST DNSRULE
type: MMLCommand
name: LST DNSRULE（显示DNS规则）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DNSRULE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则管理
- DNS规则
status: active
---

# LST DNSRULE（显示DNS规则）

## 功能

**适用NF：PGW-U、UPF**

该命令用于回显DNS规则。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPLICATIONID | 应用标识 | 可选必选说明：可选参数<br>参数含义：该参数用于配置DNS列表所属的应用标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：该参数用于和SMF下发的PDR中携带的Application ID进行匹配。 |
| DNSRULENAME | DNS规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置DNS规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |
| DOMAIN | 域名 | 可选必选说明：可选参数<br>参数含义：该参数用于设置DNS规则的服务器域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DNSRULE]] · DNS规则（DNSRULE）

## 使用实例

在需要查看轻量DNS规则时，执行该命令查看现有规则：

```
LST DNSRULE: APPLICATIONID="app1", DNSRULENAME="rule1";
```

```

RETCODE = 0  操作成功

DNS域名列表
-----------
DNS规则名称  =  rule1
   应用标识  =  app1
       域名  =  test
 IP地址类型  =  IPV4
   IPv4地址  =  10.0.0.0
    DNS TTL  =  86400
   IPv6地址  =  ::
 配置域名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-DNSRULE.md`
