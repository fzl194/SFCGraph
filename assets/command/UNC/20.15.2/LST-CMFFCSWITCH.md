---
id: UNC@20.15.2@MMLCommand@LST CMFFCSWITCH
type: MMLCommand
name: LST CMFFCSWITCH（查询CMF流控开关配置数据）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CMFFCSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST CMFFCSWITCH（查询CMF流控开关配置数据）

## 功能

该命令用于查询CMF流控功能开关的配置。

## 注意事项

- CMF Pod单节点部署时不支持CMF流控，第三方CaaS场景不支持CMF流控，CSPEdge裸机场景不支持CMF流控。
- 当未执行[**SET CMFFCSWITCH**](设置CMF流控开关（SET CMFFCSWITCH）_37011290.md)命令时，本命令查询流控功能开关为“未设置”状态。默认流控功能开关取值为代码默认值，可通过[**DSP DBGHAFD**](显示HAFD调试命令结果（DSP DBGHAFD）_94730404.md)命令查询。查询时，参数DEBUGNAME取值为"cmf fc switch"。
- 当执行过[**SET CMFFCSWITCH**](设置CMF流控开关（SET CMFFCSWITCH）_37011290.md)命令后，本命令回显数据和[**DSP DBGHAFD**](显示HAFD调试命令结果（DSP DBGHAFD）_94730404.md)回显数据保持一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/CMFFCSWITCH]] · CMF流控开关配置数据（CMFFCSWITCH）

## 使用实例

查询流控功能开关的配置：

```
%%LST CMFFCSWITCH:;%%
RETCODE = 0  操作成功

结果如下
--------
流控功能开关  =  未设置
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CMFFCSWITCH.md`
