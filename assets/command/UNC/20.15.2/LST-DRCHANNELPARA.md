---
id: UNC@20.15.2@MMLCommand@LST DRCHANNELPARA
type: MMLCommand
name: LST DRCHANNELPARA（查询容灾通道参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DRCHANNELPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 容灾管理
status: active
---

# LST DRCHANNELPARA（查询容灾通道参数）

## 功能

该命令用于查询CSDB容灾通道参数，包括心跳间隔和消息重试次数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLUSTERID | 子集群标识 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定唯一一个子集群，可以通过<br>**[DSP DBCLUSTER](../集群管理/查询CSDB子集群信息（DSP DBCLUSTER）_29626985.md)**<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：1～10。<br>默认值：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DRCHANNELPARA]] · 容灾通道参数（DRCHANNELPARA）

## 使用实例

查询所有子集群的容灾通道参数：

```
LST DRCHANNELPARA:;
%%LST DRCHANNELPARA:;%%
RETCODE = 0  操作成功
操作结果如下：
--------------
          子集群标识  =  1
    容灾通道心跳间隔  =  20
容灾通道消息重试次数  =  20
         
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DRCHANNELPARA.md`
