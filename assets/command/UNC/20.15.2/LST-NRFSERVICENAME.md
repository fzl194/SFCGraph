---
id: UNC@20.15.2@MMLCommand@LST NRFSERVICENAME
type: MMLCommand
name: LST NRFSERVICENAME（查看NRF功能实体服务列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFSERVICENAME
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- NRF性能对象管理
status: active
---

# LST NRFSERVICENAME（查看NRF功能实体服务列表）

## 功能

**适用NF：NRF**

该命令用于查看NRF功能实体服务列表。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFSERVICENAME]] · 查看NRF功能实体服务列表（NRFSERVICENAME）

## 使用实例

查询NRF功能实体服务列表：

```
LST NRFSERVICENAME:;
%%LST NRFSERVICENAME:;%%
RETCODE = 0  执行成功

操作结果如下:
-------------------------
NRF服务名称      

nrf-servcename001  
nrf-servcename002
nrf-servcename003
(结果个数 = 3)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFSERVICENAME.md`
