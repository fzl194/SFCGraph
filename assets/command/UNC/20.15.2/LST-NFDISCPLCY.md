---
id: UNC@20.15.2@MMLCommand@LST NFDISCPLCY
type: MMLCommand
name: LST NFDISCPLCY（查询NF的服务发现策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFDISCPLCY
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- NF发现策略管理
status: active
---

# LST NFDISCPLCY（查询NF的服务发现策略）

## 功能

**适用NF：AMF、SMF、NSSF、NRF、NCG**

该命令用于查询配置的服务发现流程的策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFDISCPLCY]] · NF的服务发现策略（NFDISCPLCY）

## 使用实例

查询配置服务发现流程策略。

```
%%LST NFDISCPLCY:;%%
RETCODE = 0  操作成功

结果如下
--------
                                   缓存开关  =  ON
                               服务发现策略  =  LOCAL_FIRST
                           缓存清理策略开关  =  ON
                               缓存更新开关  =  ON
                               列表检索开关  =  OFF
                     Locality优选的匹配策略  =  LOCSELECT_INVALID
                         APN NI和OI选择开关  =  OFF
                  周期性强制NRF服务发现开关  =  COMMERCIAL_MODE
                    强制NRF服务发现周期(秒)  =  600
                               缓存锁定开关  =  OFF
                     NF实例标识冲突核查开关  =  OFF
                       最大有效负载(千字节)  =  0
                   网元选择基于负载控制开关  =  OFF
             NF Service选择基于负载控制开关  =  OFF
                     网元缓存同步区域化开关  =  OFF
NF缓存服务发现是否支持perPlmnSnssaiList开关  =  OFF
                       列表检索的目标NF类型  =  NULL
                        列表检索速率(个/秒)  =  1
                           广播服务发现策略  =  LOCAL_FIRST
                  本地发现TAI优先级优选开关  =  OFF
                        SmfInfoList匹配策略  =  禁止使用
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFDISCPLCY.md`
