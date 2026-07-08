---
id: UNC@20.15.2@MMLCommand@RMV RACID
type: MMLCommand
name: RMV RACID（删除RAC组内绑定的RAC号段）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RACID
command_category: 配置类
applicable_nf:
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 虚拟APN映射管理
- 基于RAC位置的虚拟APN映射管理
- RAC组的RAC段
status: active
---

# RMV RACID（删除RAC组内绑定的RAC号段）

## 功能

**适用NF：GGSN**

该命令用来删除RAC组内绑定的RAC号段。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RACSECNUM | RAC段编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2047。<br>默认值：无<br>配置原则：无 |
| RACGROUPNAME | RAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该RACGROUPNAME必须已经由ADD RACGROUP配置过。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RACID]] · RAC组内绑定的RAC号段（RACID）

## 使用实例

假设运营商需要删除指定RAC组绑定的某个RAC号段，“RAC组名”为“beijing”，“RAC号段”为2，执行该命令：

```
RMV RACID:RACGROUPNAME="beijing",RACSECNUM=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除RAC组内绑定的RAC号段（RMV-RACID）_09651581.md`
