---
id: UNC@20.15.2@MMLCommand@LST STGALARMCTRL
type: MMLCommand
name: LST STGALARMCTRL（查询融合计费话单缓存告警上报的控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: STGALARMCTRL
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费缓存
- 缓存控制
status: active
---

# LST STGALARMCTRL（查询融合计费话单缓存告警上报的控制参数）

## 功能

**适用NF：SMF、PGW-C**

该命令用于查询融合计费话单缓存告警上报的控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@STGALARMCTRL]] · 融合计费话单缓存告警上报的控制参数（STGALARMCTRL）

## 使用实例

查询告警产生门限，告警监控时长：

```
%%LST STGALARMCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
告警产生门限  =  10240
告警监控时长  =  120
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-STGALARMCTRL.md`
