---
id: UDG@20.15.2@MMLCommand@RMV CFPFSPECACTION
type: MMLCommand
name: RMV CFPFSPECACTION（删除指定内容过滤策略特殊场景下的业务动作）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CFPFSPECACTION
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤策略特殊场景下的业务动作
status: active
---

# RMV CFPFSPECACTION（删除指定内容过滤策略特殊场景下的业务动作）

## 功能

**适用NF：PGW-U、UPF**

删除指定内容过滤策略特殊场景下的业务动作。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFPROFILENAME | 套餐名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容过滤策略名称。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CFPFSPECACTION]] · 指定内容过滤策略特殊场景下的业务动作（CFPFSPECACTION）

## 使用实例

删除指定名字test的指定内容过滤策略特殊场景下的业务动作：

```
RMV CFPFSPECACTION: CFPROFILENAME="profile1_test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-CFPFSPECACTION.md`
