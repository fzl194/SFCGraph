---
id: UNC@20.15.2@MMLCommand@DSP NSSFSTARTSTAS
type: MMLCommand
name: DSP NSSFSTARTSTAS（显示NSSF开工状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NSSFSTARTSTAS
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF维测管理
status: active
---

# DSP NSSFSTARTSTAS（显示NSSF开工状态）

## 功能

**适用NF：NSSF**

查询NSSF微服务的开工状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NSSF开工状态（NSSFSTARTSTAS）](configobject/UNC/20.15.2/NSSFSTARTSTAS.md)

## 使用实例

查询所有NSSF微服务的开工状态：

```
%%DSP NSSFSTARTSTAS:;%%
RETCODE = 0  执行成功

结果如下
------------------------
微服务类型         功能实体名称                                            开工状态        

NSSF               nssf/cellcore/cell-service-NssfExecSvc                  状态正常 
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet2   状态正常  
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet3   状态正常
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet4   状态正常
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet5   状态正常
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet0   状态正常
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet1   状态正常
NSSF               ctrl/cellcore/cell-service-NssfCtrlSvc                  状态正常
(结果个数 = 8)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NSSF开工状态（DSP-NSSFSTARTSTAS）_64343869.md`
