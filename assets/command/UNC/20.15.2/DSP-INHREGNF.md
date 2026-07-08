---
id: UNC@20.15.2@MMLCommand@DSP INHREGNF
type: MMLCommand
name: DSP INHREGNF（显示禁止的NF）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: INHREGNF
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF实例管理
status: active
---

# DSP INHREGNF（显示禁止的NF）

## 功能

**适用NF：NRF**

该命令用于在NRF上查询通过INH REGNF命令禁止的NF实例。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [禁止的NF（INHREGNF）](configobject/UNC/20.15.2/INHREGNF.md)

## 使用实例

显示当前NRF上通过INH REGNF命令设置的被禁止的NF实例：

```
DSP INHREGNF:;
%%DSP INHREGNF:;%%
RETCODE = 0  执行成功

结果如下
-------------------------
NF实例标识       

123e4567-e89b-12d3-a456-426655440000     
123e4567-e89b-12d3-a456-426655440001      
123e4567-e89b-12d3-a456-426655440002
(结果个数 = 3)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示禁止的NF（DSP-INHREGNF）_09652300.md`
