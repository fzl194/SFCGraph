---
id: UDG@20.15.2@MMLCommand@RMV EXTENDPROP
type: MMLCommand
name: RMV EXTENDPROP（删除扩展属性配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: EXTENDPROP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- 扩展属性
status: active
---

# RMV EXTENDPROP（删除扩展属性配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用来删除所有扩展属性配置信息，或者指定名称的配置信息。

## 注意事项

- 该命令执行后立即生效。
- 如果扩展属性配置被绑定到其他配置中，如绑定到某个分类组中，则不允许删除，需要先解除绑定关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXTENDPROPNAME | 扩展属性名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置扩展属性名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [扩展属性配置（EXTENDPROP）](configobject/UDG/20.15.2/EXTENDPROP.md)

## 使用实例

删除配置扩展属性：EXTENDPROPNAME为textcategoryprop：

```
RMV EXTENDPROP:EXTENDPROPNAME="textcategoryprop";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除扩展属性配置（RMV-EXTENDPROP）_82837597.md`
