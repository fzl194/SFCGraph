---
id: UDG@20.15.2@MMLCommand@RMV RPTPROTMPCLASS
type: MMLCommand
name: RMV RPTPROTMPCLASS（删除业务报表映射承载协议分类配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RPTPROTMPCLASS
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务报表管理
- 报表本地策略管理
- 报表映射承载协议分类
status: active
---

# RMV RPTPROTMPCLASS（删除业务报表映射承载协议分类配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除业务报表映射承载协议分类配置。当运营商希望删除业务报表映射承载协议分类配置，则配置该命令。

## 注意事项

- 该命令执行后立即生效。
- 如果引用了该映射承载协议分类的映射记录存在，则不允许删除映射承载协议分类。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MPPROTCLASSNM | 映射承载协议分类名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置映射承载协议分类名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTPROTMPCLASS]] · 业务报表映射承载协议分类配置（RPTPROTMPCLASS）

## 使用实例

假如运营商需要删除名称为p2p的业务报表映射承载协议分类配置：

```
RMV RPTPROTMPCLASS: MPPROTCLASSNM="p2p";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-RPTPROTMPCLASS.md`
