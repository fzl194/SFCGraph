---
id: UNC@20.15.2@MMLCommand@RMV HTTPVPNMAP
type: MMLCommand
name: RMV HTTPVPNMAP（删除HTTP VPN映射关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: HTTPVPNMAP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP VPN映射管理
status: active
---

# RMV HTTPVPNMAP（删除HTTP VPN映射关系）

## 功能

该命令用于删除HTTP对端地址与本端VPN的映射关系。

## 注意事项

- 该命令执行后立即生效。

- 若删除的HTTP VPN映射关系已经被客户端HTTP实体引用，且该HTTP实体所在的HTTP实体组存在使用其他VPN的客户端HTTP实体，则不允许删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP VPN映射的索引信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~512。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [HTTP VPN映射关系（HTTPVPNMAP）](configobject/UNC/20.15.2/HTTPVPNMAP.md)

## 使用实例

若运营商要删除索引为1的HTTP VPN映射关系，可以用如下命令

```
RMV HTTPVPNMAP: INDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除HTTP-VPN映射关系（RMV-HTTPVPNMAP）_99472510.md`
