---
id: UDG@20.15.2@MMLCommand@RMV UPDRA
type: MMLCommand
name: RMV UPDRA（删除DRA）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UPDRA
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- Diameter管理
- DRA管理
- DRA信息
status: active
---

# RMV UPDRA（删除DRA）

## 功能

**适用NF：UPF**

![](删除DRA（RMV UPDRA）_45432704.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除对端信息可能导致Diameter链路中断，进而影响用户使用业务，比如用户被去活等。

此命令用于删除DRA的基本信息，删除特定的DRA。

## 注意事项

- 该命令执行后立即生效。
- 如果DRA主机名称被绑定在Diameter链路组下，则同时删除Diameter链路组。如果Diameter链路组被Diameter链路组本端接口引用，则同时删除Diameter链路组本端接口。
- 删除DRA的同时删除该DRA主机名对应的地址信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DRA的主机名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT2670控制是否区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DRA（UPDRA）](configobject/UDG/20.15.2/UPDRA.md)

## 使用实例

不再使用DRA实例dra1，则使用该命令删除DRA实例：

```
RMV UPDRA:HOSTNAME="dra1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除DRA（RMV-UPDRA）_45432704.md`
