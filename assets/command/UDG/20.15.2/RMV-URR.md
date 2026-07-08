---
id: UDG@20.15.2@MMLCommand@RMV URR
type: MMLCommand
name: RMV URR（删除URR）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: URR
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 使用率上报规则
status: active
---

# RMV URR（删除URR）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除使用量上报规则信息。当运营商希望删除使用量上报规则信息，则配置该命令。

## 注意事项

- 该命令执行后立即生效。
- 如果不输入使用量上报规则信息名称，表示删除系统中所有使用量上报规则信息。当配置量较大时单次执行可能无法删除全部记录，需要执行多次。
- 如果引用了该使用量上报规则信息的计费属性记录存在，则不允许删除使用量上报规则信息记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| URRNAME | 使用量上报规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置URR名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [URR（URR）](configobject/UDG/20.15.2/URR.md)

## 使用实例

假如运营商需要删除名称为onlineURR的使用量上报规则信息：

```
RMV URR: URRNAME="onlineURR";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除URR（RMV-URR）_86527145.md`
