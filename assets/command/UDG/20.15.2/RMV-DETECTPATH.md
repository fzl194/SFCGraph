---
id: UDG@20.15.2@MMLCommand@RMV DETECTPATH
type: MMLCommand
name: RMV DETECTPATH（删除探测路径配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: DETECTPATH
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- N6路径管理
- N6路径参数
status: active
---

# RMV DETECTPATH（删除探测路径配置）

## 功能

**适用NF：UPF**

该命令用于删除探测路径配置。

## 注意事项

- 该命令执行后立即生效。
- 探测路径绑定APN后，路径信息不允许删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PATHNAME | 路径名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用于连通性探测的路径名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DETECTPATH]] · 探测路径配置（DETECTPATH）

## 使用实例

删除一条名为“testpath3”的探测路径配置：

```
RMV DETECTPATH: PATHNAME="testpath3";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除探测路径配置（RMV-DETECTPATH）_47501345.md`
