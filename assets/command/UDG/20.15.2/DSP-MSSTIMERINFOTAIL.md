---
id: UDG@20.15.2@MMLCommand@DSP MSSTIMERINFOTAIL
type: MMLCommand
name: DSP MSSTIMERINFOTAIL（查询定时器详细信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSTIMERINFOTAIL
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 定时器统计查询
status: active
---

# DSP MSSTIMERINFOTAIL（查询定时器详细信息）

## 功能

该命令用于查询定时器详细信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSSTIMERINFOTAIL]] · 定时器详细信息（MSSTIMERINFOTAIL）

## 使用实例

查询定时器详细信息：

```
DSP MSSTIMERINFOTAIL:RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
--------
定时器ID   定时器控制块魔术字    定时器状态    定时器模式    定时器类型     定时器触发类型    定时器时长（ms）    定时器超时最大/平均值（ms）    序列号        定时器回调函数名称

0          4660                  TICKING       PERIOD        NORMAL         WORKFRAME         15000               --/--                          18            PAE_DP_DrvSndFailChkHandle
1          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          21            ufp_MemLeakCheckProc
2          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          61            ufp_MemDamageCheckProc
3          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          21            ufp_MemOverLoadCheckProc
4          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          21            ufpMbufQueCollect
5          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          27            ufpMbufLeakCheck
6          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          27            ufpMbufDamageCheckPorc
7          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          27            ufpMbufOverLoadCheck
8          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          26            ufpQueDeadCheck
9          4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          27            ufpQueDamageCheck
10         4660                  TICKING       PERIOD        NORMAL         CALLBACK          1000                --/--                          27            ufpQueOverloadCheck
11         4660                  TICKING       PERIOD        NORMAL         WORKFRAME         5000                --/--                          53            PAE_DP_FabricReassTimerHandle
12         4660                  TICKING       PERIOD        NORMAL         WORKFRAME         100                 --/--                          27            PAE_DP_OamTimerHandle
13         4660                  TICKING       PERIOD        NORMAL         CALLBACK          10                  --/--                          26            ufp_SchCpuSamping
(结果个数 = 14)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MSSTIMERINFOTAIL.md`
