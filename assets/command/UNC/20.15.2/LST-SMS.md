---
id: UNC@20.15.2@MMLCommand@LST SMS
type: MMLCommand
name: LST SMS（查询SMS配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMS
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 短消息
- 短消息配置
status: active
---

# LST SMS（查询SMS配置信息）

## 功能

**适用网元：SGSN**

该命令用于查询SMS参数表中的配置数据。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMS]] · SMS配置信息（SMS）

## 使用实例

查询SMS参数设置：

LST SMS:;

```
%%LST SMS:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
                  QoS可靠性  =  1
                  QoS优先级  =  1
                QoS延迟等级  =  1
              QoS最大吞吐量  =  9
              QoS平均吞吐量  =  18
         短消息最大试发次数  =  3
   SMMO等待RP_ACK定时器(ms)  =  20000
   SMMO等待CP_ACK定时器(ms)  =  6500
   SMMT等待CP_ACK定时器(ms)  =  6500
  SMMT等待CP_DATA定时器(ms)  =  10000
S-SMO-CDR中记录的短消息中心  =  请求的短消息中心
           SMS ODB 限制方案  =  根据目的号码限制
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMS配置信息(LST-SMS)_26145732.md`
