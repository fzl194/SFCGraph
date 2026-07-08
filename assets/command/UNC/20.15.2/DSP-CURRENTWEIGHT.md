---
id: UNC@20.15.2@MMLCommand@DSP CURRENTWEIGHT
type: MMLCommand
name: DSP CURRENTWEIGHT（显示服务类型当前时间的非动态权重）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CURRENTWEIGHT
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 权重分配管理
- 展示当前权重信息
status: active
---

# DSP CURRENTWEIGHT（显示服务类型当前时间的非动态权重）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询当前的权重配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务类型。<br>数据来源：本端规划<br>取值范围：<br>- “UAM_0（UAM_0）”：涉及如下类型POD：接入/移动性管理POD。<br>- “USM_0（USM_0）”：涉及如下类型POD：会话管理POD。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CURRENTWEIGHT]] · 服务类型当前时间的非动态权重（CURRENTWEIGHT）

## 使用实例

查询“服务类型”为“USM_0”的pod的当前权重信息，执行如下命令：

```
%%DSP CURRENTWEIGHT: SERVICETYPE=USM_0;%%
RETCODE = 20111 操作成功

结果如下
--------
服务类型  POD名称  Host ID  Node ID  权重  当前权重策略类型
USM_0  sm2-pod-0 192.168.1.4  192.168.1.5  1.000   STATIC
(结果个数 = 1)

---    END 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示服务类型当前时间的非动态权重（DSP-CURRENTWEIGHT）_27256388.md`
