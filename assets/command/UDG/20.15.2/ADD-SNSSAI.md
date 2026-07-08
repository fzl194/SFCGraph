---
id: UDG@20.15.2@MMLCommand@ADD SNSSAI
type: MMLCommand
name: ADD SNSSAI（增加NF支持的网络切片选择标识）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SNSSAI
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 8192
category_path:
- 用户面服务管理
- 会话管理
- 网络切片管理
- 网络切片选择标识
status: active
---

# ADD SNSSAI（增加NF支持的网络切片选择标识）

## 功能

**适用NF：UPF**

该命令用于添加一个新的网络切片选择标识。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为8192。
- 不配置该命令不影响用户激活。
- 如果需要基于SNSSAI进行性能统计或基于SNSSAI进行报文转发，需要配置该命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SST | 切片/服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用来设置切片/服务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无<br>配置原则：无 |
| SD | 切片区分码 | 可选必选说明：可选参数<br>参数含义：该参数用来指定切片区分码。<br>数据来源：全网规划<br>取值范围：字符串类型，每个字符必须为0~9的数字或a~f/A-F的字母,大小写不敏感。<br>默认值：无<br>配置原则：该参数必须是长度为6的字符串。如S-NSSAI无SD，SD需配置为全F。若用户配置时，不输入SD参数，默认将SD配置为全F。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NF支持的网络切片选择标识（SNSSAI）](configobject/UDG/20.15.2/SNSSAI.md)

## 使用实例

假如运营商希望增加一条SST为1，SD为"123456"的记录：

```
ADD SNSSAI: SST=1, SD="123456";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加NF支持的网络切片选择标识（ADD-SNSSAI）_95089577.md`
