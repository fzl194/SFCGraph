---
id: UDG@20.15.2@MMLCommand@RMV L2TPGROUP
type: MMLCommand
name: RMV L2TPGROUP（删除指定L2TP组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: L2TPGROUP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- L2TP组
status: active
---

# RMV L2TPGROUP（删除指定L2TP组）

## 功能

**适用NF：PGW-U、UPF**

![](删除指定L2TP组（RMV L2TPGROUP）_35373526.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，如果该L2tpGroup存在用户，删除后会导致业务中断。

该命令用于删除指定的L2TP组，当不需要使用本地配置的L2TP组接入用户时，使用该命令配置。

## 注意事项

- 该命令执行后立即生效。
- 通过RMV L2TPGROUP删除组信息时，会删除该L2TP组下的所有L2TPLNSINFO配置。
- 如果这个L2TPGROUP绑定了Giif接口，则不能被删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | L2TP组号 | 可选必选说明：必选参数<br>参数含义：指定L2TP组号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1500。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/L2TPGROUP]] · 指定L2TP组（L2TPGROUP）

## 使用实例

假设用户不需要使用l2TP组1时，使用该命令进行删除：

```
RMV L2TPGROUP:GROUPID=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除指定L2TP组（RMV-L2TPGROUP）_35373526.md`
