---
id: UDG@20.15.2@MMLCommand@RMV L2TPLNSINFO
type: MMLCommand
name: RMV L2TPLNSINFO（删除L2TP组中的LNS信息）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: L2TPLNSINFO
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- L2tp组Lns信息
status: active
---

# RMV L2TPLNSINFO（删除L2TP组中的LNS信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除L2TP组中的LNS信息。

## 注意事项

- 该命令执行后立即生效。
- 当L2TP组存在用户时，不允许通过RMV L2TPLNSINFO命令删除LNS配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | L2TP组号 | 可选必选说明：必选参数<br>参数含义：指定L2TP组号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1500。<br>默认值：无<br>配置原则：该参数使用ADD L2TPGROUP命令配置生成。 |
| LNSNO | LNS序号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定添加LNS的序号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/L2TPLNSINFO]] · L2TP组的LNS信息（L2TPLNSINFO）

## 使用实例

假设用户不需要使用l2TP组1中的LNS NUMBER为1的LNS：

```
RMV L2TPLNSINFO: GROUPID=1, LNSNO=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-L2TPLNSINFO.md`
