---
id: UNC@20.15.2@MMLCommand@LST AMFPLCYFUNC
type: MMLCommand
name: LST AMFPLCYFUNC（查询AMF策略功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFPLCYFUNC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AM策略和UE策略管理
- AMF策略功能管理
status: active
---

# LST AMFPLCYFUNC（查询AMF策略功能）

## 功能

**适用NF：AMF**

该命令用于查询AMF策略功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [AMF策略功能（AMFPLCYFUNC）](configobject/UNC/20.15.2/AMFPLCYFUNC.md)

## 使用实例

查询AMF策略功能，执行如下命令：

```
%%LST AMFPLCYFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
           AM策略关闭实时通知PCF开关  =  是
           UE策略关闭实时通知PCF开关  =  是
               N14接口是否传递AM策略  =  是
                    灵活选频功能开关  =  是
                        RFSP清除方式  =  未携带RFSP
                            默认RFSP  =  0
                  是否开启动态NI功能  =  是
                      默认运营商全称  =  FullName
                      默认运营商简称  =  ShortName
                    重叠区域生效策略  =  公网区域
                相邻位置区域处理开关  =  否
                  高铁AM偶联老化开关  =  否
             高铁AM偶联老化时长(min)  =  120
               N14接口是否传递UE策略  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF策略功能（LST-AMFPLCYFUNC）_96472701.md`
