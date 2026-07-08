---
id: UNC@20.15.2@MMLCommand@LST PCCTIMER
type: MMLCommand
name: LST PCCTIMER（查询PCC定时器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCCTIMER
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 信令控制
- 定时器
status: active
---

# LST PCCTIMER（查询PCC定时器）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询PCC定时器配置参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCCTIMER]] · 复位PCC定时器（PCCTIMER）

## 使用实例

查询PCC定时器配置参数：

```
LST PCCTIMER:;
```

```

RETCODE = 0  操作成功

PCC定时器信息
-------------
         Revalidation重授权迟滞时间（秒）  =  600
                           应用层重传次数  =  0
                         事务等待重传次数  =  1
              N7接口TxTimer定时器时长系数  =  1
                 应用层重传时间间隔（秒）  =  5
                    事务等待重传间隔 (秒)  =  1
           用户回滚后在线保持时长（分钟）  =  0
                     重定向迟滞时间（秒）  =  600
Failover All-sessions定时器超时时长(分钟)  =  3
     Supported-features协商定时器（分钟）  =  60
                 动态PCRF老化时长（分钟）  =  60
                     随机延迟范围（分钟）  =  0
                     N7接口请求信息定时器  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PCC定时器（LST-PCCTIMER）_96782686.md`
