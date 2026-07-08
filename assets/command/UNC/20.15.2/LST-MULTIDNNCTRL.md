---
id: UNC@20.15.2@MMLCommand@LST MULTIDNNCTRL
type: MMLCommand
name: LST MULTIDNNCTRL（查询2B2C漫游双DNN特性相关的功能控制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MULTIDNNCTRL
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 本地分流管理
- 2B2C双DNN控制
status: active
---

# LST MULTIDNNCTRL（查询2B2C漫游双DNN特性相关的功能控制）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询2B2C漫游双DNN特性相关的功能控制，如IdleTime功能、IP地址冲突检测、地址冲突时是否保留大网业务等参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MULTIDNNCTRL]] · 2B2C漫游双DNN特性相关的功能控制（MULTIDNNCTRL）

## 使用实例

查询所有MULTIDNNCTRL记录：

```
%%LST MULTIDNNCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
   MultiDnnSMF会话空闲定时器时长(min)  =  12000
                    UE IP地址冲突检测  =  使能
        UE IP地址检测冲突后重分配次数  =  10
UE IP地址冲突后是否丢弃MulDnnSessRule  =  丢弃MulDnnSessRule
             专网会话创建失败最大次数  =  3
            是否在EPS向UDM查询专用DNN  =  NULL
                  在EPS是否先获取策略  =  不使能
        锚点UPF无智能分流能力处理方式  =  丢弃MulDnnSessRule
            SMF无智能分流能力处理方式  =  丢弃MulDnnSessRule
             是否支持创建多个专网会话  =  不使能
               是否删除MulDnnSessRule  =  保留MulDnnSessRule
                       园区域名IP规格  =  900
                       特性冲突优先级  =  ULCL特性优先
                     特性冲突处理方式  =  保留PDU会话
     等待MULDNN-SMF响应定时器时长(秒)  =  16
            专网SMF重选和重试最大次数  =  0
                 专网会话创建抑制功能  =  专网会话创建抑制
     专网会话创建抑制定时器时长（秒）  =  300
                  专网DNN会话触发方式  =  延迟触发
                    UE IP地址转换位置  =  专网会话锚点UPF
                  园区DNN信元携带方式  =  请求DNN
   是否支持访地策略和智能分流同时生效  =  使能
                      是否支持就近接入 = 不使能
                        就近接入关键字 = ""
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MULTIDNNCTRL.md`
