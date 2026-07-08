---
id: UNC@20.15.2@MMLCommand@DSP SRVMSGSTAT
type: MMLCommand
name: DSP SRVMSGSTAT（查询服务消息统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SRVMSGSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 服务管理
- 服务消息统计
status: active
---

# DSP SRVMSGSTAT（查询服务消息统计）

## 功能

该命令用于查询服务申请的处理统计信息。

## 注意事项

该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONSUMERVNFCID | 服务VNFC ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在业务VNFC下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_59103764.md)**<br>获得，所得NODEID即为服务VNFC ID。<br>数据来源：全网规划<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SRVMSGSTAT]] · 服务消息统计（SRVMSGSTAT）

## 使用实例

查询服务消息统计

DSP SRVMSGSTAT: CONSUMERVNFCID=4;

```
%%DSP SRVMSGSTAT: CONSUMERVNFCID=4;%%
RETCODE = 0  操作成功。

结果如下
--------
                               服务VNFC ID  =  4
                    接收服务申请消息的次数  =  1
                接收整机减容请求消息的次数  =  0
                接收自动减容请求消息的次数  =  0
           接收add prgrp请求响应消息的次数  =  0
           接收del prgrp请求响应消息的次数  =  0
                  接收del ru请求消息的次数  =  0
                  接收查询ru状态消息的次数  =  0
                          接收RU开工的次数  =  1
接收的ADD RU/MANO SCALE/AUTO SCALE开工次数  =  0
              接收的RU故障恢复后RU开工次数  =  0
                接收的下游业务响应消息次数  =  1
            接收服务框架收到拓扑的响应次数  =  1
                接收的服务框架查询拓扑次数  =  0
                    发送首包响应消息的次数  =  1
                  发送本地扩减容消息的次数  =  1
                  发送远端扩减容消息的次数  =  1
                 发送ScaleIn响应消息的次数  =  0
                   发送add prgrp消息的次数  =  0
                   发送del prgrp消息的次数  =  0
                发送del ruid响应消息的次数  =  0
              发送查询ru状态响应消息的次数  =  0
                发送服务申请响应消息的次数  =  1
                          主动推送拓扑次数  =  1
                      发送业务平滑消息次数  =  0
                              上次清除时间  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SRVMSGSTAT.md`
