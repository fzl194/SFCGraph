---
id: UDG@20.15.2@MMLCommand@RMV OSPFV3
type: MMLCommand
name: RMV OSPFV3（删除OSPFv3进程配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFV3
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3进程配置
status: active
---

# RMV OSPFV3（删除OSPFv3进程配置）

## 功能

该命令用于删除OSPFv3协议进程。

![](删除OSPFv3进程配置（RMV OSPFV3）_00866049.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会导致路由器之间的OSPFv3邻接关系中断，且以前的信息将无法恢复。

## 注意事项

- 该命令执行后立即生效。
- 删除OSPFv3进程可能会导致业务受损。
- 删除OSPFv3进程会导致路由器之间的OSPFv3邻居关系中断。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPFv3进程必须已经存在。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFV3]] · OSPFv3进程配置（OSPFV3）

## 使用实例

删除OSPFv3协议进程号为1的配置：

```
RMV OSPFV3: PROCID=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除OSPFv3进程配置（RMV-OSPFV3）_00866049.md`
