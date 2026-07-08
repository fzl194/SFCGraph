---
id: UDG@20.15.2@MMLCommand@LST IFIPV6NDRAPREFIX
type: MMLCommand
name: LST IFIPV6NDRAPREFIX（查询IPv6 RA通告前缀）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IFIPV6NDRAPREFIX
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- IPv6地址前缀通告
status: active
---

# LST IFIPV6NDRAPREFIX（查询IPv6 RA通告前缀）

## 功能

该命令用于查询接口IPv6 RA通告前缀。

## 注意事项

- 该命令执行后立即生效。
- 指定的前缀不能为链路本地地址（fe80::）、组播地址（ff00::）以及其他接口已经使用的前缀（包括接口地址前缀和RA消息携带的前缀）。
- 该命令可以在VNRS_VNFC的Ethernet接口，Ethernet子接口以及Tunnel口上配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPV6前缀接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IFIPV6NDRAPREFIX]] · IPv6 RA通告前缀（IFIPV6NDRAPREFIX）

## 使用实例

查询接口IPv6 RA通告前缀：

```
LST IFIPV6NDRAPREFIX:IFNAME="ethernet64/0/3";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
            接口名  =  Ethernet64/0/3
      IPv6前缀地址  =  2001:DB8::
      IPv6前缀长度  =  64
   优先生存期（s）  =  10
   有效生存期（s）  =  10
无状态地址配置标志  =  不使能
      本地链路标志  =  不使能
(结果个数 = 1)
---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IFIPV6NDRAPREFIX.md`
