---
id: UNC@20.15.2@MMLCommand@ADD RACGROUP
type: MMLCommand
name: ADD RACGROUP（增加RAC组）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD RACGROUP（增加RAC组）

## 功能

**适用NF：GGSN**

该命令用来添加RAC组。当需要在指定RAC组内绑定某个RAC号段时，使用该命令添加RAC组。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入256条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RACGROUPNAME | RAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [RAC组（RACGROUP）](configobject/UNC/20.15.2/RACGROUP.md)

## 使用实例

假设运营商需要去添加一个新的RAC组“beijing”，用于RAC号段的绑定：

```
ADD RACGROUP:RACGROUPNAME="beijing";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加RAC组（ADD-RACGROUP）_09652702.md`
