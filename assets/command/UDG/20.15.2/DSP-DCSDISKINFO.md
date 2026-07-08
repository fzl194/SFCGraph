---
id: UDG@20.15.2@MMLCommand@DSP DCSDISKINFO
type: MMLCommand
name: DSP DCSDISKINFO（显示DCS直通存储使用率）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DCSDISKINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- MML命令
- 系统资源管理
status: active
---

# DSP DCSDISKINFO（显示DCS直通存储使用率）

## 功能

本命令用于显示DCS直通存储使用率。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：DCS微服务对应的POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DCSDISKINFO]] · DCS直通存储使用率（DCSDISKINFO）

## 使用实例

显示“relay-pod-0”POD的DCS直通存储使用率。

```
%%DSP DCSDISKINFO: PODNAME="relay-pod-0";%%
RETCODE = 0  操作成功

结果如下
------------------------
        POD名称  =  relay-pod-0
         容器ID  =  relay-pod-0__171
       节点名称  =  192.168.1.2
       分区名称  =  vdc
分区使用率（%）  =  25
 读速率（KB/s）  =  63
 写速率（KB/s）  =  2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示DCS直通存储使用率（DSP-DCSDISKINFO）_26367873.md`
