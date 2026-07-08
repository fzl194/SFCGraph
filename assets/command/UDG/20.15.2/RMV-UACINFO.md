---
id: UDG@20.15.2@MMLCommand@RMV UACINFO
type: MMLCommand
name: RMV UACINFO（删除UAC信息）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UACINFO
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 专网策略配置
- UAC信息
status: active
---

# RMV UACINFO（删除UAC信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除UAC服务器的地址信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UACNAME | UAC名称 | 可选必选说明：必选参数<br>参数含义：UAC名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UAC信息（UACINFO）](configobject/UDG/20.15.2/UACINFO.md)

## 使用实例

使用命令RMV UACINFO删除UAC服务器的地址信息：

```
RMV UACINFO: UACNAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除UAC信息（RMV-UACINFO）_28121351.md`
