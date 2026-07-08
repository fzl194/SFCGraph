---
id: UDG@20.15.2@MMLCommand@RMV NGBINDDFSRPAIR
type: MMLCommand
name: RMV NGBINDDFSRPAIR（删除5G LAN实例绑定双发选收结对配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: NGBINDDFSRPAIR
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN双发选收配置
- 5G LAN实例绑定双发选收结对
status: active
---

# RMV NGBINDDFSRPAIR（删除5G LAN实例绑定双发选收结对配置）

## 功能

**适用NF：UPF**

该命令用于删除双发选收结对与5G LAN会话实例绑定关系。

## 注意事项

- 该命令执行后立即生效。
- 双发选收结对已绑定该5G LAN会话实例。
- 双发选收结对未加入到静态组播组中。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为18～37。<br>默认值：无<br>配置原则：无 |
| DFSRPAIRID | 双发选收结对ID | 可选必选说明：可选参数<br>参数含义：该参数用于配置双发选收结对ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1-2048。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G LAN实例绑定双发选收结对配置（NGBINDDFSRPAIR）](configobject/UDG/20.15.2/NGBINDDFSRPAIR.md)

## 使用实例

把双发选收结对1与5G LAN会话实例a0000001-460-01-01解绑：

```
RMV NGBINDDFSRPAIR: VNINSTANCE="a0000001-460-01-01", DFSRPAIRID=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除5G-LAN实例绑定双发选收结对配置（RMV-NGBINDDFSRPAIR）_22918680.md`
