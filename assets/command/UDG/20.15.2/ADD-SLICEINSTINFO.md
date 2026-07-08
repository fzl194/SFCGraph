---
id: UDG@20.15.2@MMLCommand@ADD SLICEINSTINFO
type: MMLCommand
name: ADD SLICEINSTINFO（添加切片实例信息）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SLICEINSTINFO
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 128
category_path:
- 用户面服务管理
- 会话管理
- 网络切片管理
- 网络切片实例信息
status: active
---

# ADD SLICEINSTINFO（添加切片实例信息）

## 功能

**适用NF：UPF**

此命令用于添加切片实例信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为128。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSIINFO | NsiInfo | 可选必选说明：必选参数<br>参数含义：NSIINFO。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～40。<br>默认值：无<br>配置原则：无 |
| NSSIID | NSSI ID | 可选必选说明：必选参数<br>参数含义：NSSI ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～40。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SLICEINSTINFO]] · 切片实例信息（SLICEINSTINFO）

## 使用实例

添加切片实例信息：

```
ADD SLICEINSTINFO: NSSIID="1", NsiInfo="test";RETCODE = 0  操作成功
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-SLICEINSTINFO.md`
