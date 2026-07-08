---
id: UNC@20.15.2@MMLCommand@LST NRFLINKMNGPARA
type: MMLCommand
name: LST NRFLINKMNGPARA（查询NRF的链路管理参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFLINKMNGPARA
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- 链路管理
status: active
---

# LST NRFLINKMNGPARA（查询NRF的链路管理参数）

## 功能

**适用NF：NRF**

该命令用于查询NRF的链路管理参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFLINKMNGPARA]] · NRF的链路管理参数（NRFLINKMNGPARA）

## 使用实例

查询NRF的链路管理参数：

```
LST NRFLINKMNGPARA:;
%%LST NRFLINKMNGPARA:;%%
RETCODE = 0  操作成功

结果如下
------------------------
  逻辑链路刷新间隔(秒)  =  300
      单次下发地址个数  =  20
链路信息老化时长(分钟)  =  1440
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF的链路管理参数（LST-NRFLINKMNGPARA）_31773564.md`
