---
id: UDG@20.15.2@MMLCommand@ADD HBUSRATTRCONF
type: MMLCommand
name: ADD HBUSRATTRCONF（新增高带宽用户属性）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: HBUSRATTRCONF
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 8
category_path:
- 用户面服务管理
- 业务匹配策略
- 体验分级
- 体验分级用户匹配
- 高带宽用户属性
status: active
---

# ADD HBUSRATTRCONF（新增高带宽用户属性）

## 功能

**适用NF：PGW-U、UPF**

该命令用于新增高带宽用户属性。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为8。
- 在同一条高带宽用户属性命令中，不同的过滤条件为与关系，即所有过滤条件均匹配中，才认为匹配中高带宽用户。
- 用户的高带宽用户属性变化后，对新流生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONFNAME | 高带宽用户属性名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置高带宽用户属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| USRATTRCONDNM1 | 过滤条件名称1 | 可选必选说明：必选参数<br>参数含义：该参数用于设置过滤条件名称1。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USRATTRCOND命令配置生成。 |
| USRATTRCONDNM2 | 过滤条件名称2 | 可选必选说明：可选参数<br>参数含义：该参数用于设置过滤条件名称2。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USRATTRCOND命令配置生成。 |
| USRATTRCONDNM3 | 过滤条件名称3 | 可选必选说明：可选参数<br>参数含义：该参数用于设置过滤条件名称3。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USRATTRCOND命令配置生成。 |
| USRATTRCONDNM4 | 过滤条件名称4 | 可选必选说明：可选参数<br>参数含义：该参数用于设置过滤条件名称4。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USRATTRCOND命令配置生成。 |

## 操作的配置对象

- [高带宽用户属性（HBUSRATTRCONF）](configobject/UDG/20.15.2/HBUSRATTRCONF.md)

## 使用实例

新增指定UsrAttrCondNm1为高带宽用户的高带宽用户属性：

```
ADD HBUSRATTRCONF: CONFNAME="conf1", USRATTRCONDNM1="UsrAttrCondNm1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/新增高带宽用户属性（ADD-HBUSRATTRCONF）_46287562.md`
