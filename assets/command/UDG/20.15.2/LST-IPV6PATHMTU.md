---
id: UDG@20.15.2@MMLCommand@LST IPV6PATHMTU
type: MMLCommand
name: LST IPV6PATHMTU（查询IPv6 Path MTU配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPV6PATHMTU
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 Path MTU
status: active
---

# LST IPV6PATHMTU（查询IPv6 Path MTU配置）

## 功能

该命令用于查询IPv6路径MTU配置。

若不指定VRFNAME时，则查询所有IPv6路径MTU信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：公网需要输入_public_，默认查询所有VPN。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPV6PATHMTU]] · IPv6 Path MTU配置（IPV6PATHMTU）

## 使用实例

查询IPv6 Path MTU配置：

```
LST IPV6PATHMTU:VRFNAME="vpn1";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
         IPv6地址  =  2001:db8::11
          VPN名称  =  vpn1
路径MTU值（byte）  =  1500
(返回结果 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IPV6PATHMTU.md`
