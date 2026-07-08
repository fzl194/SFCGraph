---
id: UNC@20.15.2@MMLCommand@LST OCSALMTHD
type: MMLCommand
name: LST OCSALMTHD（查询OCS告警阈值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OCSALMTHD
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 告警管理
- OCS告警阈值
status: active
---

# LST OCSALMTHD（查询OCS告警阈值）

## 功能

**适用NF：PGW-C、SMF**

该命令用于显示OCS告警相关配置。包括OCS链路告警阈值、OCS链路状态采样配置和OCS应用层告警阈值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/OCSALMTHD]] · OCS告警阈值（OCSALMTHD）

## 使用实例

显示OCS告警阈值相关配置：

```
LST OCSALMTHD:;
```

```

RETCODE = 0  操作成功。

OCS告警阈值
-----------
  OCS链路告警产生阈值（%）  =  50
  OCS链路告警恢复阈值（%）  =  80
OCS链路状态采样间隔 （秒）  =  5
       OCS链路状态采样次数  =  12
            连续检测周期数  =  15
     OCS应用层告警产生阈值  =  20
     OCS应用层告警恢复阈值  =  10
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询OCS告警阈值（LST-OCSALMTHD）_09897343.md`
