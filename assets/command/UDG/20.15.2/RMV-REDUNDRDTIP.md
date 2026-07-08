---
id: UDG@20.15.2@MMLCommand@RMV REDUNDRDTIP
type: MMLCommand
name: RMV REDUNDRDTIP（删除冗余备份重定向IP地址）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: REDUNDRDTIP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 静态地址用户路由冗余
- 冗余备份重定向IP
status: active
---

# RMV REDUNDRDTIP（删除冗余备份重定向IP地址）

## 功能

**适用NF：PGW-U、UPF**

该命令用来删除全局的冗余备份隧道虚拟重定向IP。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：可选参数<br>参数含义：该参数用于设置冗余备份重定向IP类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPv4：表示地址类型为IPv4。<br>- IPv6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/REDUNDRDTIP]] · 冗余备份重定向IP（REDUNDRDTIP）

## 使用实例

删除冗余备份隧道虚拟重定向地址：

```
RMV REDUNDRDTIP:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除冗余备份重定向IP地址（RMV-REDUNDRDTIP）_75097446.md`
