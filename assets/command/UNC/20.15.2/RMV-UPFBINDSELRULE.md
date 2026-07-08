---
id: UNC@20.15.2@MMLCommand@RMV UPFBINDSELRULE
type: MMLCommand
name: RMV UPFBINDSELRULE（删除UPF和规则的绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UPFBINDSELRULE
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- SGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF和规则的绑定关系
status: active
---

# RMV UPFBINDSELRULE（删除UPF和规则的绑定关系）

## 功能

**适用NF：SMF、PGW-C、SGW-C**

该命令用于删除UPF和规则的绑定关系。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF和规则的绑定关系的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4999。<br>默认值：无<br>配置原则：<br>该参数取值不能重复，建议从0开始顺序取值。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPFBINDSELRULE]] · UPF和规则的绑定关系（UPFBINDSELRULE）

## 使用实例

删除UPF和规则的绑定关系，UPF实例名称为"UPF1"，规则名称为"rulename1"：

```
RMV UPFBINDSELRULE: INDEX=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UPF和规则的绑定关系（RMV-UPFBINDSELRULE）_75823004.md`
