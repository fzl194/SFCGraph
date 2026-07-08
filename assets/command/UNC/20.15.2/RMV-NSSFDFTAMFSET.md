---
id: UNC@20.15.2@MMLCommand@RMV NSSFDFTAMFSET
type: MMLCommand
name: RMV NSSFDFTAMFSET（删除默认AMF集所支持的S-NSSAI范围）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NSSFDFTAMFSET
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- AMF集合配置管理
status: active
---

# RMV NSSFDFTAMFSET（删除默认AMF集所支持的S-NSSAI范围）

## 功能

**适用NF：NSSF**

该命令用于删除默认AMF集所支持的S-NSSAI范围。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NSSF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于描述命令的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFDFTAMFSET]] · 默认AMF集所支持的S-NSSAI范围（NSSFDFTAMFSET）

## 使用实例

假如运营商希望删除INDEX为1的记录，执行下列命令。

```
RMV NSSFDFTAMFSET: INDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除默认AMF集所支持的S-NSSAI范围（RMV-NSSFDFTAMFSET）_12111346.md`
