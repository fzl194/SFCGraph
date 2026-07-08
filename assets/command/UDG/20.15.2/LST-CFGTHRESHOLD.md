---
id: UDG@20.15.2@MMLCommand@LST CFGTHRESHOLD
type: MMLCommand
name: LST CFGTHRESHOLD（查询配置对象告警阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CFGTHRESHOLD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 配置服务管理
- 维护管理
status: active
---

# LST CFGTHRESHOLD（查询配置对象告警阈值）

## 功能

该命令用于查询配置对象告警阈值。系统通过检测配置对象当前记录数与配置对象最大记录数的比值是否大于配置对象告警阈值决定是否上报“ALM-135602215 配置数量超阈值”。

> **说明**
> 无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| OBJECTNAME | 配置对象名称 | 可选必选说明：可选参数。<br>参数含义：用于指定配置对象名称。<br>取值范围：长度不超过16的字符串。<br>默认值：无。<br>配置原则：当不输入该参数时，表示查询所有配置对象的对象告警阈值。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CFGTHRESHOLD]] · 配置对象告警阈值（CFGTHRESHOLD）

## 使用实例

查询指定配置对象的配置对象告警阈值，执行以下命令：

```
%%LST CFGTHRESHOLD: OBJECTNAME="TcmcTypeInner";%%
RETCODE = 0  操作成功

操作结果如下
------------
                 配置对象名称  =  TcmcTypeInner
        配置对象告警阈值（%）  =  12
    配置对象告警恢复阈值（%）  =  12
           配置对象当前记录数  =  1
           配置对象最大记录数  =  100
配置对象当前记录数百分比（%）  =  1
         是否存在默认告警阈值  =  否
(结果个数 = 1)
```

查询所有配置对象告警阈值，执行以下命令：

```
%%LST CFGTHRESHOLD:;%%
RETCODE = 0  操作成功

操作结果如下
------------
配置对象名称   配置对象告警阈值（%）  配置对象告警恢复阈值（%）  配置对象当前记录数 配置对象最大记录数  配置对象当前记录数百分比（%）  是否存在默认告警阈值  

TcmcTypeInner  12                     12                         1                   100                 1                              否                    
TsdkTypeInner  10                     1                          1                   100                 1                              是                    
TsdkforSPS2    50                     30                         1                   100                 1                              否                    
testforSPS3    50                     40                         1                   100                 1                              否                    
testforSPS4    40                     30                         1                   100                 1                              否                    
(结果个数 = 5)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-CFGTHRESHOLD.md`
