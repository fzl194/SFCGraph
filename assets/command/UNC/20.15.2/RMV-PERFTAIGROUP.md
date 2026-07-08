---
id: UNC@20.15.2@MMLCommand@RMV PERFTAIGROUP
type: MMLCommand
name: RMV PERFTAIGROUP（删除TAI组性能统计对象）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PERFTAIGROUP
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# RMV PERFTAIGROUP（删除TAI组性能统计对象）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于删除指定的TAI组性能统计对象。

## 注意事项

- 该命令执行后立即生效。

- 在执行本命令之前请首先通过RMV PERFTAIGROUPMEM和RMV PERFRPTRANGE删除对本命令的TAIGROUPNAME参数的引用，否则本命令执行失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAIGROUPNAME | TAI组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAI组的性能统计名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写，不支持空格及“\”且全局唯一。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFTAIGROUP]] · TAI组性能统计对象（PERFTAIGROUP）

## 使用实例

当需要删除一个组名为"huawei"的TAI组对象，执行如下命令：

```
RMV PERFTAIGROUP: TAIGROUPNAME="huawei";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除TAI组性能统计对象（RMV-PERFTAIGROUP）_17465986.md`
