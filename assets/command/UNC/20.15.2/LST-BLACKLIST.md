---
id: UNC@20.15.2@MMLCommand@LST BLACKLIST
type: MMLCommand
name: LST BLACKLIST（查询黑名单地址列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BLACKLIST
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- 静态地址黑名单管理
status: active
---

# LST BLACKLIST（查询黑名单地址列表）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询符合条件的黑名单配置。

## 注意事项

- 如果没有指定黑名单名称，则显示所有的黑名单记录。
- 如果指定了黑名单名称，则显示匹配名称的黑名单配置记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 名称 | 可选必选说明：可选参数<br>参数含义：黑名单地址段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头或结尾，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BLACKLIST]] · 黑名单地址列表（BLACKLIST）

## 使用实例

查询所有静态地址黑名单：

```
LST BLACKLIST:;
RETCODE = 0  操作成功。

结果如下
--------
            名称  =  testblacklist
      IP地址类型  =  IPv4
    IPv4起始地址  =  192.168.0.1
    IPv4结束地址  =  192.168.0.255
IPv6前缀起始地址  =  ::
IPv6前缀结束地址  =  ::
         绑定VPN  =  使能
       VPN实例名  =  testvpn
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-BLACKLIST.md`
