---
id: UDG@20.15.2@MMLCommand@LST RELAYSALMPARA
type: MMLCommand
name: LST RELAYSALMPARA（查询媒体中继业务告警参数配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RELAYSALMPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继业务告警参数配置
status: active
---

# LST RELAYSALMPARA（查询媒体中继业务告警参数配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询媒体中继业务告警参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYSALMPARA]] · 媒体中继业务告警参数配置（RELAYSALMPARA）

## 使用实例

假如需要查询媒体中继业务告警参数，则命令如下：

```
LST RELAYSALMPARA:;
```

```

RETCODE = 0  操作成功
 
结果如下
------------------------
               告警检测时长（分钟）  =  5
                URL鉴权失败告警开关  =  使能
      URL鉴权告警上报阈值（万分比）  =  100
      URL鉴权告警恢复阈值（万分比）  =  10
            Referer校验失败告警开关  =  使能
  Referer校验告警上报阈值（万分比）  =  100
  Referer校验告警恢复阈值（万分比）  =  10
                   回源失败告警开关  =  使能
     回源失败告警上报阈值（万分比）  =  100
     回源失败告警恢复阈值（万分比）  =  10
         未知类型的媒体访问告警开关  =  使能
 未知媒体访问告警上报阈值（万分比）  =  100  
 未知媒体访问告警恢复阈值（万分比）  =  10
              Relay资源不足告警开关  =  使能
Relay资源不足告警上报阈值（百分比）  =  80
Relay资源不足告警恢复阈值（百分比）  =  75
         媒体中继UE业务失败告警开关  =  使能
   UE业务失败告警上报阈值（万分比）  =  100
   UE业务失败告警恢复阈值（万分比）  =  10
                    DNS故障告警开关  =  使能
        DNS故障告警检测时长（分钟）  =  5
        DNS告警恢复检测时长（分钟）  =  1
                   告警上报优化开关  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询媒体中继业务告警参数配置（LST-RELAYSALMPARA）_25355077.md`
