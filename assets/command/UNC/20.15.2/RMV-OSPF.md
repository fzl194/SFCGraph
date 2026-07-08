---
id: UNC@20.15.2@MMLCommand@RMV OSPF
type: MMLCommand
name: RMV OSPF（删除OSPF进程配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: OSPF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF进程配置
status: active
---

# RMV OSPF（删除OSPF进程配置）

## 功能

该命令用于删除OSPF协议进程。

![](删除OSPF进程配置（RMV OSPF）_00841109.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，该操作会导致路由器之间的OSPF邻接关系中断，且以前的信息将无法恢复。

## 注意事项

- 该命令执行后立即生效。
- 删除OSPF进程可能会导致业务受损。
- 删除OSPF进程会导致路由器之间的OSPF邻接关系中断。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPF]] · OSPF进程配置（OSPF）

## 使用实例

删除OSPF协议进程号为1的配置：

```
RMV OSPF: PROCID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-OSPF.md`
