---
id: UNC@20.15.2@MMLCommand@LST AGFOUTFC
type: MMLCommand
name: LST AGFOUTFC（查询出局流控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AGFOUTFC
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- AGF流控参数信息
status: active
---

# LST AGFOUTFC（查询出局流控参数）

## 功能

**适用NF：NCG**

该命令用于查询AGF出局流控参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AGFOUTFC]] · 出局流控参数（AGFOUTFC）

## 使用实例

查询AGF出局流控参数

```
+++    UNC/*MEID:0 MENAME:UNC_VNF_ncg2*/        2021-12-12 18:48:24+8:00
O&M    #1886
%%LST AGFOUTFC:;%%
RETCODE = 0  操作成功

结果如下
--------
                                出局流控模式  =  会话级和全局流控模式
                            全局流控阈值(次)  =  20000
                        全局流控恢复阈值(次)  =  4000
                            消息间隔条数(条)  =  10
                    会话级流控退出时长(分钟)  =  120
                会话级流控状态退避时长(分钟)  =  60
                            全局统计周期(秒)  =  60
                   是否统计TOPO发现失败次数   =  true
            全局流控状态最大退避时长(秒)      = 600
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AGFOUTFC.md`
