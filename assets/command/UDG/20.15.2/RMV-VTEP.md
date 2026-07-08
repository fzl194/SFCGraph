---
id: UDG@20.15.2@MMLCommand@RMV VTEP
type: MMLCommand
name: RMV VTEP（删除VXLAN隧道端点）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: VTEP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- VXLAN隧道端点配置
status: active
---

# RMV VTEP（删除VXLAN隧道端点）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除VXLAN隧道端点。

## 注意事项

- 该命令执行后立即生效。
- 当VTEP绑定到VXLAN Group上时需要先解除绑定关系才可以删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VTEPNAME | VXLAN隧道端点名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置VXLAN隧道端点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VTEP]] · VXLAN隧道端点（VTEP）

## 使用实例

删除VTEP Name为vtep1的隧道端点：

```
RMV VTEP: VTEPNAME="vtep1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除VXLAN隧道端点（RMV-VTEP）_68194505.md`
