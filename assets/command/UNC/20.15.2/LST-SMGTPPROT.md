---
id: UNC@20.15.2@MMLCommand@LST SMGTPPROT
type: MMLCommand
name: LST SMGTPPROT（查询会话管理GTP协议功能参数配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMGTPPROT
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
- 会话协议参数管理
- GTP会话协议参数管理
- GTP会话协议参数
status: active
---

# LST SMGTPPROT（查询会话管理GTP协议功能参数配置）

## 功能

**适用NF：SGW-C、PGW-C、GGSN**

该命令用于查询会话管理GTP协议功能参数配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMGTPPROT]] · 会话管理GTP协议功能参数配置（SMGTPPROT）

## 使用实例

查询会话管理GTP协议参数配置：

```
%%LST SMGTPPROT:;%%
RETCODE = 0  操作成功

结果如下
--------
                         GTP协议版本  =  GTPV2
                       承载级PCO开关  =  不使能
去活消息携带reactivation-request开关  =  不使能
    透明传输reactivation-request开关  =  使能
              S5S8接口支持多承载开关  =  不使能
               S2b接口支持多承载开关  =  不使能
          NB-IoT场景ePCO信元携带方式  =  协商模式
            不携带MSISDN用户激活策略  =  使能
                      PCO携带QoS开关  =  使能
                          Ppd功能开关 = 不使能
         23G网络侧发起的二次激活开关  =  使能
             LTE到GU专有承载切换开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMGTPPROT.md`
