---
id: UNC@20.15.2@MMLCommand@RMV ADDRPOOL
type: MMLCommand
name: RMV ADDRPOOL（删除地址池）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ADDRPOOL
command_category: 配置类
applicable_nf:
- GGSN
- SMF
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址池管理
status: active
---

# RMV ADDRPOOL（删除地址池）

## 功能

**适用NF：GGSN、SMF、PGW-C**

- 该命令在某一地址池不再使用时，可以用来删掉该地址池。
- 删除地址池同时删除该地址池下的地址段和Agent IP。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [地址池（ADDRPOOL）](configobject/UNC/20.15.2/ADDRPOOL.md)

## 使用实例

假设运营商不再使用“pool1”地址池，则需要删除一个本地IPv4地址池“pool1”：

```
RMV ADDRPOOL: POOLNAME="pool1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除地址池（RMV-ADDRPOOL）_09654433.md`
