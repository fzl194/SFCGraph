---
id: UNC@20.15.2@MMLCommand@LST TCPBPCFG
type: MMLCommand
name: LST TCPBPCFG（查询TCP过载反压HTTP流控配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TCPBPCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP反压流控管理
status: active
---

# LST TCPBPCFG（查询TCP过载反压HTTP流控配置）

## 功能

该命令用于查询传输层TCP过载反压到应用层HTTP流控相关参数。

## 注意事项

起控阈值需大于停控阈值，且起控阈值不能低于70%，停控阈值不能低于40%。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TCPBPCFG]] · TCP过载反压HTTP流控配置（TCPBPCFG）

## 使用实例

查询TCP的CPU反压流控属性配置，可执行如下命令: LST TCPBPCFG:;

```
结果如下
------------------------
反压流量控制开关= OFF
  起始反压门限(%)=80
      开始反压持续时间=5
   反压停止阈值(%)=75
       反压停止时长=60
           流控方向=客户端
（结果数=1）
---    结束
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-TCPBPCFG.md`
