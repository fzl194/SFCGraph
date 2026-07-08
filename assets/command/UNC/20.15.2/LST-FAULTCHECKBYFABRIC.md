---
id: UNC@20.15.2@MMLCommand@LST FAULTCHECKBYFABRIC
type: MMLCommand
name: LST FAULTCHECKBYFABRIC（查询故障快速检测配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FAULTCHECKBYFABRIC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST FAULTCHECKBYFABRIC（查询故障快速检测配置信息）

## 功能

该命令用于查询基于Fabric链路状态的故障快速检测参数配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@FAULTCHECKBYFABRIC]] · 故障快速检测配置信息（FAULTCHECKBYFABRIC）

## 使用实例

查询故障快速检测配置。

```
%%LST FAULTCHECKBYFABRIC:;%%
RETCODE = 0  操作成功

结果如下
------------------------
   故障快速检测开关  =  开启
防震荡保护时长 (分)  =  20
等待上报时长 (毫秒)  =  4000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-FAULTCHECKBYFABRIC.md`
