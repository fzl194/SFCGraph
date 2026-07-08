---
id: UNC@20.15.2@MMLCommand@RMV PERFS1TACSEG
type: MMLCommand
name: RMV PERFS1TACSEG（删除S1TAC段）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PERFS1TACSEG
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

# RMV PERFS1TACSEG（删除S1TAC段）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用来删除某个S1TAC号段。

## 注意事项

- 该命令执行后立即生效。

- RMV PERFS1TACSEG时同时删除关联的PERFREGTAC配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACSEGNAME | TAC段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [S1TAC段（PERFS1TACSEG）](configobject/UNC/20.15.2/PERFS1TACSEG.md)

## 使用实例

当运营商需要删除一个TAC号段，执行如下命令：

```
RMV PERFS1TACSEG: TACSEGNAME="changping";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除S1TAC段（RMV-PERFS1TACSEG）_44530774.md`
