---
id: UDG@20.15.2@MMLCommand@ADD TETHERINGTTL
type: MMLCommand
name: ADD TETHERINGTTL（配置tethering的TTL值）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: TETHERINGTTL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 255
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- Tethering检测
- 配置tethering的ttl值
status: active
---

# ADD TETHERINGTTL（配置tethering的TTL值）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置判断tethering的TTL值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为255。
- 如果配置了该命令，则软参BIT633、BIT634、BYTE621不再生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TTLVALUE | Tethering TTL值 | 可选必选说明：必选参数<br>参数含义：该参数用于设置判断tethering的TTL值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [tethering的TTL值（TETHERINGTTL）](configobject/UDG/20.15.2/TETHERINGTTL.md)

## 使用实例

配置判断tethering的TTL值：

```
ADD TETHERINGTTL: TTLVALUE=56;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/配置tethering的TTL值（ADD-TETHERINGTTL）_96925966.md`
