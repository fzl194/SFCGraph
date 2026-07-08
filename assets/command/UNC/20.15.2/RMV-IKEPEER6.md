---
id: UNC@20.15.2@MMLCommand@RMV IKEPEER6
type: MMLCommand
name: RMV IKEPEER6（删除IPv6 IKE对等体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IKEPEER6
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IKE对等体IPv6
status: active
---

# RMV IKEPEER6（删除IPv6 IKE对等体）

## 功能

![](删除IPv6 IKE对等体（RMV IKEPEER6）_21521252.assets/notice_3.0-zh-cn_2.png)

删除IKE对等体，影响业务流量使用IPSEC进行加解密功能，有业务影响。

该命令用于删除IKE对等体。

## 注意事项

- 该命令执行后立即生效。

- 当IKE对等体被IPsec策略引用时，IKE对等体不能被删除。如果需要删除IKE对等体，必须先删除IKE对等体的引用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERNAME | IKE对等体名称 | 可选必选说明：必选参数<br>参数含义：对端名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IKEPEER6]] · IPv6 IKE对等体（IKEPEER6）

## 使用实例

删除名称为“peer1”的IKE对等体：

```
RMV IKEPEER6:PEERNAME="peer1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-IKEPEER6.md`
