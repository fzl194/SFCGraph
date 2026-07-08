---
id: UNC@20.15.2@MMLCommand@DSP NRFDISCERRSTAT
type: MMLCommand
name: DSP NRFDISCERRSTAT（显示NRF记录的错误统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NRFDISCERRSTAT
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF维测管理
status: active
---

# DSP NRFDISCERRSTAT（显示NRF记录的错误统计信息）

## 功能

**适用NF：NRF**

该命令用于查询NF服务发现过程中NRF记录的错误统计信息，用于支撑定位问题。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFDISCERRSTAT]] · NRF记录的错误统计信息（NRFDISCERRSTAT）

## 使用实例

查询NRF记录的错误统计信息：

```
 DSP NRFDISCERRSTAT:;
%% DSP NRFDISCERRSTAT:;%%
RETCODE = 0  操作成功

结果如下
------------------------
CellServiceID  错误描述                                  错误统计次数  最后一次错误发生的时间

0              queryNfInstancesByTai_RecordNotFoundErr   11            2019-09-17 08:14:38.921196576 +0       
0              DiscDslFinal_DiscDslFinalErr              25            2019-09-17 08:10:36.156884259 +0   
(结果个数 = 2)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NRFDISCERRSTAT.md`
