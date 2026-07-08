---
id: UDG@20.15.2@MMLCommand@DSP FABPORTSUBDTL
type: MMLCommand
name: DSP FABPORTSUBDTL（显示Fabric端口亚健康通信质量信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FABPORTSUBDTL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP FABPORTSUBDTL（显示Fabric端口亚健康通信质量信息）

## 功能

该命令用于显示Fabric端口亚健康通信质量信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP PAENODE**](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)<br>查看工作角色为数据转发对应的微服务实例号。 |

## 操作的配置对象

- [Fabric端口亚健康通信质量信息（FABPORTSUBDTL）](configobject/UDG/20.15.2/FABPORTSUBDTL.md)

## 使用实例

查询Fabric端口亚健康通信质量。

```
%%DSP FABPORTSUBDTL: CELLINSTANCE="vusn-pod-0__103__0";%%
RETCODE = 0  操作成功

结果如下
--------
源Cell名称                源节点名称        源主机名称      目的Cell名称                          目的节点名称    目的主机名称     端口名称  端口通信方向  亚健康发生时间  
vusn-pod-0__103__0        192.168.1.1       host-1          vsm-pod-8f88bf67d-6qtz2__103__0       192.168.1.2     host-2           port-1    1             2025-02-14 11:37:55        
vusn-pod-0__103__0        192.168.1.1       host-1          gtp-pod-669d99bdb7-9dgdv__103__0      192.168.1.3     host-3           port-2    1             2025-02-14 11:37:55
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示Fabric端口亚健康通信质量信息（DSP-FABPORTSUBDTL）_76129914.md`
