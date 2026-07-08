---
id: UNC@20.15.2@MMLCommand@LST MSFAULTTOLERANCE
type: MMLCommand
name: LST MSFAULTTOLERANCE（查询故障检测参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MSFAULTTOLERANCE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST MSFAULTTOLERANCE（查询故障检测参数）

## 功能

该命令用于查询故障检测配置参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSFAULTTOLERANCE]] · 故障检测参数（MSFAULTTOLERANCE）

## 使用实例

查询故障检测参数的配置。

```
%%LST MSFAULTTOLERANCE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
故障检测类型                     心跳周期(100ms)       心跳超时周期数            自杀开关  

进程级别正向监控                 5                       12                        OFF             
进程级别反向监控                 5                       10                        ON              
域级别正向监控                   5                       12                        OFF             
多连接正向监控                   5                       12                        OFF             
多连接反向监控                   5                       10                        ON              
(结果个数 = 5)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MSFAULTTOLERANCE.md`
