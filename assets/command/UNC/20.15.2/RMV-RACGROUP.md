---
id: UNC@20.15.2@MMLCommand@RMV RACGROUP
type: MMLCommand
name: RMV RACGROUP（删除RAC组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RACGROUP
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
- 虚拟APN映射的RAC组
status: active
---

# RMV RACGROUP（删除RAC组）

## 功能

**适用NF：GGSN**

该命令用来删除指定的RAC组。当RAC组下绑定RAC号段时，同时可以删除该RAC组下的所有绑定的RAC号段。

## 注意事项

- 该命令执行后立即生效。

- 当RAC组被作为映射规则在ADD VIRTUALAPNRULE命令中配置的时候，如果需要删除这个RAC组，需要先使用RMV VIRTUALAPNRULE命令解除该RAC组对应的所有虚拟APN映射关系，再删除该RAC组，否则删除命令执行失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RACGROUPNAME | RAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [RAC组（RACGROUP）](configobject/UNC/20.15.2/RACGROUP.md)

## 使用实例

假设运营商需要去删除一个本地已经配置的“RAC组名”为“beijing”的RAC组：

```
RMV RACGROUP:RACGROUPNAME="beijing";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除RAC组（RMV-RACGROUP）_09654439.md`
