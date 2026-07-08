---
id: UNC@20.15.2@MMLCommand@RMV PERFREGION
type: MMLCommand
name: RMV PERFREGION（删除区域性能统计对象）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PERFREGION
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# RMV PERFREGION（删除区域性能统计对象）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用来删除指定的区域性能统计对象。

## 注意事项

- 该命令执行后立即生效。

- RMV PERFREGION时同时删除的配置清单：PERFREGAPN，PERFREGTAC。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REGNAME | 区域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定区域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [区域性能统计对象（PERFREGION）](configobject/UNC/20.15.2/PERFREGION.md)

## 使用实例

当运营商需要删除名为“beijing”的区域性能统计对象时，执行如下命令：

```
RMV PERFREGION: REGNAME="beijing";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除区域性能统计对象（RMV-PERFREGION）_44530771.md`
