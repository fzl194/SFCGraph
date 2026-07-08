---
id: UDG@20.15.2@MMLCommand@RMV TLSPSK
type: MMLCommand
name: RMV TLSPSK（删除预共享密钥）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: TLSPSK
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP TLS预共享密钥管理
status: active
---

# RMV TLSPSK（删除预共享密钥）

## 功能

该命令用于删除预共享密钥。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PSKIDX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TLS预共享密钥的记录索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TLSPSK]] · 预共享密钥（TLSPSK）

## 使用实例

若需要删除索引为1的预共享密钥，可执行如下命令：

```
RMV TLSPSK: PSKIDX=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-TLSPSK.md`
