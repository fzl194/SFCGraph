---
id: UNC@20.15.2@MMLCommand@LST NRFDISCVERIFY
type: MMLCommand
name: LST NRFDISCVERIFY（查询服务发现NF属性冲突核验参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFDISCVERIFY
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF属性冲突核验
status: active
---

# LST NRFDISCVERIFY（查询服务发现NF属性冲突核验参数）

## 功能

**适用NF：NRF**

该命令用于查询服务发现流程中NF属性冲突核验参数，该参数用于控制发现流程中NF属性冲突核验行为。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFDISCVERIFY]] · 服务发现NF属性冲突核验参数（NRFDISCVERIFY）

## 使用实例

查询服务发现流程中NF属性冲突核验参数记录。

```
LST NRFDISCVERIFY:;
%%LST NRFDISCVERIFY:;%%
RETCODE = 0  操作成功

结果如下
--------
   服务发现NF属性冲突核验开关  =  打开
                     起始位置  =  10
                         长度  =  3
             NF间冲突核验属性  =  IMSI&MSISDN&ROUTINGINDICATOR&TAI&IPV6PREFIX
NF和跨NRF路由数据冲突核验属性  =  IMSI&ROUTINGINDICATOR&TAI&IPV6PREFIX
       告警最长老化时长(分钟)  =  10
    单进程最大核验速率(次/秒)  =  3
   服务发现NF属性冲突优选开关  =  打开   
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFDISCVERIFY.md`
