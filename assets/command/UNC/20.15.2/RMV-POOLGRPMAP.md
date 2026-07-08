---
id: UNC@20.15.2@MMLCommand@RMV POOLGRPMAP
type: MMLCommand
name: RMV POOLGRPMAP（删除地址池组映射关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: POOLGRPMAP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址池组映射配置
status: active
---

# RMV POOLGRPMAP（删除地址池组映射关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除地址池组和UPF组的映射关系，当地址池组中的地址池不再使用时，可使用该命令将其删除。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MAPPINGNAME | 映射名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池组映射规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [地址池组映射关系（POOLGRPMAP）](configobject/UNC/20.15.2/POOLGRPMAP.md)

## 使用实例

删除地址池组和UPF组的映射关系，映射是one：

```
RMV POOLGRPMAP: MAPPINGNAME="one";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除地址池组映射关系（RMV-POOLGRPMAP）_32232827.md`
