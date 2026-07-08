---
id: UNC@20.15.2@MMLCommand@LST DFTIDLETIME
type: MMLCommand
name: LST DFTIDLETIME（查询默认空闲上下文定时器配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DFTIDLETIME
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
- 会话管理
- 接入管理
- 接入管理运维
- SMF公共配置
- 空闲上下文定时器
status: active
---

# LST DFTIDLETIME（查询默认空闲上下文定时器配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询默认空闲上下文定时器开关和时长配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DFTIDLETIME]] · 默认空闲上下文定时器配置（DFTIDLETIME）

## 使用实例

查询系统配置的默认空闲上下文定时器开关和时长参数：

```
LST DFTIDLETIME:;
RETCODE = 0  操作成功

结果如下
--------
               SGW-C空闲上下文核查开关  =  使能
PGW-C和SGW-C/PGW-C网元的上下文核查开关  =  使能
                GGSN空闲上下文核查开关  =  使能
               H-SMF空闲上下文核查开关  =  使能
             H-SMF不活动上下文核查开关  =  使能
         I-SMF/V-SMF空闲上下文核查开关  =  使能
       I-SMF/V-SMF不活动上下文核查开关  =  使能
                       GUL承载级别参数  =  会话级
             缺省承载和默认GBR的定时器  =  一天
                   承载定时器时长(min)  =  1440
                   会话定时器时长(min)  =  1440
            SMF会话空闲定时器时长(min)  =  1440
          SMF会话不活动定时器时长(min)  =  40
                  空闲超时发送更新消息  =  去使能
               H-SMF空闲上下文核查级别  =  会话级
       专有QoS Flow空闲定时器时长(min)  =  1440
       缺省QoS Flow空闲定时器时长(min)  =  1440
              GGSN一次激活上下文定时器  =  一天
         Proxy-SMF S8空闲上下文核查开关 = 使能
           Proxy-SMF 空闲上下文核查开关 = 使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DFTIDLETIME.md`
