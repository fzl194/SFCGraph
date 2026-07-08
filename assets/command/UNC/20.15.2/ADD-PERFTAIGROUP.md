---
id: UNC@20.15.2@MMLCommand@ADD PERFTAIGROUP
type: MMLCommand
name: ADD PERFTAIGROUP（增加TAI组性能统计对象）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD PERFTAIGROUP（增加TAI组性能统计对象）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于增加TAI组性能统计对象的配置。

## 注意事项

- 该命令执行后立即生效。

- 本命令实际允许配置的记录数同时受网管能力约束。如果有疑问，请联系华为技术支持。

- 最多可输入3000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAIGROUPNAME | TAI组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAI组的性能统计名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写，不支持空格及“\”且全局唯一。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [TAI组性能统计对象（PERFTAIGROUP）](configobject/UNC/20.15.2/PERFTAIGROUP.md)

## 使用实例

当需要添加一个组名为"huawei"的TAI组对象，执行如下命令：

```
ADD PERFTAIGROUP: TAIGROUPNAME="huawei";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加TAI组性能统计对象（ADD-PERFTAIGROUP）_17465982.md`
