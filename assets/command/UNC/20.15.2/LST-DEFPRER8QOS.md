---
id: UNC@20.15.2@MMLCommand@LST DEFPRER8QOS
type: MMLCommand
name: LST DEFPRER8QOS（查询缺省的Pre-R8 QoS参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DEFPRER8QOS
command_category: 查询类
applicable_nf:
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- PreR8 QoS配置
- 全局PreR8 QoS纠错
status: active
---

# LST DEFPRER8QOS（查询缺省的Pre-R8 QoS参数）

## 功能

**适用NF：GGSN**

该命令用于查询UNC的QoS参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [缺省的Pre-R8 QoS参数（DEFPRER8QOS）](configobject/UNC/20.15.2/DEFPRER8QOS.md)

## 使用实例

查询QoS缺省配置：

```
%%LST DEFPRER8QOS:;%%
RETCODE = 0  操作成功

结果如下
--------
                         ARP值  =  高
                      延迟等级  =  1
                 发送错误的SDU  =  不检测
       下行保证带宽(千比特/秒)  =  384
       上行保证带宽(千比特/秒)  =  384
       下行最大带宽(千比特/秒)  =  384
       上行最大带宽(千比特/秒)  =  384
             最大SDU长度(字节)  =  1520
         平均吞吐量(字节/小时)  =  尽力而为
           最大吞吐量(字节/秒)  =  最大256k字节每秒
                        优先级  =  高
                    可靠性等级  =  1
  Background业务残留比特误码率  =  6E-8
Conversation业务残留比特误码率  =  1E-6
 Interactive业务残留比特误码率  =  6E-8
   Streaming业务残留比特误码率  =  1E-6
       Background业务SDU误码率  =  1E-6
     Conversation业务SDU误码率  =  1E-5
      Interactive业务SDU误码率  =  1E-6
        Streaming业务SDU误码率  =  1E-7
                  信令传输优化  =  优化
                    源统计描述  =  语音
                通信处理优先级  =  高
                      业务类型  =  会话类
                传输时延(毫秒)  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询缺省的Pre-R8-QoS参数（LST-DEFPRER8QOS）_09651521.md`
