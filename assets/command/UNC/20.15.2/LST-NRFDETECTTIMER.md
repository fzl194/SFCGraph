---
id: UNC@20.15.2@MMLCommand@LST NRFDETECTTIMER
type: MMLCommand
name: LST NRFDETECTTIMER（查询NRF检测时长信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFDETECTTIMER
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF检测时长信息管理
status: active
---

# LST NRFDETECTTIMER（查询NRF检测时长信息）

## 功能

**适用NF：NRF**

该命令用于查询NRF上各类检测时长信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFDETECTTIMER]] · NRF检测时长信息（NRFDETECTTIMER）

## 使用实例

查询NRF检测时长信息。

```
LST NRFDETECTTIMER:;
%%LST NRFDETECTTIMER:;%%
RETCODE = 0  操作成功

结果如下
--------
内部资源使用超限检测时长(秒)    =  1200
NF携带信元防呆故障检测时长(秒)  =  600
             TPS平滑取值周期数  =  20
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF检测时长信息（LST-NRFDETECTTIMER）_45168567.md`
