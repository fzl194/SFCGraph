---
id: UNC@20.15.2@MMLCommand@LST LINKCONGCTRL
type: MMLCommand
name: LST LINKCONGCTRL（查询Diameter链路拥塞控制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LINKCONGCTRL
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- Diameter链路拥塞控制
status: active
---

# LST LINKCONGCTRL（查询Diameter链路拥塞控制）

## 功能

**适用NF：PGW-C、SMF**

此命令用来查询链路拥塞触发告警和链路拥塞触发重建链相关参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LINKCONGCTRL]] · Diameter链路拥塞控制（LINKCONGCTRL）

## 使用实例

查询LinkCongCtrl命令配置：

```
LST LINKCONGCTRL:;
```

```

RETCODE = 0  操作成功

Diameter链路拥塞控制
--------------------
                告警开关  =  允许
        告警上报检测周期  =  12
      链路重建的检测周期  =  255
触发链路重建的链路拥塞率  =  80
        告警恢复检测周期  =  12
            链路重建开关  =  禁止
触发告警上报的链路拥塞率  =  20
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LINKCONGCTRL.md`
