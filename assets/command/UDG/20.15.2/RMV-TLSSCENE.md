---
id: UDG@20.15.2@MMLCommand@RMV TLSSCENE
type: MMLCommand
name: RMV TLSSCENE（删除TLS证书场景）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: TLSSCENE
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP TLS证书场景管理
status: active
---

# RMV TLSSCENE（删除TLS证书场景）

## 功能

当需要更换或删除TLS证书场景时，使用该命令删除TLS证书场景配置。

> **说明**
> - 该命令执行后立即生效。
>
> - 删除TLS证书场景前，需要先删除对应的TLSPARA。
> - 删除TLS证书场景后，该场景与证书的关联关系也会删除，如果再次添加该场景，则需要重新关联证书。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定证书场景的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~254。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TLSSCENE]] · TLS证书场景（TLSSCENE）

## 使用实例

若运营商想删除索引为1的TLS证书场景配置，可以用如下命令：

```
RMV TLSSCENE:INDEX=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除TLS证书场景（RMV-TLSSCENE）_83813642.md`
