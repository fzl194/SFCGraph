---
id: UNC@20.15.2@MMLCommand@RMV PERFREGTAC
type: MMLCommand
name: RMV PERFREGTAC（删除区域性能统计对象和TAC段的绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PERFREGTAC
command_category: 配置类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# RMV PERFREGTAC（删除区域性能统计对象和TAC段的绑定关系）

## 功能

**适用NF：PGW-C、SGW-C**

该命令用于删除区域性能统计对象和TAC段的绑定关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REGNAME | 区域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定与TAC段绑定的区域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD PERFREGION命令配置生成。 |
| TACSEGNAME | TAC段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定与区域绑定的TAC段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD PERFS1TACSEG命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFREGTAC]] · 区域性能统计对象和TAC段的绑定关系（PERFREGTAC）

## 使用实例

当运营商需要删除一个区域性能统计对象绑定的TAC号段时，执行如下命令：

```
RMV PERFREGTAC: REGNAME="beijing", TACSEGNAME="changping";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PERFREGTAC.md`
