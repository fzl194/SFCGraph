---
id: UNC@20.15.2@MMLCommand@LST IFIPV6ADDRPOLICY
type: MMLCommand
name: LST IFIPV6ADDRPOLICY（查询IPv6地址策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IFIPV6ADDRPOLICY
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- IPv6地址策略
status: active
---

# LST IFIPV6ADDRPOLICY（查询IPv6地址策略）

## 功能

该命令用于查询IPv6地址策略。

## 注意事项

- 该命令执行后立即生效。
- 如果用户没有配置任何地址选择策略表项，执行该命令时系统只显示缺省策略表项，即显示::1、::、2002::、FC00::、::FFFF:0.0.0.0地址前缀的选择策略表项信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNNAME | VPN实例名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6地址策略的VPN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IFIPV6ADDRPOLICY]] · IPv6地址策略（IFIPV6ADDRPOLICY）

## 使用实例

显示IPv6地址策略：

```
LST IFIPV6ADDRPOLICY:;
```

```
RETCODE = 0  操作成功

结果如下
-------------------------
VPN实例名称 IPv6地址               IPv6地址前缀长度     目的地址优先级                  源地址优先级

_public_    ::                     0                    40                               1
_public_    ::1                    128                  50                               0
_public_    ::FFFF:0.0.0.0         96                   10                               4
_public_    2002::                 16                   30                               2
_public_    FC00::                 7                    20                               3
(结果个数 = 5)
---   END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IFIPV6ADDRPOLICY.md`
