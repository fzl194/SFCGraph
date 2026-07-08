---
id: UDG@20.15.2@MMLCommand@DSP FINGIDENSTATIC
type: MMLCommand
name: DSP FINGIDENSTATIC（查询SA指纹识别统计结果）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FINGIDENSTATIC
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 协议识别
- SA指纹识别
- SA指纹识别统计
status: active
---

# DSP FINGIDENSTATIC（查询SA指纹识别统计结果）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询SA指纹识别的统计结果。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/FINGIDENSTATIC]] · SA指纹识别统计结果（FINGIDENSTATIC）

## 使用实例

显示SA指纹识别的统计结果：

```
DSP FINGIDENSTATIC:;
```

```

RETCODE = 0  操作成功

指纹识别统计信息
----------------------------------------
统计结果                                                                                                                                                                                                     

Pod Name(ssgpod-0):
StatisticStartTime is 2022-03-18 15:06:00
Protocol            DB counter          FP counter          DB=FP counter       DB<>FP counter
facebook            1000                2000                500                 200                 
youtube             3000                4000                800                 300       
(Statistic-Number = 2)

Pod Name(ssgpod-1):
StatisticStartTime is 2022-03-18 15:06:00
Protocol            DB counter          FP counter          DB=FP counter       DB<>FP counter
facebook            1000                2000                500                 200                 
youtube             3000                4000                800                 300       
(Statistic-Number = 2)

(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-FINGIDENSTATIC.md`
