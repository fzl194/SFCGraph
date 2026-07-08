---
id: UNC@20.15.2@MMLCommand@LST PDPNUMBERARP
type: MMLCommand
name: LST PDPNUMBERARP（查询基于PDP数的ARP控制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PDPNUMBERARP
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- Qos管理
- 基于PDP数的ARP控制
status: active
---

# LST PDPNUMBERARP（查询基于PDP数的ARP控制）

## 功能

**适用NF：SGW-C、PGW-C、GGSN**

该命令用于显示当前APN用户数比例差异化服务配置，包括拒绝告警门限和恢复告警门限信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定QoS Profile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PDPNUMBERARP]] · 基于PDP数的ARP控制（PDPNUMBERARP）

## 使用实例

- 查询给定QOSPROFILENAME对应当前APN实例按用户数比例差异化服务的配置：
  ```
  %%LST PDPNUMBERARP: QOSPROFILENAME="qp1";%%
  RETCODE = 0  操作成功

  结果如下
  --------
    QoS Profile名  =  qp1
         业务级别  =  会话业务
         用户级别  =  高
  拒绝告警门限(%)  =  100
  恢复告警门限(%)  =  99
  (结果个数 = 1)

  ---    END
  ```
- 查询当前APN实例全部的按用户数比例差异化服务的配置：
  ```
  %%LST PDPNUMBERARP:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  QoS Profile名  业务级别  用户级别  拒绝告警门限(%)  恢复告警门限(%)  

  qp1            会话业务  高        100              99            
  qp2            通用业务  中        100              1             
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询基于PDP数的ARP控制（LST-PDPNUMBERARP）_09653024.md`
