---
id: UNC@20.15.2@MMLCommand@LST TLBGLBCONF
type: MMLCommand
name: LST TLBGLBCONF（查询TLB全局配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TLBGLBCONF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP服务端负载管理
- 整系统负载管理
- 全局属性
status: active
---

# LST TLBGLBCONF（查询TLB全局配置）

## 功能

该命令用于查询HTTP服务端TCP链路整系统负载均衡（TLB）的功能开关及相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [TLB全局配置（TLBGLBCONF）](configobject/UNC/20.15.2/TLBGLBCONF.md)

## 使用实例

如果想查询HTTP服务端TCP链路整系统负载均衡（TLB）的功能开关及相关参数，可以用如下命令：

```
%%LST TLBGLBCONF:;%%
RETCODE = 0  操作成功

结果如下
--------
                           TLB全局开关  =  打开
                              均衡模式  =  链路数控制
                   重均衡偏差阈值（%）  =  10
                  重均衡最小链路数阈值  =  5
              重均衡最小时间间隔（秒）  =  30
    接收TCP SYN报文的流控阈值（包/秒）  =  2000
上报直通TCP SYN报文的流控阈值（包/秒）  =  200
            临时五元组策略有效期（秒）  =  5
                        五元组核查开关  =  打开
                五元组核查周期（分钟）  =  30
                         五元组老化阈值 =  5
              TLB表项流控阈值（个/秒）  =  1000
                暂停TLB功能的阈值（%）  =  95
                恢复TLB功能的阈值（%）  =  85
                SYN包转发时延（毫秒）   =  20
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询TLB全局配置（LST-TLBGLBCONF）_15834601.md`
