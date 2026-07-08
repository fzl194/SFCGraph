---
id: UNC@20.15.2@MMLCommand@LST NRFDATACHK
type: MMLCommand
name: LST NRFDATACHK（查询NRF数据一致性核查相关参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFDATACHK
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF数据一致性核查
status: active
---

# LST NRFDATACHK（查询NRF数据一致性核查相关参数）

## 功能

**适用NF：NRF**

该命令用于查询NRF数据核查相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFDATACHK]] · NRF数据一致性核查相关参数（NRFDATACHK）

## 使用实例

查询NRF数据核查相关参数。

```
LST NRFDATACHK;
%%LST NRFDATACHK;%%
RETCODE = 0  执行成功

操作结果如下:
-------------------------
          核查周期(分)  =  15
      核查失败告警开关  =  打开
      回复心跳失败开关  =  打开
数据一致性核查功能开关  =  打开

(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFDATACHK.md`
