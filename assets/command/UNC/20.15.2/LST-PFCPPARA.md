---
id: UNC@20.15.2@MMLCommand@LST PFCPPARA
type: MMLCommand
name: LST PFCPPARA（查询PFCP参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PFCPPARA
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- PFCP路径管理
- PFCP路径参数管理
status: active
---

# LST PFCPPARA（查询PFCP参数）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询PFCP参数，包括SMF主动发起的N4心跳间隔和心跳阈值等参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PFCPPARA]] · PFCP参数（PFCPPARA）

## 使用实例

以下命令用于查询所有的PFCPPARA： LST PFCPPARA:;

```
%%LST PFCPPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
                               心跳间隔(秒)  =  30
                               去活用户开关  =  开
                               去活间隔(秒)  =  900
                       心跳消息超时间隔(秒)  =  3
                       心跳消息发送次数阈值  =  5
PfcpSessionReport响应消息缓存队列的老化时长  =  16
                               迁移间隔(秒)  =  60
                               核查用户开关  =  开
                         惯性运行定时器(秒)  =  30
            校验UPF主动上报PFCP消息的合法性  =  关
           用户面链路故障信息老化时间(小时)  =  10
                       支持处理备份流量开关  =  是
               PFCP修改请求消息重发优化开关  =  关
                       静默路径业务迁移开关  =  使能
                   静默路径业务迁移间隔(秒)  =  0
                   静默路径业务回迁间隔(秒)  =  60
                   静默路径状态恢复间隔(秒)  =  3600
               静默路径发送偶联建立请求消息  =  使能
                   流量上报消息保序优化开关  =  关
                       发送偶联更新消息开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PFCPPARA.md`
