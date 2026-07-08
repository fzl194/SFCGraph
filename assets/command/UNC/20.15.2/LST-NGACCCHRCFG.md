---
id: UNC@20.15.2@MMLCommand@LST NGACCCHRCFG
type: MMLCommand
name: LST NGACCCHRCFG（查询NG接入CHR上报策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGACCCHRCFG
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- CHR管理
- NG接入CHR配置
status: active
---

# LST NGACCCHRCFG（查询NG接入CHR上报策略）

## 功能

**适用NF：AMF**

该命令用于查询系统上报NG接入CHR单据采集及订阅流程设置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGACCCHRCFG]] · NG接入CHR上报策略（NGACCCHRCFG）

## 使用实例

查询NG接入CHR单据采集策略配置：

```
%%LST NGACCCHRCFG:;%%
RETCODE = 0  操作成功

结果如下
------------------------
高性能服务器上报流程控制模板索引  =  0
低性能服务器上报流程控制模板索引  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NG接入CHR上报策略（LST-NGACCCHRCFG）_34945603.md`
