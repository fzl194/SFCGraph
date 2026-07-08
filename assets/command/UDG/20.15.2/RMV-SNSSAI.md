---
id: UDG@20.15.2@MMLCommand@RMV SNSSAI
type: MMLCommand
name: RMV SNSSAI（删除NF支持的网络切片选择标识）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SNSSAI
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 网络切片管理
- 网络切片选择标识
status: active
---

# RMV SNSSAI（删除NF支持的网络切片选择标识）

## 功能

**适用NF：UPF**

该命令用于删除指定或所有配置的网络切片选择标识。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SST | 切片/服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用来设置切片/服务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无<br>配置原则：该参数使用ADD SNSSAI命令配置生成。 |
| SD | 切片区分码 | 可选必选说明：可选参数<br>参数含义：该参数用来指定切片区分码。<br>数据来源：全网规划<br>取值范围：字符串类型，每个字符必须为0~9的数字或a~f/A-F的字母,大小写不敏感。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD SNSSAI命令配置生成。<br>- 该参数必须是长度为6的字符串。如S-NSSAI无SD，SD需配置为全F。若用户配置时，不输入SD参数，默认将SD配置为全F。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SNSSAI]] · NF支持的网络切片选择标识（SNSSAI）

## 使用实例

删除UPF配置的指定网络切片选择标识：

```
RMV SNSSAI: SST=1, SD="123456";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除NF支持的网络切片选择标识（RMV-SNSSAI）_95089579.md`
